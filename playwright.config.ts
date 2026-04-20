import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  timeout: 30_000,
  use: {
    baseURL: 'http://localhost:4321',
    trace: 'on-first-retry',
  },
  webServer: {
    command: 'npm run dev',
    url: 'http://localhost:4321',
    timeout: 60_000,
    reuseExistingServer: !process.env.CI,
  },
  projects: [
    { name: 'chromium', use: devices['Desktop Chrome'] },
  ],
});
