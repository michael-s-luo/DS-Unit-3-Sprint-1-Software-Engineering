""" 
3.1.4 Lecture & Guided Project
Date: 2022/11/16

Usage of pytest and pytest fixtures & decorators
"""
from bloomdata.wallet import Wallet
import pytest


@pytest.fixture()
def empty_wallet():
    '''returns a wallet instance with a zero balance'''
    wallet = Wallet()
    return wallet

@pytest.fixture
def wallet_20():
    '''returns a wallet of balance: 20'''
    return Wallet(20)

def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0

def test_setting_initial_amount(wallet_20):
    assert wallet_20.balance == 20