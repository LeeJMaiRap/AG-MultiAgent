# Browser Evidence Checklist

## Real Browser Proof Checklist

- [ ] Browser package exists.
- [ ] Browser executable exists.
- [ ] Headless launch succeeds.
- [ ] Local server start command documented.
- [ ] Target route documented.
- [ ] Screenshot path documented.
- [ ] Screenshot produced.
- [ ] Browser test log saved.
- [ ] Assertions cover visible text and key UI state.
- [ ] Cleanup closes browser and server.
- [ ] Evidence claims match proof.

## Browser-Like Fallback Checklist

- [ ] Missing browser executable documented.
- [ ] No install/download occurred.
- [ ] Local HTTP route tested.
- [ ] HTML structure checked.
- [ ] Visible text approximated or extracted.
- [ ] Escaping/security-relevant rendering checked if in scope.
- [ ] Claims limited to browser-like proof.
- [ ] Missing screenshot/real browser limitations stated.

## Stop Gate

Stop and ask PM/user if task requires:

```text
- real browser screenshot
- JavaScript runtime behavior
- visual regression
- browser-specific CSS/layout proof
- accessibility scan through browser engine
```

and browser executable cannot launch.
