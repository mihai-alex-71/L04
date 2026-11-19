import os
import sqlite3
import subprocess

import pytest

import exercise2
from exercise2 import *


# bug report 1
def test_r1_is_valid_password_no_digits():
    assert is_valid_password("abcdefgh") == False


# bug report 2
def test_r2_clamp_with_edge_values():
    assert clamp(3, 1, 5) == 3
    assert clamp(7, 1, 5) == 5
    assert clamp(1, 1, 5) == 1
    assert clamp(5, 1, 5) == 5
