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


class ATM:
    """ATM
    預金、引き出しの機能を持つ。
    """

    def __init__(self, bank_account: BankAccount) -> None:
        self.bank_account = bank_account
        self.balance = bank_account.my_account_balance

    def guide_menu(self, menu_num: int) -> int | list[str] | None:
        if menu_num == GUIDE_NUMBER["deposit"]:
            return self.deposit(input(GUIDE_MENU_MSG["deposit"]))
        elif menu_num == GUIDE_NUMBER["withdraw"]:
            return self.withdrawal(input(GUIDE_MENU_MSG["withdraw"]))

    def deposit(self, deposit_amount: str) -> int | list[str]:
        """入金
        Args:
            deposit_amount (int): 入金額
        Returns:
            int: 残高
        """
        to_int_deposit_amount = int(deposit_amount)
        deposit_validation = DepositValidation(to_int_deposit_amount)
        if deposit_validation.validate():
            self.balance += to_int_deposit_amount
            self.bank_account.my_account_balance = self.balance
            return self.balance
        else:
            print(deposit_validation.errors[0])

    def withdrawal(self, withdrawal_amount: str) -> int | None:
        """出金
        Args:
            withdrawal_amount (int): 出金額
        Returns:
            int: 残高
            str: 残高不足のメッセージ
        """
        to_int_withdraw_amount = int(withdrawal_amount)
        withdraw_validation = WithdrawalValidation(self.balance, to_int_withdraw_amount)
        if withdraw_validation.validate():
            self.balance -= to_int_withdraw_amount
            self.bank_account.my_account_balance = self.balance
            return self.balance
        else:
            print(withdraw_validation._errors[0])


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
        elif self.amount < 0:
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
        elif self.amount < 0:
            self.errors = ERROR_MESSAGE["value_greater_than"]
        elif self.amount is None:
            self.errors = ERROR_MESSAGE["not_entry"]

        return self.is_valid


def main() -> None:
    """メイン処理"""
    # 残金の確認
    bank_account = BankAccount(100)
    print(f"残金:{bank_account.my_account_balance}")

    # ATM機能のインスタンス化
    atm = ATM(bank_account)

    # ATMの操作案内
    atm.guide_menu(int(input(GUIDE_MENU_MSG["front"])))

    print(f"残金:{bank_account.my_account_balance}")


if __name__ == "__main__":
    main()
