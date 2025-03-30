from dataclasses import dataclass


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

    def auth_user_id(self, input_user_id: str) -> bool:
        """ユーザーIDの判定のみを行う
        Args:
            input_user_id (str): ユーザーから入力されたID
        Returns:
            bool: ユーザーIDが有効ならTrue
        """
        for user in self.account_info():
            if input_user_id == user["id"]:
                self._authenticated_user_pin = user["pin"]
                return True
        return False

    def auth_user_pin(self, input_user_pin: str) -> bool:
        """暗証番号の判定のみを行う
        Args:
            input_pin (str): ユーザーから入力された暗証番号
        Returns:
            bool: 暗証番号が正しければTrue
        """
        try:
            to_int_user_pin = int(input_user_pin)
            if to_int_user_pin == self._authenticated_user_pin:
                return True
            elif to_int_user_pin != self._authenticated_user_pin:
                return False

        except ValueError:
            return False


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
