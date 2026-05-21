# Toolchain Preflight Matrix

## Purpose

Define how Agent-Teams checks common toolchains before claiming Local, Integration, or Production verification.

## Rules

```text
Check before use.
Do not install silently.
If missing, use approved fallback or mark Needs Approval / Blocked.
Do not claim evidence level higher than available toolchain supports.
Record command, output, and claim boundary.
```

## Matrix

| Toolchain | Detect Command | Minimum Evidence | Install Approval Requirement | Fallback | Claim Boundary If Missing |
|---|---|---|---|---|---|
| Node.js | `node --version` | version output | install needs approval | docs-only or alternate runtime | no Node execution/build/test claim |
| npm | `npm --version` | version output | install needs approval | no-install scripts only | no npm install/test/build claim |
| pnpm | `pnpm --version` | version output | install needs approval | npm if project already uses npm and approved | no pnpm claim |
| yarn | `yarn --version` | version output | install needs approval | npm if project already uses npm and approved | no yarn claim |
| TypeScript compiler | `npx tsc --version` or `tsc --version` | version output | `npx` package download/install needs approval if not already present | `node --check` for JS only | no TypeScript compile claim |
| Python | `python3 --version` | version output | install needs approval | docs-only | no Python execution/test claim |
| pip | `python3 -m pip --version` | version output | install needs approval | stdlib-only Python | no pip dependency claim |
| Python venv | `python3 -m venv --help` | command succeeds | install needs approval | system Python without deps if acceptable | no isolated env claim |
| Browser executable | browser-specific launch command | launch succeeds | browser binary install needs explicit approval | browser-like fallback, labelled | no real browser/screenshot/a11y/visual claim |
| Playwright | `node -e "require('playwright')"` and browser launch | package import + executable launch | `npm install playwright` / `npx playwright install` needs explicit approval | fetch/DOM-like fallback, labelled | package present != browser proof |
| Puppeteer | `node -e "require('puppeteer')"` and browser launch | package import + executable launch | `npm install puppeteer` needs explicit approval | fetch/DOM-like fallback, labelled | package present != browser proof |
| ESLint | `npx eslint --version` or local binary | version output | install/download needs approval if absent | syntax/build checks | no lint claim |
| Prettier | `npx prettier --version` or local binary | version output | install/download needs approval if absent | manual formatting review | no formatter claim |
| Docker | `docker --version` | version output | install/use may need approval; daemon access high risk | local commands | no container build/run claim |
| kubectl | `kubectl version --client` | client version | install/use requires explicit approval; cluster writes critical | no deploy | no Kubernetes/deploy claim |
| Cloud CLI | `<cli> --version` | version output | install/use requires explicit approval; credentials critical | no cloud action | no cloud/deploy claim |
| System packages | `dpkg -s <pkg>` or tool command | package/tool exists | `apt install` / `apt-get install` requires explicit approval | fallback if approved | no system-tool claim |

## Preflight Record Template

```text
Toolchain: <name>
Detect command: <command>
Result: Present | Missing | Error | Needs Approval | Blocked
Output/log: <path-or-inline>
Install needed: Yes | No
Approval packet: <path-or-none>
Fallback: <none-or-approved-fallback>
Claim boundary: <boundary>
```

## Browser-Specific Rule

```text
Browser package installed is not browser proof.
Real browser proof requires executable launch evidence.
Screenshot/a11y/visual claims require captured evidence.
```

## Dependency-Specific Rule

```text
Package manager availability is not install approval.
Every new install/download still needs dependency approval packet and PM/user approval per risk level.
```
