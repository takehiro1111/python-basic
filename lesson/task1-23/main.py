"""
81. ATMを作成しよう
# コマンドラインから実行すること

# 要件定義
# ・残額、入金、引き出しの機能を実装

# 実際にATMに必要な機能をリストアップして、ご自由に開発してみてください!
"""

from dataclasses import dataclass

from setting import ERROR_MESSAGE, GUIDE_MENU_MSG, GUIDE_NUMBER


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


class Auth:
    """ユーザーIDと暗証番号による認証機能"""

    def __init__(self):
        self.authenticated_user_id = None

    @property
    def user_list(self) -> list[dict]:
        """ユーザーごとにIDと暗証番号のリストをデータとして保持。

        Returns:
            list[dict]: ATMの処理に必要な情報
        """
        users = [{"id": "takehiro1111", "pin": 1234}, {"id": "test-user", "pin": 5678}]
        return users

    @property
    def return_user_ids(self) -> list[str]:
        """入力されたユーザーIDと比較するために保存されているユーザーIDの一覧を取得

        Returns:
            list[string]: 全ユーザーのID
        """
        return [user["id"] for user in self.user_list]

    def get_user_pin(self, user_id: str) -> int | None:
        """入力された暗証番号と比較するために保存されているそのユーザーの暗証番号を取得

        Args:
            user_id (str): ユーザーID

        Returns:
            str | None: 登録済みのユーザーの場合に暗証番号を返す。
        """
        for user in self.user_list:
            if user_id == user["id"]:
                return user["pin"]

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
            print("ユーザーIDの入力回数を超過しました。最初からやり直してください。")
            return False

        if input_user_id in self.return_user_ids:
            self.authenticated_user_id = input_user_id
            return True
        elif input_user_id not in self.return_user_ids:
            attempt_check -= 1
            return self.auth_user_id(
                input("ユーザーiDを入力してください。(英文字 + 数字)"), attempt_check
            )

    def auth_user_pin(self, input_user_pin: int, attempt_check=3) -> bool:
        """暗証番号による認証

        Args:
            input_user_pin (int): ユーザーから入力された暗証番号
            attempt_check (int, optional): 再試行回数の上限をデフォルト値として設定

        Returns:
            bool: 暗証番号による認証の成否
        """
        if attempt_check == 0:
            print("暗証番号の入力回数を超過しました。最初からやり直してください。")
            return False

        # 入力時に比較対象になる暗証番号の取得
        correct_pin = self.get_user_pin(self.authenticated_user_id)

        if input_user_pin == correct_pin:
            print("正しい暗証番号です。")
            return True
        elif input_user_pin != correct_pin:
            print("暗証番号が間違っています。再入力してください。")
            attempt_check -= 1
            return self.auth_user_pin(
                int(input("暗証番号を入力してください。")), attempt_check
            )


class ATM:
    """ATM
    預金、引き出しの機能を持つ。
    """

    def __init__(self, bank_account: BankAccount, auth: Auth) -> None:
        self.bank_account = bank_account
        self.auth = auth

    def guide_menu(self, menu_num: int) -> int | list[str] | None:
        """_summary_

        Args:
            menu_num (int): ATMの処理を選択する番号

        Returns:
            int | list[str] | None: メニュー選択後に入金または出勤処理の関数を返す。
        """
        if menu_num == GUIDE_NUMBER["deposit"]:
            return self.deposit(input(GUIDE_MENU_MSG["deposit"]))
        elif menu_num == GUIDE_NUMBER["withdraw"]:
            return self.withdrawal(input(GUIDE_MENU_MSG["withdraw"]))

    def deposit(self, deposit_amount: str) -> int | None:
        """入金
        Args:
            deposit_amount (int): 入金額
        Returns:
            int: 残高
        """
        to_int_deposit_amount = int(deposit_amount)
        deposit_validation = DepositValidation(to_int_deposit_amount)
        try:
            if deposit_validation.validate() and self.auth.auth_user_pin(
                int(input("暗証番号を入力してください。"))
            ):
                self.bank_account.my_account_balance += to_int_deposit_amount
                print(f"{to_int_deposit_amount}円を入金しました。")
                return self.bank_account.my_account_balance

            return self.show_error_msg(deposit_validation.errors)

        except ValueError:
            print("暗証番号は数字4桁で入力してください。")
            return None

    def withdrawal(self, withdrawal_amount: str) -> int | None:
        """出金
        Args:
            withdrawal_amount (int): 出金額
        Returns:
            int: 残高
            str: 残高不足のメッセージ
        """
        to_int_withdraw_amount = int(withdrawal_amount)
        withdraw_validation = WithdrawalValidation(
            self.bank_account.my_account_balance, to_int_withdraw_amount
        )
        try:
            if withdraw_validation.validate() and self.auth.auth_user_pin(
                int(input("暗証番号を入力してください。"))
            ):
                self.bank_account.my_account_balance -= to_int_withdraw_amount
                print(f"{to_int_withdraw_amount}円を引き出しました。")
                return self.bank_account.my_account_balance

            return self.show_error_msg(withdraw_validation.errors)

        except ValueError:
            print("暗証番号は数字4桁で入力してください。")
            return None

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
    # 口座のインスタンス化
    bank_account = BankAccount(100)

    # 認証機能のインスタンス化
    auth = Auth()

    # ATM機能のインスタンス化
    atm = ATM(bank_account, auth)

    # 残金の確認
    print(f"残金:{bank_account.my_account_balance}")

    # ユーザーIDの認証
    if auth.auth_user_id(input("ユーザーIDを入力してください。(英文字 + 数字)")):
        # ATMの操作案内
        atm.guide_menu(int(input(GUIDE_MENU_MSG["front"])))

        print(f"残金:{bank_account.my_account_balance}")


if __name__ == "__main__":
    main()
