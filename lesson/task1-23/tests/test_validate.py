import pytest
from src.setting import ERROR_MESSAGE
from src.validate import BaseValidation, DepositValidation, WithdrawalValidation


class TestBaseValidation:
    def test_errors(self):
        base_validation = BaseValidation()
        assert base_validation._errors == []

    def test_is_valid(self):
        base_validation = BaseValidation()
        assert base_validation.is_valid


class TestDepositValidation:
    def test_validate(self):
        deposit_validation = DepositValidation(1000)
        assert deposit_validation.validate()
        assert deposit_validation.is_valid

    def test_validate_none(self):
        deposit_validation = DepositValidation(None)
        assert deposit_validation.validate() is False
        assert ERROR_MESSAGE["not_entry"] in deposit_validation.errors

    def test_validate_less_one(self):
        deposit_validation = DepositValidation(0)
        assert deposit_validation.validate() is False
        assert ERROR_MESSAGE["value_greater_than"] in deposit_validation.errors

        deposit_validation = DepositValidation(-1)
        assert deposit_validation.validate() is False
        assert ERROR_MESSAGE["value_greater_than"] in deposit_validation.errors


class TestWithdrawalValidation:
    def test_validate(self):
        withdraw_validation = WithdrawalValidation(1000, 500)
        assert withdraw_validation.validate()

    def test_validate_none(self):
        withdraw_validation = WithdrawalValidation(1000, None)
        assert withdraw_validation.validate() is False
        assert ERROR_MESSAGE["not_entry"] in withdraw_validation.errors

    def test_validate_less_one(self):
        withdraw_validation = WithdrawalValidation(1000, 0)
        assert withdraw_validation.validate() is False
        assert ERROR_MESSAGE["value_greater_than"] in withdraw_validation.errors

        withdraw_validation = WithdrawalValidation(1000, -1)
        assert withdraw_validation.validate() is False
        assert ERROR_MESSAGE["value_greater_than"] in withdraw_validation.errors

    def test_validate_less_blance(self):
        withdraw_validation = WithdrawalValidation(1000, 2000)
        assert withdraw_validation.validate() is False
        assert ERROR_MESSAGE["insufficient_balance"] in withdraw_validation.errors
