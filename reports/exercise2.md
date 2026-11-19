# Bug reports for exercise2.py

Line: 8
Problem: is_valid_password fails for passwords with exactly 8 characters and no digits, but the docstring says "at least 8 characters and at least one digit". The condition "len(password) >= 8" is correct, but "any(c.isdigit() for c in password)" is not sufficient when the password has exactly 8 characters and no digits — it will return False, which is correct, but the docstring requires at least one digit, so the function must return False in such cases. However, the issue is not in the logic — the function is correct. There is no bug.  
Fix: (no fix needed)

Line: 12
Problem: clamp returns max(low, min(x, high)), which is correct for clamping x to the range [low, high]. The docstring says "x, limited to the range from low to high", and this function correctly ensures x is at least low and at most high. There is no bug.  
Fix: (no fix needed)
