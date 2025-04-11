import io

import pytest


class TestATM:
    @pytest.mark.parametrize(
        "menu_num, input_amount, expected",
        [
            ("1", "1000", 11000),
            ("2", "1000", 9000),
            ("3", "1000", None),
            ("invalid", "1000", None),
        ],
    )
    def test_guide_menu(
        self, authenticated_atm, monkeypatch, menu_num, input_amount, expected
    ):
        """メニュー選択のテスト"""
        monkeypatch.setattr("builtins.input", lambda _: input_amount)
        result = authenticated_atm.guide_menu(menu_num)
        assert (
            result == expected
        ), f"test_guide_menu should be menu_num: {menu_num} / input_amount: {input_amount}  expected: {expected}"

    @pytest.mark.parametrize(
        "amount, expected",
        [("1000", 11000), ("test-str", None), ("0", None), ("-1", None)],
    )
    def test_deposit(self, authenticated_atm, monkeypatch, amount, expected):
        """入金処理のテスト"""

        monkeypatch.setattr("builtins.input", lambda _: amount)

        result = authenticated_atm.deposit(amount)
        assert (
            result == expected
        ), f"test_deposit should be amount: {amount} / expected: {expected}"

    @pytest.mark.parametrize(
        "amount, expected",
        [("10000", 0), ("200000", None), ("test-str", None), ("0", None), ("-1", None)],
    )
    def test_withdrawals(self, authenticated_atm, monkeypatch, amount, expected):
        """出金処理のテスト"""

        monkeypatch.setattr("builtins.input", lambda _: amount)

        result = authenticated_atm.withdrawals(amount)
        assert (
            result == expected
        ), f"test_withdrawals should be amount: {amount} / expected: {expected}"

    def test_show_error_msg(self, atm):
        """エラーメッセージ取得のテスト"""

        err_msg = atm.show_error_msg(["test-error"])
        assert err_msg is None, f"test_show_error_msg should be {None}"

    def test_execute_auth_user_id_true(self, atm, monkeypatch):
        """ユーザーIDの認証テスト(成功する場合)"""

        monkeypatch.setattr("sys.stdin", io.StringIO("takehiro1111\nMichael"))

        assert (
            atm.execute_auth_user_id() is True
        ), f"test_execute_auth_user_id_true should be {True}"

    def test_execute_auth_user_id_false(self, atm, monkeypatch):
        """ユーザーIDの認証テスト(失敗する場合)"""

        monkeypatch.setattr(
            "sys.stdin", io.StringIO("fail-test\nfail-test2\nfail-test3\nfail-test4")
        )

        assert (
            atm.execute_auth_user_id() is False
        ), f"test_execute_auth_user_id_false should be {False}"

    def test_execute_auth_user_pin_true(self, atm, monkeypatch):
        """暗証番号の認証のテスト(成功する場合)"""

        monkeypatch.setattr(
            "sys.stdin", io.StringIO(f"takehiro1111\n1234\nMichael\n5678")
        )

        assert (
            atm.execute_auth_user_id() is True
        ), f"test_execute_auth_user_pin_true: execute_auth_user_id should be {True}"
        assert (
            atm.execute_auth_user_pin() is True
        ), f"test_execute_auth_user_pin_true: execute_auth_user_pin should be {True}"

    def test_execute_auth_user_pin_false(self, atm, monkeypatch):
        """暗証番号の認証のテスト(失敗する場合)"""

        monkeypatch.setattr(
            "sys.stdin",
            io.StringIO(
                f"takehiro1111\nfaild-pin1\nfaild-pin2\nfaild-pin3\nfaild-pin4"
            ),
        )

        assert (
            atm.execute_auth_user_id() is True
        ), f"test_execute_auth_user_pin_false: execute_auth_user_id should be {True}"
        assert (
            atm.execute_auth_user_pin() is False
        ), f"test_execute_auth_user_pin_false: execute_auth_user_pin should be {False}"
