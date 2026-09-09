# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: city-by-you.spec.js >> known defects >> renders custom ideas as text, never as HTML
- Location: tests/city-by-you.spec.js:253:3

# Error details

```
Error: expect(locator).toHaveCount(expected) failed

Locator:  locator('#city-traits b, .custom-scene-note b')
Expected: 0
Received: 2
Timeout:  5000ms

Call log:
  - Expect "toHaveCount" locator('#city-traits b, .custom-scene-note b') with timeout 5000ms
  - waiting for locator('#city-traits b, .custom-scene-note b')
    14 × locator resolved to 2 elements
       - unexpected value "2"

```

# Page snapshot

```yaml
- main [ref=e2]:
  - generic [ref=e3]:
    - generic [ref=e4]:
      - link "Back to beginning" [ref=e5] [cursor=pointer]:
        - /url: "#intro"
        - text: CITY, BY YOU
      - button "Start over ↺" [ref=e6] [cursor=pointer]
    - generic [ref=e7]:
      - generic [ref=e8]:
        - paragraph [ref=e9]: YOUR MAYORAL VISION
        - heading "The Greenroom City" [level=2] [ref=e11]
        - paragraph [ref=e12]: A city where trees, water, and shared green spaces lead the way. Your own idea — “<b>community bakery</b>” — shapes the scene you see here. It begins with <b>community bakery</b> and keeps a big park at its heart.
        - generic [ref=e13]:
          - generic [ref=e14]: Age 30
          - generic [ref=e15]: nature
          - generic [ref=e16]: community bakery
          - generic [ref=e17]: A shaded canopy
          - generic [ref=e18]: Lively
          - generic [ref=e19]: A big park
          - generic [ref=e20]: Bike lanes
          - generic [ref=e21]: A public library
          - generic [ref=e22]: Circular reuse
          - generic [ref=e23]: Sidewalk breakfast
        - button "Build another city ↺" [ref=e24] [cursor=pointer]
      - generic [ref=e25]:
        - img "An illustration of your ideal city" [ref=e26]:
          - img "A realistic city scene for The Greenroom City" [ref=e27]
          - generic [ref=e28]: "YOUR IDEA: community bakery"
        - paragraph [ref=e29]: An original city, imagined by you.
      - generic [ref=e30]:
        - heading "PLACES YOU MAY LOVE" [level=3] [ref=e31]
        - paragraph [ref=e32]: Matched to the choices you made. Tap a place to explore it on Google Maps.
        - generic [ref=e33]:
          - 'link "01 Bologna Italy · Emilia-Romagna MATCHED FOR: Canopy · Lively · Library WALK GREEN CULTURE EASE MAP ↗" [ref=e34] [cursor=pointer]':
            - /url: https://www.google.com/maps/search/?api=1&query=Bologna%2C%20Italy
            - generic [ref=e35]: "01"
            - generic [ref=e36]:
              - strong [ref=e37]: Bologna
              - generic [ref=e38]: Italy · Emilia-Romagna
              - generic [ref=e39]: "MATCHED FOR: Canopy · Lively · Library"
              - generic [ref=e40]:
                - generic [ref=e41]: WALK
                - generic [ref=e46]: GREEN
                - generic [ref=e51]: CULTURE
                - generic [ref=e56]: EASE
            - generic [ref=e61]: MAP ↗
          - 'link "02 Copenhagen Denmark · Northern Europe MATCHED FOR: Park · Bike · Library WALK GREEN CULTURE EASE MAP ↗" [ref=e62] [cursor=pointer]':
            - /url: https://www.google.com/maps/search/?api=1&query=Copenhagen%2C%20Denmark
            - generic [ref=e63]: "02"
            - generic [ref=e64]:
              - strong [ref=e65]: Copenhagen
              - generic [ref=e66]: Denmark · Northern Europe
              - generic [ref=e67]: "MATCHED FOR: Park · Bike · Library"
              - generic [ref=e68]:
                - generic [ref=e69]: WALK
                - generic [ref=e74]: GREEN
                - generic [ref=e79]: CULTURE
                - generic [ref=e84]: EASE
            - generic [ref=e89]: MAP ↗
          - 'link "03 Taipei Taiwan MATCHED FOR: Canopy · Lively · Library WALK GREEN CULTURE EASE MAP ↗" [ref=e90] [cursor=pointer]':
            - /url: https://www.google.com/maps/search/?api=1&query=Taipei%2C%20Taiwan
            - generic [ref=e91]: "03"
            - generic [ref=e92]:
              - strong [ref=e93]: Taipei
              - generic [ref=e94]: Taiwan
              - generic [ref=e95]: "MATCHED FOR: Canopy · Lively · Library"
              - generic [ref=e96]:
                - generic [ref=e97]: WALK
                - generic [ref=e102]: GREEN
                - generic [ref=e107]: CULTURE
                - generic [ref=e112]: EASE
            - generic [ref=e117]: MAP ↗
```

# Test source

```ts
  163 |     }
  164 | 
  165 |     await expect(page.locator('#city-description')).toContainText(idea);
  166 |     await expect(page.locator('#city-traits')).toContainText(idea);
  167 |     await expect(page.locator('.custom-scene-note')).toContainText(idea);
  168 |   });
  169 | });
  170 | 
  171 | test.describe('restart, reload, network, and responsive behavior', () => {
  172 |   for (const restartName of ['Start over ↺', 'Build another city ↺']) {
  173 |     test(`${restartName} clears the completed standard profile`, async ({ page }) => {
  174 |       test.fail(true, 'Known defect: restart() shows the intro without clearing its fields.');
  175 |       await finishWithStandardChoices(page);
  176 |       await page.getByRole('button', { name: restartName }).click();
  177 | 
  178 |       await expect(page.locator('#intro')).toBeVisible();
  179 |       await expect(page.getByRole('spinbutton', { name: 'YOUR AGE' })).toHaveValue('');
  180 |       await expect(page.getByRole('combobox', { name: 'YOUR FAVORITE ATMOSPHERE' })).toHaveValue('');
  181 |     });
  182 |   }
  183 | 
  184 |   test('reload discards the in-memory quiz', async ({ page }) => {
  185 |     await startQuiz(page);
  186 |     await page.locator('#answers button.answer').first().click();
  187 |     await page.reload();
  188 | 
  189 |     await expect(page.locator('#intro')).toBeVisible();
  190 |     await expect(page.getByRole('spinbutton', { name: 'YOUR AGE' })).toHaveValue('');
  191 |   });
  192 | 
  193 |   test('normal use makes no application API requests', async ({ page }) => {
  194 |     const apiRequests = [];
  195 |     page.on('request', request => {
  196 |       const { pathname } = new URL(request.url());
  197 |       if (['fetch', 'xhr'].includes(request.resourceType()) && !pathname.startsWith('/cdn-cgi/')) {
  198 |         apiRequests.push(request.url());
  199 |       }
  200 |     });
  201 |     await finishWithStandardChoices(page);
  202 |     expect(apiRequests).toEqual([]);
  203 |   });
  204 | 
  205 |   test('all shipped scripts, styles, and city images are reachable', async ({ request }) => {
  206 |     for (const path of ['/styles.css', '/app.js', '/variant.js', '/custom.js', '/spots.js']) {
  207 |       expect((await request.get(path)).ok(), path).toBeTruthy();
  208 |     }
  209 |     for (const asset of assets) {
  210 |       const response = await request.get(`/assets/${asset}.png`);
  211 |       expect(response.ok(), asset).toBeTruthy();
  212 |       expect(response.headers()['content-type'], asset).toContain('image/png');
  213 |     }
  214 |   });
  215 | 
  216 |   test('desktop grid becomes a single readable mobile column without overflow', async ({ page }) => {
  217 |     await page.setViewportSize({ width: 1280, height: 800 });
  218 |     await startQuiz(page);
  219 |     const cards = page.locator('#answers button.answer');
  220 |     const desktopFirst = await cards.nth(0).boundingBox();
  221 |     const desktopSecond = await cards.nth(1).boundingBox();
  222 |     expect(desktopFirst?.x).not.toBe(desktopSecond?.x);
  223 | 
  224 |     await page.setViewportSize({ width: 390, height: 844 });
  225 |     const mobileFirst = await cards.nth(0).boundingBox();
  226 |     const mobileSecond = await cards.nth(1).boundingBox();
  227 |     expect(Math.abs((mobileFirst?.x ?? 0) - (mobileSecond?.x ?? 0))).toBeLessThan(2);
  228 |     expect((mobileSecond?.y ?? 0)).toBeGreaterThan(mobileFirst?.y ?? 0);
  229 |     const overflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
  230 |     expect(overflow).toBeLessThanOrEqual(1);
  231 |   });
  232 | });
  233 | 
  234 | test.describe('known defects', () => {
  235 |   test('restart clears custom answers from the next run', async ({ page }) => {
  236 |     test.fail(true, 'Known defect: customAnswers is not reset by restart().');
  237 |     await startQuiz(page);
  238 |     await page.getByRole('textbox', { name: /Other idea/ }).fill('A public bath');
  239 |     await page.getByRole('button', { name: 'Next →' }).click();
  240 |     for (let step = 1; step < questions.length; step += 1) {
  241 |       await page.locator('#answers button.answer').first().click();
  242 |       await page.getByRole('button', { name: step === 7 ? 'See my city →' : 'Next →' }).click();
  243 |     }
  244 |     await page.getByRole('button', { name: 'Start over ↺' }).click();
  245 |     await page.getByRole('spinbutton', { name: 'YOUR AGE' }).fill('30');
  246 |     await page.getByRole('combobox', { name: 'YOUR FAVORITE ATMOSPHERE' }).selectOption('nature');
  247 |     await page.getByRole('button', { name: 'Start building →' }).click();
  248 | 
  249 |     await expect(page.getByRole('textbox', { name: /Other idea/ })).toHaveValue('');
  250 |     await expect(page.locator('.other-answer')).not.toHaveClass(/is-selected/);
  251 |   });
  252 | 
  253 |   test('renders custom ideas as text, never as HTML', async ({ page }) => {
  254 |     test.fail(true, 'Known defect: custom ideas are interpolated into result innerHTML without escaping.');
  255 |     await startQuiz(page);
  256 |     await page.getByRole('textbox', { name: /Other idea/ }).fill('<b>community bakery</b>');
  257 |     await page.getByRole('button', { name: 'Next →' }).click();
  258 |     for (let step = 1; step < questions.length; step += 1) {
  259 |       await page.locator('#answers button.answer').first().click();
  260 |       await page.getByRole('button', { name: step === 7 ? 'See my city →' : 'Next →' }).click();
  261 |     }
  262 | 
> 263 |     await expect(page.locator('#city-traits b, .custom-scene-note b')).toHaveCount(0);
      |                                                                        ^ Error: expect(locator).toHaveCount(expected) failed
  264 |   });
  265 | });
  266 | 
```