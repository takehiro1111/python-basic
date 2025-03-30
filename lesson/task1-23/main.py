"""
81. ATMを作成しよう
# コマンドラインから実行すること

# 要件定義
# ・残額、入金、引き出しの機能を実装

# 実際にATMに必要な機能をリストアップして、ご自由に開発してみてください!
"""

from account import AccountManager, BankAccount
from atm import ATM
from setting import GUIDE_MENU_MSG, pretty_number

# AccountManager -> 認証の判定
# ATM -> 認証の機能の実行、エラーメッセージの出力


def main() -> None:
    """メイン処理"""
    # アカウント情報のインスタンス化
    Account_manager = AccountManager()

    # 口座のインスタンス化
    bank_account = BankAccount(10000)

    # ATM機能のインスタンス化
    atm = ATM(bank_account, Account_manager)

    # 残金の確認
    pretty_number(bank_account.my_account_balance)
    print(f"残金:{bank_account.my_account_balance:,}円")

    # ユーザーIDの認証
    if atm.execute_auth_user_id():
        # ATMの操作案内
        atm.guide_menu(input(GUIDE_MENU_MSG["front"]))
        print(f"残金:{bank_account.my_account_balance:,}円")


if __name__ == "__main__":
    main()
