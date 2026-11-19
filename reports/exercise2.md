# Bug reports for exercise2.py

Line: 3
Problem: is_passing claims "True if the grade is 5 or more", but uses > 5, which excludes 5.
Example: is_passing(5) returns False, expected True.
Fix: return grade >= 5

Line: 12
Problem: clamp uses min(x, low) which incorrectly limits x to low, but the docstring says "limited to the range from low to high".
Example: clamp(3, 1, 10) returns 1, expected 3.
Fix: return max(low, min(x, high))
