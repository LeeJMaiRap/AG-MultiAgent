# Browser Proof Fallback vs Blocked Rules

## Decision Matrix

| Required Evidence | Browser Executable | Install Approved | Result |
| --- | --- | --- | --- |
| Real browser screenshot | available + launches | not needed | Proceed |
| Real browser screenshot | missing | yes | Run approved install command, then retry preflight |
| Real browser screenshot | missing | no | Blocked |
| Browser-like HTML proof accepted | missing | no | Use fallback and mark limitation |
| JS DOM runtime proof required | missing | no | Blocked |
| Accessibility scan required | missing | no | Blocked or use static partial check only if accepted |

## Evidence Level Mapping

```text
Real browser launch + screenshot -> Integration browser evidence
Browser-like fetch + HTML assertions -> Integration HTTP/UI evidence, not real browser evidence
Static template inspection -> Local/Paper evidence depending on context
```

## Required Report Language

When fallback is used, report must include:

```text
Status: PASS with fallback
Missing tool: <exact tool/executable>
Fallback used: <method>
Evidence level: <what it proves>
Claims not made: <browser/screenshot/runtime/a11y/production claims>
```

When blocked, report must include:

```text
Status: Blocked / Needs Review
Missing tool: <exact tool/executable>
Required approval or install: <exact command proposal>
Why fallback is insufficient: <reason>
```
