import pytest


class TestAccountManager:
    def test_account_info(self, account_manager):
        """IDと暗証番号のデータが正しいかテスト"""

        bank_user_list: list[dict] = [
            {"id": "takehiro1111", "pin": 1234},
            {"id": "Michael", "pin": 5678},
        ]
        assert (
            account_manager.account_info() == bank_user_list
        ), f"test_account_info should be {bank_user_list}"

    @pytest.mark.parametrize(
        "user_id, expected",
        [
            ("takehiro1111", True),
            ("Michael", True),
            ("test-dummy-user", False),
        ],
    )
    def test_auth_user_id(self, account_manager, user_id, expected):
        """ユーザーIDが一致するかテスト"""
        assert (
            account_manager.auth_user_id(user_id) == expected
        ), f"test_auth_user_id should be {expected}"

    @pytest.mark.parametrize(
        "user_id, user_pin, expected",
        [
            ("takehiro1111", 1234, True),
            ("Michael", 5678, True),
            ("test-dummy-user", 7890, False),
        ],
    )
    def test_auth_user_pin(self, account_manager, user_id, user_pin, expected):
        """ユーザーIDと暗証番号が一致するかテスト"""
        account_manager.auth_user_id(user_id)
        assert (
            account_manager.auth_user_pin(user_pin) == expected
        ), f"test_auth_user_pin: {user_id} with PIN {user_pin} should be {expected}"


class TestBankAccount:
    def test_initial_balance(self, bank_account):
        """初期残高が正しく設定されるかテスト"""
        assert bank_account._balance == 10000, f"test_initial_balance should be {10000}"

    def test_set_balance(self, bank_account):
        """残高を更新できるかテスト"""
        bank_account.my_account_balance = 20000
        assert bank_account._balance == 20000, f"test_set_balance should be {20000}"
