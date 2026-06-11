"""
HEIM visual test harness.

This is a compact toy benchmark for moving-boundary methods:
1. A conforming annular mesh is forced to track increasingly complex boundaries.
2. A fixed background grid only sees a thin band of cut cells.
3. Local meshless/FEM-like stencils near an interface are compared:
   smooth cross-interface stencil vs phase-aware/enriched stencil.

Run:
    python heim_visual_test.py
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import json

OUT = Path("heim_visual_test_output")
OUT.mkdir(exist_ok=True)

def inner_radius(theta, k, amp=0.08, base=0.35):
    return base + amp * np.sin(k * theta)

def build_conforming_annulus_mesh(k, ntheta=None, nr=24, amp=0.08):
    if ntheta is None:
        ntheta = max(160, 16 * k)
    theta = np.linspace(0, 2*np.pi, ntheta, endpoint=False)
    rin = inner_radius(theta, k, amp=amp)
    rout = 1.0
    points = []
    for j in range(nr):
        s = j / (nr - 1)
        r = (1 - s) * rin + s * rout
        points.append(np.column_stack([r*np.cos(theta), r*np.sin(theta)]))
    points = np.vstack(points)
    triangles = []
    for j in range(nr - 1):
        for i in range(ntheta):
            a = j * ntheta + i
            b = j * ntheta + ((i + 1) % ntheta)
            c = (j + 1) * ntheta + i
            d = (j + 1) * ntheta + ((i + 1) % ntheta)
            triangles.append([a, c, d])
            triangles.append([a, d, b])
    return points, np.array(triangles), theta, rin

def triangle_quality(points, tris):
    p = points[tris]
    a = np.linalg.norm(p[:, 1] - p[:, 0], axis=1)
    b = np.linalg.norm(p[:, 2] - p[:, 1], axis=1)
    c = np.linalg.norm(p[:, 0] - p[:, 2], axis=1)
    area = 0.5 * np.abs(np.cross(p[:, 1] - p[:, 0], p[:, 2] - p[:, 0]))
    return 4*np.sqrt(3) * area / (a*a + b*b + c*c + 1e-15)

def phi_wavy_boundary(x, y, k, amp=0.08):
    th = np.arctan2(y, x)
    r = np.sqrt(x*x + y*y)
    return r - inner_radius(th, k, amp=amp)

def cut_cell_mask(k, N=192):
    xs = np.linspace(-1.05, 1.05, N+1)
    ys = np.linspace(-1.05, 1.05, N+1)
    cut = np.zeros((N, N), dtype=bool)
    for i in range(N):
        for j in range(N):
            corners = np.array([[xs[i], ys[j]], [xs[i+1], ys[j]], [xs[i], ys[j+1]], [xs[i+1], ys[j+1]]])
            ph = phi_wavy_boundary(corners[:,0], corners[:,1], k)
            cut[j, i] = ph.min() <= 0 <= ph.max()
    return cut, xs, ys

def f_interface(x):
    return 0.18 * np.sin(4*np.pi*x)

def phi_graph(x, y):
    return y - f_interface(x)

def true_u(x, y):
    ph = phi_graph(x, y)
    return np.sin(np.pi*x) + np.where(ph < 0, 0.5*ph, 2.5*ph)

def true_dudy(x, y):
    return np.where(phi_graph(x, y) < 0, 0.5, 2.5)

def local_design(dx, dy, ph_rel=None, mode="smooth"):
    cols = [np.ones_like(dx), dx, dy, dx*dx, dx*dy, dy*dy]
    if mode == "enriched":
        cols.append(np.maximum(ph_rel, 0.0))
    return np.column_stack(cols)

def main():
    ks = [1, 4, 8, 12, 16, 24, 32]
    geom_rows = []
    for k in ks:
        pts, tris, theta, rin = build_conforming_annulus_mesh(k)
        q = triangle_quality(pts, tris)
        geom_rows.append({"k": k, "nodes": len(pts), "elements": len(tris),
                          "min_quality": float(q.min()),
                          "median_quality": float(np.median(q)),
                          "bad_element_pct_q_lt_0_2": float(np.mean(q < 0.2) * 100)})

    pts, tris, theta, rin = build_conforming_annulus_mesh(24)
    plt.figure(figsize=(7, 7))
    plt.triplot(pts[:,0], pts[:,1], tris, linewidth=0.25)
    plt.plot(rin*np.cos(theta), rin*np.sin(theta), linewidth=2)
    plt.gca().set_aspect("equal")
    plt.title("Conforming mesh forced to track complex boundary")
    plt.tight_layout()
    plt.savefig(OUT / "conforming_mesh.png", dpi=180)

    plt.figure(figsize=(7, 4.8))
    plt.plot([r["k"] for r in geom_rows], [r["min_quality"] for r in geom_rows], marker="o", label="min")
    plt.plot([r["k"] for r in geom_rows], [r["median_quality"] for r in geom_rows], marker="o", label="median")
    plt.axhline(0.2, linestyle="--", linewidth=1)
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUT / "mesh_quality.png", dpi=180)

    cut, xs, ys = cut_cell_mask(24)
    plt.figure(figsize=(7, 7))
    plt.imshow(cut, origin="lower", extent=[xs[0], xs[-1], ys[0], ys[-1]])
    th = np.linspace(0, 2*np.pi, 2000, endpoint=False)
    r = inner_radius(th, 24)
    plt.plot(r*np.cos(th), r*np.sin(th), linewidth=2)
    plt.gca().set_aspect("equal")
    plt.title("Fixed grid: only cut cells near interface")
    plt.tight_layout()
    plt.savefig(OUT / "fixed_grid_cut_cells.png", dpi=180)

    rng = np.random.default_rng(7)
    n_nodes = 3000
    X = rng.uniform(-1.0, 1.0, n_nodes)
    Y = rng.uniform(-0.75, 0.75, n_nodes)
    U = true_u(X, Y)
    PH = phi_graph(X, Y)

    def estimate_dudy(x0, y0, method="smooth", k_near=80):
        dx = X - x0
        dy = Y - y0
        idx = np.argsort(dx*dx + dy*dy)[:k_near]
        if method in ["same_phase", "same_phase_bc"]:
            side0 = phi_graph(x0, y0) < 0
            idx = idx[(PH[idx] < 0) == side0]
            if len(idx) < 12:
                return np.nan
            A = local_design(dx[idx], dy[idx])
            b = U[idx].copy()
            if method == "same_phase_bc":
                xints = x0 + np.linspace(-0.08, 0.08, 9)
                yints = f_interface(xints)
                A_i = local_design(xints-x0, yints-y0)
                b_i = np.sin(np.pi*xints)
                A = np.vstack([A, 3.0*A_i])
                b = np.concatenate([b, 3.0*b_i])
        elif method == "enriched":
            A = local_design(dx[idx], dy[idx], ph_rel=phi_graph(X[idx], Y[idx]), mode="enriched")
            b = U[idx]
        else:
            A = local_design(dx[idx], dy[idx])
            b = U[idx]
        coef, *_ = np.linalg.lstsq(A, b, rcond=None)
        return coef[2]

    n_targets = 700
    TX = rng.uniform(-0.9, 0.9, n_targets)
    TY = f_interface(TX) - rng.uniform(0.005, 0.06, n_targets)
    exact = true_dudy(TX, TY)

    method_map = {
        "smooth": "Smooth stencil crossing interface",
        "same_phase": "Same-phase only",
        "same_phase_bc": "Same-phase + interface condition",
        "enriched": "Enriched kink basis",
    }
    rows = []
    all_errors = {}
    for key, label in method_map.items():
        vals = np.array([estimate_dudy(x, y, key) for x, y in zip(TX, TY)])
        err = np.abs(vals - exact)
        all_errors[label] = err
        err = err[np.isfinite(err)]
        rows.append({"method": label, "mae": float(err.mean()), "p95_abs_error": float(np.quantile(err, 0.95))})

    for label, fname, title in [
        ("Smooth stencil crossing interface", "naive_error.png", "Naive smooth stencil error"),
        ("Enriched kink basis", "enriched_error.png", "Interface-aware enriched stencil error"),
    ]:
        plt.figure(figsize=(7, 5.4))
        plt.scatter(TX, TY, c=all_errors[label], s=12)
        xx = np.linspace(-1, 1, 500)
        plt.plot(xx, f_interface(xx), linewidth=2)
        plt.colorbar(label="absolute derivative error")
        plt.title(title)
        plt.tight_layout()
        plt.savefig(OUT / fname, dpi=180)

    plt.figure(figsize=(8.5, 5))
    labels = [r["method"] for r in rows]
    plt.bar(np.arange(len(labels)), [r["mae"] for r in rows])
    plt.xticks(np.arange(len(labels)), labels, rotation=25, ha="right")
    plt.ylabel("mean absolute derivative error")
    plt.tight_layout()
    plt.savefig(OUT / "interface_error_bar.png", dpi=180)

    (OUT / "results.json").write_text(json.dumps({"geometry": geom_rows, "interface_error": rows}, indent=2))
    print(json.dumps({"geometry": geom_rows, "interface_error": rows}, indent=2))

if __name__ == "__main__":
    main()
