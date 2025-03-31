import pytest
from src.validate import DepositValidation, WithdrawalValidation


def test_deposit_validation_valid():
    """有効な入金額がバリデーションを通過することをテスト"""
    validation = DepositValidation(1000)
    assert validation.validate() == True
    assert validation.is_valid == True
    assert len(validation.errors) == 0


def test_deposit_validation_negative():
    """負の入金額がバリデーションでエラーになることをテスト"""
    validation = DepositValidation(-100)
    assert validation.validate() == False
    assert validation.is_valid == False
    assert len(validation.errors) > 0


def test_withdrawal_validation_valid(bank_account):
    """有効な出金額がバリデーションを通過することをテスト"""
    validation = WithdrawalValidation(bank_account.my_account_balance, 1000)
    assert validation.validate() == True


def test_withdrawal_validation_exceed_balance(bank_account):
    """残高超過の出金額がバリデーションでエラーになることをテスト"""
    exceed_amount = bank_account.my_account_balance + 1000
    validation = WithdrawalValidation(bank_account.my_account_balance, exceed_amount)
    assert validation.validate() == False
    assert "残高不足です" in validation.errors[0]
