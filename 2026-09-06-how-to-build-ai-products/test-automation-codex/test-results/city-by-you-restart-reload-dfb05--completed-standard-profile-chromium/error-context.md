# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: city-by-you.spec.js >> restart, reload, network, and responsive behavior >> Build another city ↺ clears the completed standard profile
- Location: tests/city-by-you.spec.js:173:5

# Error details

```
Error: expect(locator).toHaveValue(expected) failed

Locator:  getByRole('spinbutton', { name: 'YOUR AGE' })
Expected: ""
Received: "30"
Timeout:  5000ms

Call log:
  - Expect "toHaveValue" getByRole('spinbutton', { name: 'YOUR AGE' }) with timeout 5000ms
  - waiting for getByRole('spinbutton', { name: 'YOUR AGE' })
    14 × locator resolved to <input min="8" max="120" type="number" id="age-input" inputmode="numeric" placeholder="e.g. 24"/>
       - unexpected value "30"

```

```yaml
- spinbutton "YOUR AGE": "30"
```

# Test source

```ts
  79  |       await expect(page.locator('#answers button.answer')).toHaveCount(5);
  80  |       await expect(page.getByRole('textbox', { name: /Other idea/ })).toHaveAttribute('maxlength', '54');
  81  |       const next = page.getByRole('button', { name: step === 7 ? 'See my city →' : 'Next →' });
  82  |       await expect(next).toBeDisabled();
  83  |       await page.locator('#answers button.answer').first().press('Enter');
  84  |       await expect(next).toBeEnabled();
  85  |       await next.click();
  86  |     }
  87  |     await expect(page.locator('#result')).toBeVisible();
  88  |   });
  89  | 
  90  |   test('back restores the prior selection and changing to a card clears custom text', async ({ page }) => {
  91  |     await startQuiz(page);
  92  |     const custom = page.getByRole('textbox', { name: /Other idea/ });
  93  |     await custom.fill('A public bath');
  94  |     await expect(page.getByRole('button', { name: 'Next →' })).toBeEnabled();
  95  |     await page.getByRole('button', { name: /A café/ }).click();
  96  |     await expect(custom).toHaveValue('');
  97  |     await page.getByRole('button', { name: 'Next →' }).click();
  98  |     await page.getByRole('button', { name: '← Back' }).click();
  99  | 
  100 |     await expect(page.getByRole('button', { name: /A café/ })).toHaveClass(/is-selected/);
  101 |     await expect(page.getByRole('button', { name: '← Back' })).toBeDisabled();
  102 |   });
  103 | 
  104 |   test('accepts an intentionally blank Other idea', async ({ page }) => {
  105 |     await startQuiz(page);
  106 |     await page.getByRole('textbox', { name: /Other idea/ }).focus();
  107 | 
  108 |     await expect(page.locator('.other-answer')).toHaveClass(/is-selected/);
  109 |     await expect(page.getByRole('button', { name: 'Next →' })).toBeEnabled();
  110 |   });
  111 | });
  112 | 
  113 | test.describe('results', () => {
  114 |   test('builds a complete deterministic city with art and three safe map links', async ({ page }) => {
  115 |     await finishWithStandardChoices(page, { age: '30', vibe: 'nature' });
  116 | 
  117 |     await expect(page.locator('#city-name')).toHaveText('The Greenroom City');
  118 |     await expect(page.locator('#city-description')).toContainText('It begins with a café');
  119 |     await expect(page.locator('#city-traits > span')).toHaveCount(10);
  120 |     await expect(page.locator('#city-art img')).toHaveAttribute('alt', 'A realistic city scene for The Greenroom City');
  121 |     await expect.poll(
  122 |       () => page.locator('#city-art img').evaluate(image => image.naturalWidth),
  123 |       { timeout: 15_000 },
  124 |     ).toBeGreaterThan(0);
  125 |     const places = page.locator('#world-match a.place');
  126 |     await expect(places).toHaveCount(3);
  127 |     for (const place of await places.all()) {
  128 |       await expect(place).toHaveAttribute('href', /^https:\/\/www\.google\.com\/maps\/search\//);
  129 |       await expect(place).toHaveAttribute('target', '_blank');
  130 |       await expect(place).toHaveAttribute('rel', 'noopener');
  131 |     }
  132 |   });
  133 | 
  134 |   for (const [vibe, title] of [
  135 |     ['calm', 'The Gentle City'],
  136 |     ['vibrant', 'The Brightside City'],
  137 |     ['creative', 'The Make-Believe City'],
  138 |     ['nature', 'The Greenroom City'],
  139 |     ['connected', 'The Common Ground'],
  140 |   ]) {
  141 |     test(`${vibe} produces ${title}`, async ({ page }) => {
  142 |       await finishWithStandardChoices(page, { age: '30', vibe });
  143 |       await expect(page.locator('#city-name')).toHaveText(title);
  144 |       await expect(page.locator('#city-traits')).toContainText(vibe);
  145 |     });
  146 |   }
  147 | 
  148 |   for (const [age, title] of [['16', 'The Open-Door City'], ['60', 'The Good Pace City']]) {
  149 |     test(`age ${age} produces ${title}`, async ({ page }) => {
  150 |       await finishWithStandardChoices(page, { age, vibe: 'creative' });
  151 |       await expect(page.locator('#city-name')).toHaveText(title);
  152 |     });
  153 |   }
  154 | 
  155 |   test('carries a custom answer, punctuation, and quotes into the result', async ({ page }) => {
  156 |     await startQuiz(page);
  157 |     const idea = 'Neighbors’ bakery & night café';
  158 |     await page.getByRole('textbox', { name: /Other idea/ }).fill(idea);
  159 |     await page.getByRole('button', { name: 'Next →' }).click();
  160 |     for (let step = 1; step < questions.length; step += 1) {
  161 |       await page.locator('#answers button.answer').first().click();
  162 |       await page.getByRole('button', { name: step === 7 ? 'See my city →' : 'Next →' }).click();
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
> 179 |       await expect(page.getByRole('spinbutton', { name: 'YOUR AGE' })).toHaveValue('');
      |                                                                        ^ Error: expect(locator).toHaveValue(expected) failed
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
  263 |     await expect(page.locator('#city-traits b, .custom-scene-note b')).toHaveCount(0);
  264 |   });
  265 | });
  266 | 
```