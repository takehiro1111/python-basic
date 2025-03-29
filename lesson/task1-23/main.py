"""
81. ATMを作成しよう
# コマンドラインから実行すること

# 要件定義
# ・残額、入金、引き出しの機能を実装

# 実際にATMに必要な機能をリストアップして、ご自由に開発してみてください!
"""

from dataclasses import dataclass

from setting import (
    ATM_ID_MSG,
    ATM_INPUT_MSG,
    ATM_PIN_MSG,
    ERROR_MESSAGE,
    GUIDE_MENU_MSG,
    GUIDE_NUMBER,
)


class AccountManager:
    """銀行口座の属性情報を管理
    認証に必要なユーザーIDと暗証番号を保持。

    """

    # 直接参照はしない
    _USERS: list[dict] = [
        {"id": "takehiro1111", "pin": 1234},
        {"id": "Michael", "pin": 5678},
    ]

    def __init__(self):
        self._authenticated_user_pin = None

    @classmethod
    def account_info(cls) -> list[dict]:
        """ユーザーごとにIDと暗証番号のリストをデータとして保持。

        Returns:
            list[dict]: ユーザーの属性情報
        """
        return cls._USERS

    def get_auth_user_by_id(self, input_user_id: str) -> dict | None:
        for user in self.account_info():
            if input_user_id == user["id"]:
                self._authenticated_user_id = user["pin"]
                return user
        return None

    def auth_user_id(self, input_user_id: str, attempt_check=3) -> bool:
        """ユーザーIDによる認証

        Args:
            input_user_id (str): ユーザーから入力されたID
            attempt_check (int, optional): 再試行回数の上限をデフォルト値として設定

        Returns:
            bool: ユーザーIDによる認証の成否
        """
        if attempt_check == 0:
            print(ATM_ID_MSG["exceed_limit_input_id"])
            return False

        has_auth_user = self.get_auth_user_by_id(input_user_id)

        if has_auth_user is None:
            attempt_check -= 1
            return self.auth_user_id(input(ATM_ID_MSG["input_user_id"]), attempt_check)
        elif has_auth_user is not None:
            self._authenticated_user_pin = has_auth_user["pin"]
            return True

    def auth_user_pin(self, input_user_pin: str, attempt_check=3) -> bool:
        """暗証番号による認証

        Args:
            input_user_pin (int): ユーザーから入力された暗証番号
            attempt_check (int, optional): 再試行回数の上限をデフォルト値として設定

        Returns:
            bool: 暗証番号による認証の成否
        """
        if attempt_check == 0:
            print(ATM_PIN_MSG["exceed_limit_input_pin"])
            return False

        try:
            to_int_input_user_pin = int(input_user_pin)

            if to_int_input_user_pin == self._authenticated_user_pin:
                print(ATM_PIN_MSG["correct_input_pin"])
                return True
            elif to_int_input_user_pin != self._authenticated_user_pin:
                print(ATM_PIN_MSG["mistake_input_pin"])
                attempt_check -= 1
                return self.auth_user_pin(
                    input(ATM_PIN_MSG["input_pin"]), attempt_check
                )

        except ValueError:
            print(ATM_PIN_MSG["type_err_input_pin"])
            attempt_check -= 1
            return self.auth_user_pin(input(ATM_PIN_MSG["input_pin"]), attempt_check)


@dataclass
class BankAccount:
    """銀行口座
    残高のデータを確認する。

    Attributes:
        _balance(int): 残高
    """

    _balance: int

    @property
    def my_account_balance(self) -> int:
        """残高の表示

        Returns:
            int: 残高
        """
        return self._balance

    @my_account_balance.setter
    def my_account_balance(self, result_after_atm: int) -> None:
        """ATM処理後の残高更新

        Args:
            int: ATMクラスのメソッドで処理した後の残高
        """
        self._balance = result_after_atm


class ATM:
    """ATM
    預金、引き出しの機能を持つ。
    """

    def __init__(
        self, bank_account: BankAccount, account_manager: AccountManager
    ) -> None:
        self.bank_account = bank_account
        self.account_manager = (
            account_manager  # インスタンスメソッドを使用したいため初期化。
        )

    def guide_menu(self, menu_num: str, attempt_check=3) -> int | list[str] | None:
        """_summary_

        Args:
            menu_num (int): ATMの処理を選択する番号

        Returns:
            int | list[str] | None: メニュー選択後に入金または出勤処理の関数を返す。
        """
        try:
            if attempt_check == 0:
                print(ATM_INPUT_MSG["exceed_limit"])
                return

            has_int_menu_num = int(menu_num)
            if has_int_menu_num == GUIDE_NUMBER["deposit"]:
                return self.deposit(input(GUIDE_MENU_MSG["deposit"]))
            elif has_int_menu_num == GUIDE_NUMBER["withdraw"]:
                return self.withdrawal(input(GUIDE_MENU_MSG["withdraw"]))

        except ValueError:
            print(ERROR_MESSAGE["to_int"])
            attempt_check -= 1
            self.guide_menu(input(GUIDE_MENU_MSG["front"]), attempt_check)

    def deposit(self, deposit_amount: str, attempt_check=3) -> int | bool:
        """入金
        Args:
            deposit_amount (int): 入金額
        Returns:
            int: 残高
        """
        try:
            if attempt_check == 0:
                print(ATM_INPUT_MSG["exceed_limit"])
                return

            to_int_deposit_amount = int(deposit_amount)
            deposit_validation = DepositValidation(to_int_deposit_amount)

            if deposit_validation.validate() and self.account_manager.auth_user_pin(
                input(ATM_PIN_MSG["input_pin"])
            ):
                self.bank_account.my_account_balance += to_int_deposit_amount
                print(f"{to_int_deposit_amount}円を入金しました。")
                return self.bank_account.my_account_balance

            return self.show_error_msg(deposit_validation.errors)
        except ValueError:
            print(ERROR_MESSAGE["to_int"])
            attempt_check -= 1
            self.deposit(input(GUIDE_MENU_MSG["deposit"]), attempt_check)

    def withdrawal(self, withdrawal_amount: str, attempt_check=3) -> int | None:
        """出金
        Args:
            withdrawal_amount (int): 出金額
        Returns:
            int: 残高
            str: 残高不足のメッセージ
        """
        try:
            if attempt_check == 0:
                print(ATM_INPUT_MSG["exceed_limit"])
                return

            to_int_withdraw_amount = int(withdrawal_amount)
            withdraw_validation = WithdrawalValidation(
                self.bank_account.my_account_balance, to_int_withdraw_amount
            )

            if withdraw_validation.validate():
                if self.account_manager.auth_user_pin(input(ATM_PIN_MSG["input_pin"])):
                    self.bank_account.my_account_balance -= to_int_withdraw_amount
                    print(f"{to_int_withdraw_amount}円を引き出しました。")
                    return self.bank_account.my_account_balance
            # 出金額が残高以上などのValueとしてエラーにはならない場合の処理としてelseを使用している。
            else:
                attempt_check -= 1
                print(ERROR_MESSAGE["invalid_amount"])
                return self.withdrawal(input(GUIDE_MENU_MSG["withdraw"]), attempt_check)

            return self.show_error_msg(withdraw_validation.errors)

        except ValueError:
            print(ERROR_MESSAGE["to_int"])
            attempt_check -= 1
            return self.withdrawal(input(GUIDE_MENU_MSG["withdraw"]), attempt_check)

    @staticmethod
    def show_error_msg(error_msg: list[str]) -> None:
        for msg in error_msg:
            print(msg)
        return None


class BaseValidation:
    def __init__(self) -> None:
        self._errors = []

    @property
    def errors(self) -> list[str]:
        return self._errors

    @errors.setter
    def errors(self, error_msg: str) -> None:
        self._errors.append(error_msg)

    @property
    def is_valid(self) -> bool:
        return len(self._errors) == 0


class DepositValidation(BaseValidation):
    """validate
    預金時のvalidate

    Attributes:
        amount(int): 入金額
    """

    def __init__(self, amount: int) -> None:
        super().__init__()
        self.amount = amount

    def validate(self) -> bool:
        """金額の検証

        Args:
            amount (int): 入力された金額

        Returns:
            bool: 金額が絶対値であればTrueを返す。
        """
        if self.amount is None:
            self.errors = ERROR_MESSAGE["not_entry"]
        elif self.amount < 1:
            self.errors = ERROR_MESSAGE["value_greater_than"]

        return self.is_valid


class WithdrawalValidation(BaseValidation):
    """validate
    引き出し時のvalidate

    Attributes:
        balance(int): 残高
        amount(int): 入金額
    """

    def __init__(self, balance: int, amount: int) -> None:
        super().__init__()
        self.amount = amount
        self.balance = balance

    def validate(self) -> bool:
        """金額の検証

        Args:
            balance(int): 残高
            amount (int): 入力された金額

        Returns:
            bool: 金額が絶対値であればTrueを返す。
        """
        if self.balance < self.amount:
            self.errors = ERROR_MESSAGE["insufficient_balance"]
        elif self.amount < 1:
            self.errors = ERROR_MESSAGE["value_greater_than"]
        elif self.amount is None:
            self.errors = ERROR_MESSAGE["not_entry"]

        return self.is_valid


def main() -> None:
    """メイン処理"""
    # アカウント情報のインスタンス化
    Account_manager = AccountManager()

    # 口座のインスタンス化
    bank_account = BankAccount(100)

    # ATM機能のインスタンス化
    atm = ATM(bank_account, Account_manager)

    # 残金の確認
    print(f"残金:{bank_account.my_account_balance}円")

    # ユーザーIDの認証
    if Account_manager.auth_user_id(input(ATM_ID_MSG["input_user_id"])):
        # ATMの操作案内
        atm.guide_menu(input(GUIDE_MENU_MSG["front"]))

        print(f"残金:{bank_account.my_account_balance}円")


if __name__ == "__main__":
    main()
