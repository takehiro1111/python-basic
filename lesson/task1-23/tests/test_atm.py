import io

import pytest
from src.account import AccountManager, BankAccount
from src.atm import ATM


class TestATM:
    @pytest.fixture
    def atm(self):
        return ATM(BankAccount(10000), AccountManager())

    @pytest.fixture
    def account_manager(self):
        return AccountManager()

    # メニュー選択
    def test_guide_menu(self, atm, monkeypatch):
        """メニュー選択のテスト"""
        # 暗証番号認証を成功させるためのモック
        monkeypatch.setattr(atm, "execute_auth_user_pin", lambda attempt_check=3: True)

        monkeypatch.setattr("builtins.input", lambda _: "1")
        monkeypatch.setattr("builtins.input", lambda _: "2")
        monkeypatch.setattr("builtins.input", lambda _: "3")

        assert atm.guide_menu("1")
        assert atm.guide_menu("2")
        assert atm.guide_menu("3") is None

    # 入金処理
    def test_deposit(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "1")

    # # 出金処理
    # def test_withdraw(self):

    # エラーメッセージの取得
    def test_show_error_msg(self, atm):
        err_msg = atm.show_error_msg(["test-error"])
        assert err_msg is None

    # ユーザーIDの認証
    def test_execute_auth_user_id_true(self, atm, monkeypatch):
        monkeypatch.setattr("sys.stdin", io.StringIO("takehiro1111\nMichael"))

        assert atm.execute_auth_user_id()

    def test_execute_auth_user_id_false(self, atm, monkeypatch):
        monkeypatch.setattr(
            "sys.stdin", io.StringIO("fail-test\nfail-test2\nfail-test3\nfail-test4")
        )

        assert atm.execute_auth_user_id() is False

    # 暗証番号の認証
    def test_execute_auth_user_pin_true(self, atm, monkeypatch):
        monkeypatch.setattr(
            "sys.stdin", io.StringIO(f"takehiro1111\n1234\nMichael\n5678")
        )

        assert atm.execute_auth_user_id()
        assert atm.execute_auth_user_pin()

    def test_execute_auth_user_pin_false(self, atm, monkeypatch):
        monkeypatch.setattr(
            "sys.stdin",
            io.StringIO(
                f"takehiro1111\nfaild-pin1\nfaild-pin2\nfaild-pin3\nfaild-pin4"
            ),
        )

        assert atm.execute_auth_user_id()
        assert atm.execute_auth_user_pin() is False
