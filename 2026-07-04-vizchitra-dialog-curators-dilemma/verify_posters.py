from __future__ import annotations

import asyncio
import json
from pathlib import Path

from playwright.async_api import async_playwright


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "_verify"
POSTERS = [
    ("01-statnostics.html", "portrait"),
    ("02-popular-actors.html", "landscape"),
    ("03-temporal-rosette.html", "landscape"),
    ("04-popularity-paradox.html", "landscape"),
    ("05-llm-pricing.html", "landscape"),
    ("06-gdpval.html", "landscape"),
]


async def main() -> None:
    OUT.mkdir(exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        context = browser.contexts[0]
        results = []
        for filename, orientation in POSTERS:
            page = await context.new_page()
            await page.set_viewport_size({"width": 1587, "height": 1587})
            await page.goto((ROOT / filename).as_uri(), wait_until="networkidle")
            await page.emulate_media(media="print")
            metrics = await page.evaluate(
                """() => {
                  const page = document.querySelector('.page');
                  const rect = page.getBoundingClientRect();
                  const content = [...document.querySelectorAll('svg, img, .chart-container, #treemap, .legend')]
                    .filter((el) => {
                      const r = el.getBoundingClientRect();
                      return r.width > 5 && r.height > 5;
                    })
                    .map((el) => {
                      const r = el.getBoundingClientRect();
                      return { tag: el.tagName, id: el.id, className: String(el.className || ''), x: r.x, y: r.y, width: r.width, height: r.height };
                    });
                  return { page: { width: rect.width, height: rect.height }, content };
                }"""
            )
            pdf_path = OUT / filename.replace(".html", ".pdf")
            png_path = OUT / filename.replace(".html", ".png")
            await page.pdf(
                path=str(pdf_path),
                prefer_css_page_size=True,
                print_background=True,
                margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            )
            await page.screenshot(path=str(png_path), full_page=True)
            results.append({"file": filename, "orientation": orientation, **metrics, "pdf": str(pdf_path), "png": str(png_path)})
            await page.close()
        await browser.close()
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
