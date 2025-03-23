"""
81. ATMを作成しよう
# コマンドラインから実行すること

# 要件定義
# ・残額、入金、引き出しの機能を実装

# 実際にATMに必要な機能をリストアップして、ご自由に開発してみてください!
"""

from dataclasses import dataclass

from setting import ERROR_MESSAGE


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


class ATM:
    """ATM
    預金、引き出しの機能を持つ。
    """

    def __init__(self):
        self.balance = BankAccount.my_account_balance

    def guide_menu(self, menu_num: int):
        if menu_num == 0:
            return ATM.deposit()
        elif menu_num == 1:
            return ATM.withdrawal()
        else:
            return ATM.guide_menu(menu_num)

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
            return self.balance
        else:
            return deposit_validation.errors

    def withdrawal(self, withdrawal_amount: str) -> int | list[str]:
        """出金
        Args:
            withdrawal_amount (int): 出金額
        Returns:
            int: 残高
            str: 残高不足のメッセージ
        """
        to_int_deposit_amount = int(withdrawal_amount)
        withdraw_validation = WithdrawalValidation(self.balance, to_int_deposit_amount)
        if withdraw_validation.validate():
            self.balance -= to_int_deposit_amount
            return self.balance
        else:
            return withdraw_validation.errors


@dataclass
class BaseValidation:
    _errors: str

    @property
    def errors(self) -> list[str]:
        return self._errors if self._errors else []


@dataclass
class DepositValidation(BaseValidation):
    """validate
    預金時のvalidate

    Attributes:
        amount(int): 入金額
    """

    def __init__(self, amount: int) -> None:
        self.amount = amount

    def validate(self) -> bool:
        """金額の検証

        Args:
            amount (int): 入力された金額

        Returns:
            bool: 金額が絶対値であればTrueを返す。
        """
        self._errors = []

        if self.amount is None:
            self._errors.append(ERROR_MESSAGE["not_entry"])
        elif self.amount < 0:
            self._errors.append(ERROR_MESSAGE["value_greater_than"])

        return True if len(self._errors) == 0 else False


@dataclass
class WithdrawalValidation(BaseValidation):
    """validate
    引き出し時のvalidate

    Attributes:
        balance(int): 残高
        amount(int): 入金額
    """

    balance: int
    amount: int

    def validate(self) -> bool:
        """金額の検証

        Args:
            balance(int): 残高
            amount (int): 入力された金額

        Returns:
            bool: 金額が絶対値であればTrueを返す。
        """
        self._errors = []
        if self.balance < self.amount:
            self._errors.append(ERROR_MESSAGE["insufficient_balance"])
        elif self.amount < 0:
            self._errors.append(ERROR_MESSAGE["value_greater_than"])
        elif self.amount is None:
            self._errors.append(ERROR_MESSAGE["not_entry"])

        return True if len(self._errors) == 0 else False


# 残金の確認
bank_account = BankAccount(100)
print(f"残金:{bank_account._balance}")

# ATM機能のインスタンス化
atm = ATM()

# 入金
deposit_amount = atm.deposit(input("入金額を入力してください。"))
print(f"入金の実行:{deposit_amount}")

# 出金の実行
withdrawal_amount = atm.withdrawal(input("出金額を入力してください。"))
print(f"出金の実行:{withdrawal_amount}")

# 残金の確認
print(f"残金:{atm.balance}")
