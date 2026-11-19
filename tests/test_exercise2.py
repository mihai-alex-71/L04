import os
import sqlite3
import subprocess

import pytest

import exercise2
from exercise2 import *


# bug report 1
def test_r1_is_passing_grade_5():
    assert is_passing(5) == True


# bug report 2
def test_r2_clamp_with_valid_value():
    assert clamp(3, 1, 10) == 3
