import pytest
from src.account import AccountManager


def test_account_info(account_manager):
    """account_infoメソッドが適切な形式のデータを返すかテスト"""
    users = account_manager.account_info()
    assert isinstance(users, list)
    assert all(isinstance(user, dict) for user in users)
    assert all("id" in user and "pin" in user for user in users)


def test_auth_user_id_valid(account_manager):
    """有効なユーザーIDで認証できることをテスト"""
    assert account_manager.auth_user_id("takehiro1111") == True


def test_auth_user_id_invalid(account_manager):
    """無効なユーザーIDで認証が失敗することをテスト"""
    assert account_manager.auth_user_id("nonexistent") == False


def test_auth_user_pin_valid(account_manager):
    """有効な暗証番号で認証できることをテスト"""
    # まずユーザーIDを認証してPINを設定
    account_manager.auth_user_id("takehiro1111")
    assert account_manager.auth_user_pin("1234") == True


def test_auth_user_pin_invalid(account_manager):
    """無効な暗証番号で認証が失敗することをテスト"""
    account_manager.auth_user_id("takehiro1111")
    assert account_manager.auth_user_pin("9999") == False


def test_auth_user_pin_non_numeric(account_manager):
    """数値でない暗証番号で認証が失敗することをテスト"""
    account_manager.auth_user_id("takehiro1111")
    assert account_manager.auth_user_pin("abcd") == False
