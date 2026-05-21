# Browser Install Risk Notes

## Risks

### Network / Supply Chain

Browser binary download uses external sources. Risk includes changed upstream artifacts, transient failures, rate limits, and supply-chain trust.

### Disk Usage

Browser binaries can be large. Cache paths such as `~/.cache/ms-playwright/**` may grow across versions.

### Package File Changes

`npm install playwright` or `npm install puppeteer` can alter dependency tree and lockfiles. This changes project state and should be committed only if intended.

### System Package Changes

`apt install chromium` or `apt-get install chromium` changes system-level packages and may require elevated privileges. Rollback can affect other tools.

### CI / Local Mismatch

Local browser install does not prove CI or production browser readiness. CI needs its own preflight and install policy.

### Evidence Overclaim

After install, real browser claim still requires launch evidence. Accessibility or visual claims require dedicated checks and logs, not only screenshot existence.

## Safer Defaults

```text
Prefer Playwright browser cache install over apt/system install when project already uses Playwright.
Prefer one exact command approval at a time.
Prefer local-only proof before CI/prod changes.
Prefer browser-like fallback if user does not need screenshot/runtime proof.
```

## Stop Conditions

Stop and ask user if:

```text
command needs elevated privileges
command changes system packages
command changes package.json or lockfile unexpectedly
install wants cloud/browser service account
download source is unclear
real secrets are requested
```
