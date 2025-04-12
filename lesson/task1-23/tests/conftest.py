import pytest
from src.account import AccountManager, BankAccount
from src.atm import ATM
from src.validate import BaseValidation


# Account
@pytest.fixture
def account_manager():
    return AccountManager()


@pytest.fixture
def bank_account():
    return BankAccount(10000)


# ATM
@pytest.fixture
def atm(bank_account, account_manager):
    return ATM(bank_account, account_manager)


@pytest.fixture
def authenticated_atm(atm, monkeypatch):
    monkeypatch.setattr(atm, "execute_auth_user_id", lambda: True)
    monkeypatch.setattr(atm, "execute_auth_user_pin", lambda attempt_check=3: True)
    return atm


# Validate
@pytest.fixture
def base_validation():
    return BaseValidation()
