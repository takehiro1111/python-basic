import pytest
from src.account import AccountManager, BankAccount


class TestAccountManager:
    @pytest.fixture
    def account_manager(self):
        return AccountManager()

    def test_account_info(self, account_manager):
        bank_user_list: list[dict] = [
            {"id": "takehiro1111", "pin": 1234},
            {"id": "Michael", "pin": 5678},
        ]
        assert account_manager.account_info() == bank_user_list

    def test_auth_user_id(self, account_manager):
        """ユーザーIDが一致するかテスト"""
        assert account_manager.auth_user_id("takehiro1111")
        assert account_manager.auth_user_id("Michael")

        # テストコードが機能するかダミー用の設定
        assert account_manager.auth_user_id("test-user") is False

    def test_auth_user_pin(self, account_manager):
        """ユーザーIDと暗証番号が一致するかテスト"""
        account_manager.auth_user_id("takehiro1111")
        assert account_manager.auth_user_pin(1234)

        account_manager.auth_user_id("Michael")
        assert account_manager.auth_user_pin(5678)


class TestBankAccount:
    @pytest.fixture
    def bank_account(self):
        return BankAccount(10000)

    def test_initial_balance(self, bank_account):
        """初期残高が正しく設定されるかテスト"""
        assert bank_account.my_account_balance == 10000

    def test_set_balance(self, bank_account):
        """残高を更新できるかテスト"""
        bank_account.my_account_balance = 20000
        assert bank_account.my_account_balance == 20000
        assert bank_account._balance == 20000
