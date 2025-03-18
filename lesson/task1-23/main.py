"""
81. ATMを作成しよう
# コマンドラインから実行すること

# 要件定義
# ・残額、入金、引き出しの機能を実装

# 実際にATMに必要な機能をリストアップして、ご自由に開発してみてください!
"""

from dataclasses import dataclass


@dataclass
class BankAccount:
    """銀行口座
    銀行口座に必要な機能

    Attributes:
        __balance(int): 残高
    """

    __balance: int

    @property
    def balance(self) -> int:
        """残高の表示

        Returns:
            int: 残高
        """
        return self.__balance

    @staticmethod
    def validate_amount(amount: int) -> bool:
        """金額の検証

        Args:
            amount (int): 入力された金額

        Returns:
            bool: 金額が絶対値であればTrueを返す。
        """
        try:
            if amount == abs(amount):
                return True
            else:
                return False
        except ValueError:
            raise ValueError("数値を入力してください。")

    def deposit(self, deposit_amount: int) -> int | str:
        """入金
        Args:
            deposit_amount (int): 入金額
        Returns:
            int: 残高
        """
        try:
            if BankAccount.validate_amount(deposit_amount):
                self.__balance += deposit_amount
                return self.__balance
            else:
                return "無効な入力です。"
        except ValueError:
            raise ValueError("数値を入力してください。")

    def withdrawal(self, withdrawal_amount: int) -> int | str:
        """出金
        Args:
            withdrawal_amount (int): 出金額
        Returns:
            int: 残高
            str: 残高不足のメッセージ
        """
        try:
            if self.__balance >= withdrawal_amount and BankAccount.validate_amount(
                withdrawal_amount
            ):
                self.__balance -= withdrawal_amount
                return self.__balance
            else:
                return "無効な入力又は残高不足です。"
        except ValueError:
            raise ValueError("数値を入力してください。")


# 残金の確認
bank_amount = BankAccount(100)
print(f"残金:{bank_amount.balance}")

# 入金
deposit_amount = bank_amount.deposit(int(input("入金額を入力してください。")))
print(f"入金の実行:{deposit_amount}")

# 出金の実行
withdrawal_amount = bank_amount.withdrawal(int(input("出金額を入力してください。")))
print(f"出金の実行:{withdrawal_amount}")

# 残金の確認
print(f"残金:{bank_amount.balance}")
