from unittest.mock import patch

import pytest
from src.atm import ATM
from src.setting import GUIDE_NUMBER


# 入力をモックするためのヘルパー関数
def mock_input(inputs):
    return lambda _: inputs.pop(0) if inputs else ""


def test_deposit_successful(atm, monkeypatch, capsys):
    """入金処理が成功するケースをテスト"""
    # auth_user_pinメソッドをモックして常に成功するようにする
    with patch.object(atm.account_manager, "auth_user_pin", return_value=True):
        # 入力をシミュレート
        monkeypatch.setattr("builtins.input", lambda _: "1000")

        # 処理前の残高を記録
        initial_balance = atm.bank_account.my_account_balance

        # 入金処理を実行
        result = atm.deposit("1000")

        # 残高が正しく増加していることを確認
        assert result == initial_balance + 1000

        # 正しいメッセージが出力されたか確認
        captured = capsys.readouterr()
        assert "1,000円を入金しました" in captured.out


def test_withdrawal_successful(atm, monkeypatch, capsys):
    """出金処理が成功するケースをテスト"""
    # auth_user_pinメソッドをモックして常に成功するようにする
    with patch.object(atm.account_manager, "auth_user_pin", return_value=True):
        # 入力をシミュレート
        monkeypatch.setattr("builtins.input", lambda _: "1000")

        # 処理前の残高を記録
        initial_balance = atm.bank_account.my_account_balance

        # 出金処理を実行
        result = atm.withdrawal("1000")

        # 残高が正しく減少していることを確認
        assert result == initial_balance - 1000

        # 正しいメッセージが出力されたか確認
        captured = capsys.readouterr()
        assert "1,000円を引き出しました" in captured.out


def test_guide_menu_deposit(atm, monkeypatch):
    """メニューから入金が選択されたときのテスト"""
    # 連続した入力をシミュレート (メニュー選択「1」→ 入金額「500」)
    inputs = ["500"]
    monkeypatch.setattr("builtins.input", mock_input(inputs))

    # depositメソッドをモックして戻り値を固定
    with patch.object(atm, "deposit", return_value=10500):
        result = atm.guide_menu(str(GUIDE_NUMBER["deposit"]))
        assert result == 10500


@pytest.mark.parametrize(
    "pin_input,expected_result", [("1234", True), ("9999", False), ("abcd", False)]
)
def test_execute_auth_user_pin_parametrized(
    atm, monkeypatch, pin_input, expected_result
):
    """暗証番号認証のパラメータ化テスト"""
    # auth_user_pinの戻り値をパラメータに合わせて設定
    with patch.object(
        atm.account_manager, "auth_user_pin", return_value=expected_result
    ):
        # 入力をシミュレート
        monkeypatch.setattr("builtins.input", lambda _: pin_input)

        # テスト実行と検証
        assert atm.execute_auth_user_pin(1) == expected_result
