import { test, expect } from '@playwright/test';

test.describe('Cookie banner', () => {
  test.beforeEach(async ({ page, context }) => {
    await context.clearCookies();
    await page.goto('/');
  });

  test('affiche le bandeau au premier visiteur', async ({ page }) => {
    await expect(page.locator('[data-cookie-banner]')).toBeVisible();
    await expect(page.locator('[data-cookie-accept-all]')).toBeVisible();
    await expect(page.locator('[data-cookie-reject-all]')).toBeVisible();
    await expect(page.locator('[data-cookie-customize]')).toBeVisible();
  });

  test('cache le bandeau après "Tout accepter"', async ({ page }) => {
    await page.click('[data-cookie-accept-all]');
    await expect(page.locator('[data-cookie-banner]')).toBeHidden();
    const stored = await page.evaluate(() => localStorage.getItem('cookie-consent'));
    expect(stored).toContain('"analytics":true');
  });

  test('cache le bandeau après "Tout refuser" (sans analytics)', async ({ page }) => {
    await page.click('[data-cookie-reject-all]');
    await expect(page.locator('[data-cookie-banner]')).toBeHidden();
    const stored = await page.evaluate(() => localStorage.getItem('cookie-consent'));
    expect(stored).toContain('"analytics":false');
  });

  test('bouton "Gérer préférences" sur /cookies rouvre la modale', async ({ page }) => {
    await page.click('[data-cookie-reject-all]');
    await page.goto('/cookies');
    await page.click('#open-cookie-preferences');
    await expect(page.locator('[data-cookie-banner]')).toBeVisible();
  });
});
