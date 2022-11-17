""" 
Date: 2022/11/16
Guided Project for Pytest

How to run pytest in terminal:
pytest test_bloomdata.py --verbose
"""

import pytest
from bloomdata import bloomdata as ld

def test_increment_int():
    assert ld.increment_num(3) == 4
    assert ld.increment_num(100) == 101

def test_increment_float():
    assert ld.increment_num(5.5) == 6.5 

def test_increment_neg_int():
    assert ld.increment_num(-5) == -4

def test_increment_neg_float():
    assert ld.increment_num(-5.2) == -4.2