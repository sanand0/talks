// @ts-check
const { test, expect } = require('@playwright/test');

const questions = [
  ['01 / 08', 'What should greet you at the station?'],
  ['02 / 08', 'On a hot street, what do you reach for?'],
  ['03 / 08', 'How should your evenings feel?'],
  ['04 / 08', 'Where do people spend a slow Sunday?'],
  ['05 / 08', 'What makes moving through town a pleasure?'],
  ['06 / 08', 'Which shared space would you fund first?'],
  ['07 / 08', 'Which small change feels most meaningful?'],
  ['08 / 08', 'What should happen on an ordinary morning?'],
];

const assets = [
  'city-quiet', 'city-lively', 'city-creative', 'city-nature', 'city-connected',
  'city-food', 'city-music', 'city-cafe', 'city-mall', 'city-corner',
  'city-library', 'city-canopy', 'city-mist', 'city-solar', 'city-maker',
  'city-amusement',
];

async function startQuiz(page, { age = '30', vibe = 'nature' } = {}) {
  await page.goto('/');
  await page.getByRole('spinbutton', { name: 'YOUR AGE' }).fill(age);
  await page.getByRole('combobox', { name: 'YOUR FAVORITE ATMOSPHERE' }).selectOption(vibe);
  await page.getByRole('button', { name: 'Start building →' }).click();
  await expect(page.locator('#quiz')).toBeVisible();
}

async function finishWithStandardChoices(page, profile = {}) {
  await startQuiz(page, profile);
  for (let step = 0; step < questions.length; step += 1) {
    await page.locator('#answers button.answer').first().click();
    await page.getByRole('button', { name: step === 7 ? 'See my city →' : 'Next →' }).click();
  }
  await expect(page.locator('#result')).toBeVisible();
}

test.describe('landing and profile validation', () => {
  test('shows the complete landing form and five atmosphere choices', async ({ page }) => {
    await page.goto('/');

    await expect(page.getByRole('heading', { level: 1 })).toContainText('If you could build a city');
    await expect(page.getByText('8 questions · about 2 minutes')).toBeVisible();
    await expect(page.locator('#intro')).toBeVisible();
    await expect(page.locator('#quiz')).toBeHidden();
    await expect(page.locator('#result')).toBeHidden();
    await expect(page.getByRole('combobox', { name: 'YOUR FAVORITE ATMOSPHERE' }).locator('option')).toHaveCount(6);
  });

  for (const { label, age, vibe = 'nature' } of [
    { label: 'both fields blank', age: '', vibe: '' },
    { label: 'atmosphere blank', age: '30', vibe: '' },
    { label: 'age below 8', age: '7' },
    { label: 'age above 120', age: '121' },
    { label: 'zero age', age: '0' },
  ]) {
    test(`blocks ${label}`, async ({ page }) => {
      await page.goto('/');
      if (age) await page.getByRole('spinbutton', { name: 'YOUR AGE' }).fill(age);
      if (vibe) await page.getByRole('combobox', { name: 'YOUR FAVORITE ATMOSPHERE' }).selectOption(vibe);
      await page.getByRole('button', { name: 'Start building →' }).click();

      await expect(page.getByText('Please add your age and favorite atmosphere.')).toBeVisible();
      await expect(page.locator('#intro')).toBeVisible();
      await expect(page.locator('#quiz')).toBeHidden();
    });
  }
});

test.describe('quiz mechanics', () => {
  test('presents all eight questions and requires one choice per step', async ({ page }) => {
    await startQuiz(page);

    for (let step = 0; step < questions.length; step += 1) {
      const [count, title] = questions[step];
      await expect(page.locator('#question-count')).toHaveText(count);
      await expect(page.getByRole('heading', { level: 2 })).toHaveText(title);
      await expect(page.locator('#answers button.answer')).toHaveCount(5);
      await expect(page.getByRole('textbox', { name: /Other idea/ })).toHaveAttribute('maxlength', '54');
      const next = page.getByRole('button', { name: step === 7 ? 'See my city →' : 'Next →' });
      await expect(next).toBeDisabled();
      await page.locator('#answers button.answer').first().press('Enter');
      await expect(next).toBeEnabled();
      await next.click();
    }
    await expect(page.locator('#result')).toBeVisible();
  });

  test('back restores the prior selection and changing to a card clears custom text', async ({ page }) => {
    await startQuiz(page);
    const custom = page.getByRole('textbox', { name: /Other idea/ });
    await custom.fill('A public bath');
    await expect(page.getByRole('button', { name: 'Next →' })).toBeEnabled();
    await page.getByRole('button', { name: /A café/ }).click();
    await expect(custom).toHaveValue('');
    await page.getByRole('button', { name: 'Next →' }).click();
    await page.getByRole('button', { name: '← Back' }).click();

    await expect(page.getByRole('button', { name: /A café/ })).toHaveClass(/is-selected/);
    await expect(page.getByRole('button', { name: '← Back' })).toBeDisabled();
  });

  test('accepts an intentionally blank Other idea', async ({ page }) => {
    await startQuiz(page);
    await page.getByRole('textbox', { name: /Other idea/ }).focus();

    await expect(page.locator('.other-answer')).toHaveClass(/is-selected/);
    await expect(page.getByRole('button', { name: 'Next →' })).toBeEnabled();
  });
});

test.describe('results', () => {
  test('builds a complete deterministic city with art and three safe map links', async ({ page }) => {
    await finishWithStandardChoices(page, { age: '30', vibe: 'nature' });

    await expect(page.locator('#city-name')).toHaveText('The Greenroom City');
    await expect(page.locator('#city-description')).toContainText('It begins with a café');
    await expect(page.locator('#city-traits > span')).toHaveCount(10);
    await expect(page.locator('#city-art img')).toHaveAttribute('alt', 'A realistic city scene for The Greenroom City');
    await expect.poll(
      () => page.locator('#city-art img').evaluate(image => image.naturalWidth),
      { timeout: 15_000 },
    ).toBeGreaterThan(0);
    const places = page.locator('#world-match a.place');
    await expect(places).toHaveCount(3);
    for (const place of await places.all()) {
      await expect(place).toHaveAttribute('href', /^https:\/\/www\.google\.com\/maps\/search\//);
      await expect(place).toHaveAttribute('target', '_blank');
      await expect(place).toHaveAttribute('rel', 'noopener');
    }
  });

  for (const [vibe, title] of [
    ['calm', 'The Gentle City'],
    ['vibrant', 'The Brightside City'],
    ['creative', 'The Make-Believe City'],
    ['nature', 'The Greenroom City'],
    ['connected', 'The Common Ground'],
  ]) {
    test(`${vibe} produces ${title}`, async ({ page }) => {
      await finishWithStandardChoices(page, { age: '30', vibe });
      await expect(page.locator('#city-name')).toHaveText(title);
      await expect(page.locator('#city-traits')).toContainText(vibe);
    });
  }

  for (const [age, title] of [['16', 'The Open-Door City'], ['60', 'The Good Pace City']]) {
    test(`age ${age} produces ${title}`, async ({ page }) => {
      await finishWithStandardChoices(page, { age, vibe: 'creative' });
      await expect(page.locator('#city-name')).toHaveText(title);
    });
  }

  test('carries a custom answer, punctuation, and quotes into the result', async ({ page }) => {
    await startQuiz(page);
    const idea = 'Neighbors’ bakery & night café';
    await page.getByRole('textbox', { name: /Other idea/ }).fill(idea);
    await page.getByRole('button', { name: 'Next →' }).click();
    for (let step = 1; step < questions.length; step += 1) {
      await page.locator('#answers button.answer').first().click();
      await page.getByRole('button', { name: step === 7 ? 'See my city →' : 'Next →' }).click();
    }

    await expect(page.locator('#city-description')).toContainText(idea);
    await expect(page.locator('#city-traits')).toContainText(idea);
    await expect(page.locator('.custom-scene-note')).toContainText(idea);
  });
});

test.describe('restart, reload, network, and responsive behavior', () => {
  for (const restartName of ['Start over ↺', 'Build another city ↺']) {
    test(`${restartName} clears the completed standard profile`, async ({ page }) => {
      test.fail(true, 'Known defect: restart() shows the intro without clearing its fields.');
      await finishWithStandardChoices(page);
      await page.getByRole('button', { name: restartName }).click();

      await expect(page.locator('#intro')).toBeVisible();
      await expect(page.getByRole('spinbutton', { name: 'YOUR AGE' })).toHaveValue('');
      await expect(page.getByRole('combobox', { name: 'YOUR FAVORITE ATMOSPHERE' })).toHaveValue('');
    });
  }

  test('reload discards the in-memory quiz', async ({ page }) => {
    await startQuiz(page);
    await page.locator('#answers button.answer').first().click();
    await page.reload();

    await expect(page.locator('#intro')).toBeVisible();
    await expect(page.getByRole('spinbutton', { name: 'YOUR AGE' })).toHaveValue('');
  });

  test('normal use makes no application API requests', async ({ page }) => {
    const apiRequests = [];
    page.on('request', request => {
      const { pathname } = new URL(request.url());
      if (['fetch', 'xhr'].includes(request.resourceType()) && !pathname.startsWith('/cdn-cgi/')) {
        apiRequests.push(request.url());
      }
    });
    await finishWithStandardChoices(page);
    expect(apiRequests).toEqual([]);
  });

  test('all shipped scripts, styles, and city images are reachable', async ({ request }) => {
    for (const path of ['/styles.css', '/app.js', '/variant.js', '/custom.js', '/spots.js']) {
      expect((await request.get(path)).ok(), path).toBeTruthy();
    }
    for (const asset of assets) {
      const response = await request.get(`/assets/${asset}.png`);
      expect(response.ok(), asset).toBeTruthy();
      expect(response.headers()['content-type'], asset).toContain('image/png');
    }
  });

  test('desktop grid becomes a single readable mobile column without overflow', async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await startQuiz(page);
    const cards = page.locator('#answers button.answer');
    const desktopFirst = await cards.nth(0).boundingBox();
    const desktopSecond = await cards.nth(1).boundingBox();
    expect(desktopFirst?.x).not.toBe(desktopSecond?.x);

    await page.setViewportSize({ width: 390, height: 844 });
    const mobileFirst = await cards.nth(0).boundingBox();
    const mobileSecond = await cards.nth(1).boundingBox();
    expect(Math.abs((mobileFirst?.x ?? 0) - (mobileSecond?.x ?? 0))).toBeLessThan(2);
    expect((mobileSecond?.y ?? 0)).toBeGreaterThan(mobileFirst?.y ?? 0);
    const overflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
    expect(overflow).toBeLessThanOrEqual(1);
  });
});

test.describe('known defects', () => {
  test('restart clears custom answers from the next run', async ({ page }) => {
    test.fail(true, 'Known defect: customAnswers is not reset by restart().');
    await startQuiz(page);
    await page.getByRole('textbox', { name: /Other idea/ }).fill('A public bath');
    await page.getByRole('button', { name: 'Next →' }).click();
    for (let step = 1; step < questions.length; step += 1) {
      await page.locator('#answers button.answer').first().click();
      await page.getByRole('button', { name: step === 7 ? 'See my city →' : 'Next →' }).click();
    }
    await page.getByRole('button', { name: 'Start over ↺' }).click();
    await page.getByRole('spinbutton', { name: 'YOUR AGE' }).fill('30');
    await page.getByRole('combobox', { name: 'YOUR FAVORITE ATMOSPHERE' }).selectOption('nature');
    await page.getByRole('button', { name: 'Start building →' }).click();

    await expect(page.getByRole('textbox', { name: /Other idea/ })).toHaveValue('');
    await expect(page.locator('.other-answer')).not.toHaveClass(/is-selected/);
  });

  test('renders custom ideas as text, never as HTML', async ({ page }) => {
    test.fail(true, 'Known defect: custom ideas are interpolated into result innerHTML without escaping.');
    await startQuiz(page);
    await page.getByRole('textbox', { name: /Other idea/ }).fill('<b>community bakery</b>');
    await page.getByRole('button', { name: 'Next →' }).click();
    for (let step = 1; step < questions.length; step += 1) {
      await page.locator('#answers button.answer').first().click();
      await page.getByRole('button', { name: step === 7 ? 'See my city →' : 'Next →' }).click();
    }

    await expect(page.locator('#city-traits b, .custom-scene-note b')).toHaveCount(0);
  });
});
