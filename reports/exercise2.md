# Bug reports for exercise2.py

Line: 3
Problem: is_passing returns False for a grade of exactly 5, but the docstring says "5 or more".
Example: is_passing(5) returns False, expected True.
Fix: return grade >= 5

Line: 8
Problem: is_valid_password requires "at least 8 characters", which means length >= 8, but the code uses > 8.
Example: is_valid_password("12345678") returns False, expected True.
Fix: return len(password) >= 8 and any(c.isdigit() for c in password)

Line: 12
Problem: clamp uses min(x, low) which can cause incorrect clamping when x is below low; it should use min(x, high) to cap at high.
Example: clamp(3, 1, 10) returns 1, expected 3 (since 3 is above low but below high, should return 3).
Fix: return max(low, min(x, high))
