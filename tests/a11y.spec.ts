import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

const routes = [
  { path: '/', label: 'Accueil' },
  { path: '/mentions-legales', label: 'Mentions légales' },
  { path: '/confidentialite', label: 'Confidentialité' },
  { path: '/cookies', label: 'Cookies' },
  { path: '/page-qui-n-existe-pas', label: '404' },
];

for (const { path, label } of routes) {
  test(`a11y: ${label} (${path}) — zéro violation WCAG 2.1 AA`, async ({ page }) => {
    await page.goto(path);
    const results = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
      .analyze();

    if (results.violations.length > 0) {
      console.log(JSON.stringify(results.violations, null, 2));
    }
    expect(results.violations).toHaveLength(0);
  });
}
