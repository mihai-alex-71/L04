# Bug reports for exercise1.py

Line: 3
Problem: is_even claims to be true for even numbers but uses == 1, which is true only for odd numbers. The docstring says it should be true for even numbers.
Example: is_even(4) returns False, expected True.
Fix: return n % 2 == 0

Line: 8
Problem: rectangle_area returns the sum of width and height, but the docstring says it should return the area, which is width times height.
Example: rectangle_area(3, 4) returns 7, expected 12.
Fix: return width * height

Line: 13
Problem: double claims to return twice the number n but adds 2 instead of multiplying by 2.
Example: double(5) returns 7, expected 10.
Fix: return n * 2
