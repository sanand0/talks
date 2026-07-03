from __future__ import annotations

import asyncio
import html
import json
from pathlib import Path

from playwright.async_api import async_playwright


ROOT = Path(__file__).resolve().parent

A3 = {
    "portrait": ("297mm", "420mm"),
    "landscape": ("420mm", "297mm"),
}


POSTER_CSS = """
* { box-sizing: border-box; }
html, body { margin: 0; min-height: 100%; background: #fff; }
body {
  font-family: Avenir Next, Optima, Candara, Segoe UI, sans-serif;
  color: #111827;
}
@page { size: var(--page-width) var(--page-height); margin: 0; }
.page {
  width: var(--page-width);
  height: var(--page-height);
  overflow: hidden;
  background: #fff;
  display: flex;
  flex-direction: column;
  padding: var(--page-padding, 0);
}
.fit {
  flex: 1 1 auto;
  min-height: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}
.fit > svg,
.fit > img,
.fit > .fragment {
  width: 100% !important;
  height: 100% !important;
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}
svg { overflow: visible; }
.title {
  font-size: 28pt;
  line-height: 1.05;
  margin: 0 0 8mm;
  font-weight: 700;
}
.description {
  font-size: 13pt;
  line-height: 1.35;
  margin: -4mm 0 7mm;
  color: #374151;
  max-width: 330mm;
}
@media screen {
  body {
    min-height: 100vh;
    display: grid;
    place-items: center;
    background:
      linear-gradient(45deg, #e5e7eb 25%, transparent 25%),
      linear-gradient(-45deg, #e5e7eb 25%, transparent 25%),
      linear-gradient(45deg, transparent 75%, #e5e7eb 75%),
      linear-gradient(-45deg, transparent 75%, #e5e7eb 75%);
    background-size: 24px 24px;
    background-position: 0 0, 0 12px, 12px -12px, -12px 0;
  }
  .page { box-shadow: 0 12px 40px rgb(0 0 0 / 0.22); }
}
@media print {
  body { print-color-adjust: exact; -webkit-print-color-adjust: exact; }
  .page { box-shadow: none; }
}
"""


def page_html(title: str, orientation: str, body: str, padding: str = "0", extra_css: str = "") -> str:
    width, height = A3[orientation]
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>
:root {{
  --page-width: {width};
  --page-height: {height};
  --page-padding: {padding};
}}
{POSTER_CSS}
{extra_css}
</style>
</head>
<body>
<main class="page">
{body}
</main>
</body>
</html>
"""


async def get_page(context, url_part: str):
    for page in context.pages:
        if url_part in page.url:
            await page.bring_to_front()
            await page.wait_for_load_state("domcontentloaded")
            return page
    page = await context.new_page()
    await page.goto(url_part, wait_until="networkidle")
    return page


async def absolutize_fragment(page, selector: str, inline_images: bool = False) -> str:
    return await page.locator(selector).evaluate(
        """async (node, inlineImages) => {
          const clone = node.cloneNode(true);
          const base = document.baseURI;
          const attrs = ["href", "src", "xlink:href"];
          const originalNodes = [node, ...node.querySelectorAll("*")];
          const cloneNodes = [clone, ...clone.querySelectorAll("*")];
          cloneNodes.forEach((el, index) => {
            const original = originalNodes[index];
            if (original) {
              const computed = getComputedStyle(original);
              const keep = [
                "background", "background-color", "border", "border-radius", "box-shadow",
                "color", "display", "fill", "font", "font-family", "font-size", "font-style",
                "font-weight", "height", "justify-content", "line-height", "margin",
                "opacity", "overflow", "padding", "position", "stroke", "stroke-width",
                "text-anchor", "text-align", "transform", "visibility", "white-space",
                "width"
              ];
              const inline = keep
                .map((name) => `${name}: ${computed.getPropertyValue(name)};`)
                .join(" ");
              el.setAttribute("style", `${inline} ${el.getAttribute("style") || ""}`.trim());
            }
            for (const attr of attrs) {
              const value = el.getAttribute(attr);
              if (value && !value.startsWith("#") && !value.startsWith("data:") && !value.startsWith("blob:")) {
                el.setAttribute(attr, new URL(value, base).href);
              }
            }
            const style = el.getAttribute("style");
            if (style && style.includes("url(")) {
              el.setAttribute("style", style.replace(/url\\((['"]?)(?!data:|https?:|#)([^'")]+)\\1\\)/g, (_, q, path) => `url(${q}${new URL(path, base).href}${q})`));
            }
          });
          if (inlineImages) {
            await Promise.all([...clone.querySelectorAll("image")].map(async (image) => {
              const href = image.getAttribute("href") || image.getAttribute("xlink:href");
              if (!href || href.startsWith("data:")) return;
              const response = await fetch(href);
              const blob = await response.blob();
              const dataUrl = await new Promise((resolve) => {
                const reader = new FileReader();
                reader.onloadend = () => resolve(reader.result);
                reader.readAsDataURL(blob);
              });
              image.setAttribute("href", dataUrl);
              image.setAttribute("xlink:href", dataUrl);
            }));
          }
          return clone.outerHTML;
        }""",
        inline_images,
    )


async def svg_page(
    context,
    url: str,
    output: str,
    title: str,
    orientation: str,
    padding: str = "0",
    fit_class: str = "fit",
    extra_css: str = "",
) -> dict:
    page = await context.new_page()
    await page.goto(url, wait_until="networkidle")
    svg = await page.locator("svg").first.evaluate("node => node.outerHTML")
    await page.close()
    (ROOT / output).write_text(
        page_html(title, orientation, f'<section class="{fit_class}">{svg}</section>', padding, extra_css),
        encoding="utf-8",
    )
    return {"file": output, "selector": "svg", "orientation": orientation}


async def capture_light_rosette(context) -> None:
    page = await context.new_page()
    await page.set_viewport_size({"width": 1874, "height": 1049})
    await page.goto("https://sanand0.github.io/datastories/novel-dataviz/", wait_until="networkidle")
    await page.wait_for_selector("#s3")
    await page.evaluate(
        """() => {
          nav.go(3);
          location.hash = "s3";
        }"""
    )
    await page.wait_for_selector("#c3 svg")
    await page.add_style_tag(
        content="""
html,
body,
#s3 {
  background: #fff !important;
}
#s3 {
  color: #111827 !important;
}
#s3 .info {
  background: #fff !important;
  border-right: 1px solid #cbd5e1 !important;
  color: #111827 !important;
}
#s3 .info-title,
#s3 .info-sub,
#s3 .info-block-t,
#s3 .info-block-t b {
  color: #111827 !important;
  opacity: 1 !important;
}
#s3 .info-num,
#s3 .info-block-h,
#s3 .info-hint {
  color: #475569 !important;
  opacity: 1 !important;
}
#s3 .viz {
  background: #fff !important;
  overflow: visible !important;
}
#s3 .viz svg {
  transform: scale(1.05);
  transform-origin: center center;
}
#s3 .viz svg line {
  stroke: rgba(100, 116, 139, 0.32) !important;
}
#nav {
  display: none !important;
}
"""
    )
    await page.locator("#s3 svg [opacity]").evaluate_all(
        """nodes => nodes.forEach((node) => {
          const value = Number(node.getAttribute("opacity"));
          if (Number.isFinite(value) && value < 0.45) node.setAttribute("opacity", "0.45");
        })"""
    )
    await page.wait_for_timeout(500)
    assets = ROOT / "assets"
    assets.mkdir(exist_ok=True)
    await page.locator("#s3").screenshot(path=str(assets / "03-temporal-rosette.png"))
    await page.close()


async def capture_gdpval(context) -> None:
    page = await context.new_page()
    await page.set_viewport_size({"width": 2400, "height": 1800})
    await page.goto("https://sanand0.github.io/datastories/gdpval/", wait_until="networkidle")
    await page.wait_for_selector("#treemap svg")
    assets = ROOT / "assets"
    assets.mkdir(exist_ok=True)
    await page.locator(".container").screenshot(path=str(assets / "06-gdpval.png"))
    await page.close()


async def main() -> None:
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        context = browser.contexts[0]

        results = []
        results.append(
            await svg_page(
                context,
                "https://sanand0.github.io/journalists/statnostics/2026-04-27-citizen-survey/05-educated-waiting.svg",
                "01-statnostics.html",
                "Statnostics",
                "portrait",
                fit_class="fit statnostics-page",
                extra_css="""
.statnostics-page > svg {
  width: 100% !important;
  height: auto !important;
  max-height: 100% !important;
}
""",
            )
        )

        image_page = await get_page(context, "https://imageexplore.straivedemo.com/")
        await image_page.wait_for_selector("svg#similarity", timeout=15000)
        popular_actors = await absolutize_fragment(image_page, "svg#similarity", inline_images=True)
        (ROOT / "02-popular-actors.html").write_text(
            page_html(
                "Popular Actors",
                "landscape",
                f"""
<section style="padding: 15mm 18mm 10mm; display: flex; flex-direction: column; min-height: 100%;">
  <h1 class="title">Popular Actors</h1>
  <p class="description">The X axis represents how &quot;Chinese&quot; each actor's photo looks. The Y axis represents how &quot;African&quot; each actor's photo looks.</p>
  <div class="fit">{popular_actors}</div>
</section>
""",
            ),
            encoding="utf-8",
        )
        results.append({"file": "02-popular-actors.html", "selector": "svg#similarity", "orientation": "landscape"})

        await capture_light_rosette(context)
        (ROOT / "03-temporal-rosette.html").write_text(
            page_html(
                "Temporal Rosette",
                "landscape",
                '<section class="fit"><img src="assets/03-temporal-rosette.png" alt="Temporal Rosette slide" style="width: 100%; height: 100%; object-fit: contain;"></section>',
            ),
            encoding="utf-8",
        )
        results.append({"file": "03-temporal-rosette.html", "selector": "#s3 screenshot", "orientation": "landscape"})

        imdb_page = await get_page(context, "https://sanand0.github.io/datastories/imdb-democracy-penalty/")
        paradox = await imdb_page.locator(".chart-container").filter(has=imdb_page.locator(".chart-title", has_text="The Popularity Paradox")).evaluate("node => node.outerHTML")
        (ROOT / "04-popularity-paradox.html").write_text(
            page_html(
                "The Popularity Paradox",
                "landscape",
                f'<section class="fit paradox-page"><div class="fragment">{paradox}</div></section>',
                "8mm",
                extra_css="""
.paradox-page .chart-container {
  padding: 0 !important;
  background: #fff !important;
}
.paradox-page .chart-title {
  color: #111827 !important;
  font-family: Avenir Next, Optima, Candara, Segoe UI, sans-serif !important;
  font-size: 30pt !important;
  font-weight: 800 !important;
  line-height: 1.05 !important;
  margin: 0 0 3mm !important;
  text-align: left !important;
}
.paradox-page .chart-subtitle {
  color: #4b5563 !important;
  font-family: Avenir Next, Optima, Candara, Segoe UI, sans-serif !important;
  font-size: 13pt !important;
  line-height: 1.35 !important;
  margin: 0 0 5mm !important;
  max-width: 330mm !important;
  text-align: left !important;
}
""",
            ),
            encoding="utf-8",
        )
        results.append({"file": "04-popularity-paradox.html", "selector": ".chart-container:has(.chart-title)", "orientation": "landscape"})

        llm_page = await get_page(context, "https://sanand0.github.io/llmpricing/")
        await llm_page.wait_for_selector("#llm-cost svg", timeout=20000)
        llm = await absolutize_fragment(llm_page, "#llm-cost svg")
        (ROOT / "05-llm-pricing.html").write_text(
            page_html(
                "LLM Model Pricing",
                "landscape",
                f"""
<section style="padding: 10mm 8mm 8mm; display: flex; flex-direction: column; min-height: 100%;">
  <h1 class="title" style="margin-bottom: 4mm;">LLM Model Pricing</h1>
  <div class="fit">{llm}</div>
</section>
""",
            ),
            encoding="utf-8",
        )
        results.append({"file": "05-llm-pricing.html", "selector": "#llm-cost svg", "orientation": "landscape"})

        await capture_gdpval(context)
        (ROOT / "06-gdpval.html").write_text(
            page_html(
                "GDPVal",
                "landscape",
                '<section class="fit"><img src="assets/06-gdpval.png" alt="GDPVal full page" style="width: 100%; height: 100%; object-fit: contain;"></section>',
                extra_css="""
body { background: #fff; }
""",
            ),
            encoding="utf-8",
        )
        results.append({"file": "06-gdpval.html", "selector": ".container screenshot", "orientation": "landscape"})

        await browser.close()
        print(json.dumps(results, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
