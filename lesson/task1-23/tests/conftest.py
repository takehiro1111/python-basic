# conftest.py
import os
import sys

# プロジェクトのルートディレクトリをパスに追加
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from src.account import AccountManager, BankAccount
from src.atm import ATM


@pytest.fixture
def account_manager():
    """AccountManagerのインスタンスを提供するフィクスチャ"""
    return AccountManager()


@pytest.fixture
def bank_account():
    """テスト用の残高10000円の口座を提供するフィクスチャ"""
    return BankAccount(10000)


@pytest.fixture
def atm(bank_account, account_manager):
    """テスト用のATMインスタンスを提供するフィクスチャ"""
    return ATM(bank_account, account_manager)
