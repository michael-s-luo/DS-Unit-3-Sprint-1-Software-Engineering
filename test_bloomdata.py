""" 
Date: 2022/11/16
Guided Project for Pytest

Basic, simple testing using pytest for bloomdata packagge.

How to run pytest in terminal:
pytest test_bloomdata.py --verbose
"""

import pytest
from bloomdata import bloomdata as ld
from bloomdata import helper_functions as hf
import pandas as pd
import numpy as np


def test_increment_int():
    """Tests incrementation with integer"""
    assert ld.increment_num(3) == 4
    assert ld.increment_num(100) == 101


def test_increment_float():
    """Tests incrementation with float"""
    assert ld.increment_num(5.5) == 6.5


def test_increment_neg_int():
    """Tests incrementation with negative integer"""
    assert ld.increment_num(-5) == -4


def test_increment_neg_float():
    """Tests incrementation with negative float"""
    assert ld.increment_num(-5.2) == -4.2


def test_random_float_type():
    """Tests return type of random_float in helper_functions.py"""
    assert isinstance(hf.random_float(float("-inf"), float("+inf")), float)


@pytest.fixture
def test_df():
    """Test 3x3 DataFrame with no null values

    Returns
    -------
    pandas DataFrame
    """
    return pd.DataFrame([[1, 2, 3], [2, 3, 4], [4, 5, 6]])


@pytest.fixture
def test_df_nulls():
    """Test 3x3 DataFrame with null values

    Returns
    -------
    pandas DataFrame
    """
    return pd.DataFrame([[np.NaN, 2, 3], [np.NaN, 3, 4], [4, 5, 6]])


def test_null_count_zero(test_df):
    """Test: null_count in helper_functions.py
    Should return 0 when input DataFrame has 0 null values

    Parameters
    ----------
    test_df : pandas DataFrame
    """
    assert hf.null_count(test_df) == 0


def test_null_count_nonzero(test_df_nulls):
    """test: null_count in helper_functions.py
    Should return non-zero integer when input DataFrame has null values

    Parameters
    ----------
    test_df_nulls : pandas DataFrame
    """
    assert hf.null_count(test_df_nulls) > 0
