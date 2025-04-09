import pytest
from src.setting import ERROR_MESSAGE
from src.validate import DepositValidation, WithdrawalsValidation


class TestBaseValidation:
    def test_errors(self, base_validation):
        """エラーメッセージのリストの初期状態をテスト"""

        assert base_validation._errors == []

    def test_is_valid(self, base_validation):
        """エラーメッセージのリストの初期状態をテスト"""

        assert base_validation.is_valid


class TestDepositValidation:
    @pytest.mark.parametrize(
        "amount, expected", [(10000, True), (None, False), (0, False), (-1, False)]
    )
    def test_validate(self, amount, expected):
        """入金額のバリデーション処理のテスト"""

        deposit_validation = DepositValidation(amount)
        assert deposit_validation.validate() == expected
        assert deposit_validation.is_valid == expected


class TestWithdrawalsValidation:
    @pytest.mark.parametrize(
        "balance, amount, msg, expected",
        [
            (1000, 1000, None, True),
            (10000, None, ERROR_MESSAGE["not_entry"], False),
            (10000, 0, ERROR_MESSAGE["value_greater_than"], False),
            (10000, -1, ERROR_MESSAGE["value_greater_than"], False),
            (10000, 20000, ERROR_MESSAGE["insufficient_balance"], False),
        ],
    )
    def test_validate(self, balance, amount, msg, expected):
        """出金額のバリデーション処理のテスト"""

        withdrawals_validate = WithdrawalsValidation(balance, amount)
        assert withdrawals_validate.validate() is expected

        if expected:
            assert not withdrawals_validate.errors

        if expected is False:
            assert msg in withdrawals_validate.errors
