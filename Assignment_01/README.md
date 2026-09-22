# Assignment 1 – Student Support Rule Engine

A command-line Python program that collects a student's attendance,
assignment average, and missed submission count, then classifies the
student into a support-priority category and prints an advisory message.

## Support-priority rules

1. **High priority** — attendance < 60 **OR** missed submissions >= 4
2. **Moderate priority** — attendance < 75 **OR** assignment average < 60
   **OR** missed submissions >= 2
3. **Routine monitoring** — none of the above conditions are true

## Files

- `support_engine.py` — main program with input validation, rule
  classification, advisory messages, and the CLI entry point.
- `test_support_engine.py` — assertion-based tests covering normal and
  boundary cases for `classify_support()` and `format_message()`.
- `README.md` — this document.

## Run commands

From the repository root:

```bash
uv run python Assignment_01/support_engine.py
uv run python Assignment_01/test_support_engine.py