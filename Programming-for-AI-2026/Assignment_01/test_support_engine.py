"""Assertion tests for the Student Support Rule Engine."""

from support_engine import classify_support, format_message

# --- classify_support boundary and normal cases ---
assert classify_support(59.99, 0, 0) == "High priority"       # below attendance boundary
assert classify_support(60, 90, 4) == "High priority"         # high missed boundary
assert classify_support(74.99, 0, 0) == "Moderate priority"   # below attendance boundary
assert classify_support(75, 59.9, 0) == "Moderate priority"   # below average boundary
assert classify_support(90, 90, 2) == "Moderate priority"     # moderate missed boundary
assert classify_support(75, 60, 1) == "Routine monitoring"    # minimum routine values
assert classify_support(100, 100, 0) == "Routine monitoring"  # maximum valid values

# --- format_message checks ---
assert format_message("High priority") == "Immediate academic support is recommended."
assert format_message("Moderate priority") == "Monitor progress and provide targeted guidance."
assert format_message("Routine monitoring") == "Continue routine monitoring."

print("All tests passed.")