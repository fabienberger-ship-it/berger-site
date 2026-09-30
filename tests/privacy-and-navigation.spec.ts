import { test, expect } from '@playwright/test';

test('la visite ne charge aucun service tiers ni traceur facultatif', async ({ page, context, baseURL }) => {
  const thirdPartyRequests: string[] = [];
  const origin = new URL(baseURL!).origin;
  page.on('request', request => {
    if (new URL(request.url()).origin !== origin) thirdPartyRequests.push(request.url());
  });
  await page.goto('/');
  await page.locator('.site-footer a[href="/cookies"]').click();
  await expect(page.getByRole('heading', { name: 'Cookies et traceurs', exact: true })).toBeVisible();
  await expect(page.getByRole('dialog')).toHaveCount(0);
  expect(thirdPartyRequests).toEqual([]);
  expect(await context.cookies()).toEqual([]);
});

test('une ancienne préférence est effacée sans toucher aux autres données locales', async ({ page }) => {
  await page.addInitScript(() => {
    localStorage.setItem('cookie-consent', JSON.stringify({ analytics: true, timestamp: Date.now() }));
    localStorage.setItem('preference-independante', 'conserver');
  });
  await page.goto('/');
  await expect.poll(() => page.evaluate(() => localStorage.getItem('cookie-consent'))).toBeNull();
  expect(await page.evaluate(() => localStorage.getItem('preference-independante'))).toBe('conserver');
});

test('sur mobile, le menu permet de rejoindre les associés et se referme', async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto('/');
  await page.locator('.mobile-nav summary').click();
  await page.getByRole('navigation', { name: 'Navigation principale mobile' }).getByRole('link', { name: 'Les associés' }).click();
  await expect(page).toHaveURL(/#associes$/);
  await expect(page.locator('.mobile-nav')).not.toHaveAttribute('open', '');
  await expect(page.locator('#associes').getByRole('link', { name: 'Écrire à Marine Gorin' })).toHaveAttribute('href', 'mailto:marine.gorin@berger-associes.fr');
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth)).toBe(true);
});

test('le menu mobile se ferme au clavier et rend le focus au bouton', async ({ page }) => {
  await page.setViewportSize({ width: 320, height: 740 });
  await page.goto('/');
  const summary = page.locator('.mobile-nav summary');
  await summary.focus();
  await page.keyboard.press('Enter');
  await expect(page.locator('.mobile-nav')).toHaveAttribute('open', '');
  await page.keyboard.press('Escape');
  await expect(page.locator('.mobile-nav')).not.toHaveAttribute('open', '');
  await expect(summary).toBeFocused();
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth)).toBe(true);
});
