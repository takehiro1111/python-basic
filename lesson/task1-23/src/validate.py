# The above code defines two classes, `DepositValidation` and `WithdrawalValidation`, that perform
# validation for deposit and withdrawal transactions, respectively, based on the provided amount and
# balance.
from src.setting import ERROR_MESSAGE


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


class WithdrawalsValidation(BaseValidation):
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

        if self.amount is None:
            self.errors = ERROR_MESSAGE["not_entry"]
        elif self.amount < 1:
            self.errors = ERROR_MESSAGE["value_greater_than"]
        elif self.balance < self.amount:
            self.errors = ERROR_MESSAGE["insufficient_balance"]
        return self.is_valid
