""" 
Guided project
"""

def increment_num(num):
    return num + 1

def test_increment_float():
    assert ld.increment_num(5.5) == 6.5 

def test_increment_neg_int():
    assert ld.increment_num(-5) == -4

def test_increment_neg_float():
    assert ld.increment_num(-5.2) == -4.2