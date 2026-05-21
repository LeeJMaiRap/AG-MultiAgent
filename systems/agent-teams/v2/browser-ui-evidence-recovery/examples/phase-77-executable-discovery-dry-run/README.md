# Phase 77 — Executable Discovery Dry Run, No Install

## Purpose

Run read-only browser executable discovery using Track 4 allowed detection commands.

No install/download command was run.

## Commands Run

```bash
command -v chromium || command -v chromium-browser || true
command -v google-chrome || command -v google-chrome-stable || true
if test -x /root/.cache/ms-playwright/chromium_headless_shell-1217/chrome-headless-shell-linux64/chrome-headless-shell; then printf '%s\n' 'present executable'; else printf '%s\n' 'missing executable'; fi
node -e "try { require('playwright'); console.log('playwright package present') } catch (error) { console.log('playwright package missing') }"
node -e "try { require('puppeteer'); console.log('puppeteer package present') } catch (error) { console.log('puppeteer package missing') }"
```

Raw output:

```text
reports/discovery.log
```

## Results

```text
chromium executable: not found
chromium-browser executable: not found
google-chrome executable: not found
google-chrome-stable executable: not found
known Playwright Chromium executable: missing executable
playwright package: present
puppeteer package: missing
```

## Decision

```text
Real browser proof: Blocked
Screenshot/visual proof: Blocked
A11y scan proof: Blocked unless a separate approved a11y tool exists
Browser-like fallback: Allowed only as fallback
```

## Claim Boundary

Allowed:

```text
Playwright package present.
Browser executable discovery completed.
Browser-like fallback may be used if labelled fallback.
```

Forbidden:

```text
real browser tested
screenshot verified
visual regression passed
accessible/a11y verified
production browser proof
```

## Notes

Package presence is not browser proof. Executable launch and artifact evidence remain required.
