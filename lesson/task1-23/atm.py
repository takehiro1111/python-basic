from account import AccountManager, BankAccount
from setting import (
    ATM_ID_MSG,
    ATM_INPUT_MSG,
    ATM_PIN_MSG,
    ERROR_MESSAGE,
    GUIDE_MENU_MSG,
    GUIDE_NUMBER,
    pretty_number,
)
from validate import DepositValidation, WithdrawalValidation


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
            elif (
                has_int_menu_num != GUIDE_NUMBER["deposit"]
                or has_int_menu_num != GUIDE_NUMBER["withdraw"]
            ):
                print(ERROR_MESSAGE["invalid_operation"])
                attempt_check -= 1
                return self.guide_menu(input(GUIDE_MENU_MSG["front"]), attempt_check)

        except ValueError:
            print(ERROR_MESSAGE["to_int"])
            attempt_check -= 1
            return self.guide_menu(input(GUIDE_MENU_MSG["front"]), attempt_check)

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

            # 以下の条件分岐でelseを使用しないために予め結果を取得。
            result_deposit_validation = deposit_validation.validate()
            result_auth_user_pin = self.execute_auth_user_pin()

            if result_deposit_validation:
                if self.execute_auth_user_id():
                    self.bank_account.my_account_balance += to_int_deposit_amount
                    pretty_number(to_int_deposit_amount)
                    print(f"{to_int_deposit_amount:,}円を入金しました。")
                    return self.bank_account.my_account_balance

                elif result_auth_user_pin is False:
                    attempt_check -= 1
                    print(ERROR_MESSAGE["invalid_amount"])
                    return self.deposit(input(GUIDE_MENU_MSG["deposit"]), attempt_check)

            elif result_deposit_validation is False:
                attempt_check -= 1
                print(ERROR_MESSAGE["invalid_amount"])
                return self.deposit(input(GUIDE_MENU_MSG["deposit"]), attempt_check)

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

            # 以下の条件分岐でelseを使用しないために予め結果を取得。
            result_withdraw_validation = withdraw_validation.validate()
            result_auth_user_pin = self.execute_auth_user_pin()

            if result_withdraw_validation:
                if result_auth_user_pin:
                    self.bank_account.my_account_balance -= to_int_withdraw_amount
                    pretty_number(to_int_withdraw_amount)
                    print(f"{to_int_withdraw_amount:,}円を引き出しました。")
                    return self.bank_account.my_account_balance
                elif result_auth_user_pin is False:
                    attempt_check -= 1
                    print(ERROR_MESSAGE["invalid_amount"])
                    return self.withdrawal(
                        input(GUIDE_MENU_MSG["withdraw"]), attempt_check
                    )

            elif result_withdraw_validation is False:
                attempt_check -= 1
                print(ERROR_MESSAGE["invalid_amount"])
                return self.withdrawal(input(GUIDE_MENU_MSG["withdraw"]), attempt_check)

        except ValueError:
            print(ERROR_MESSAGE["to_int"])
            attempt_check -= 1
            return self.withdrawal(input(GUIDE_MENU_MSG["withdraw"]), attempt_check)

    @staticmethod
    def show_error_msg(error_msg: list[str]) -> None:
        for msg in error_msg:
            print(msg)
        return None

    def execute_auth_user_id(self, attempt_check=4) -> bool:
        """ユーザーID認証の実行とメッセージ出力
        Args:
            attempt_check (int): 残り試行回数
        Returns:
            bool: 認証成功ならTrue
        """
        if attempt_check == 0:
            print(ATM_ID_MSG["exceed_limit_input_id"])
            return False

        # AccountManagerに判定のみを依頼
        if self.account_manager.auth_user_id(input(ATM_ID_MSG["input_user_id"])):
            return True

        # 認証が成功しない場合は3回まで再試行。
        attempt_check -= 1
        return self.execute_auth_user_id(attempt_check)

    def execute_auth_user_pin(self, attempt_check=4) -> bool:
        """暗証番号認証の実行とメッセージ出力
        Args:
            attempt_check (int): 残り試行回数
        Returns:
            bool: 認証成功ならTrue
        """
        if attempt_check == 0:
            print(ATM_PIN_MSG["exceed_limit_input_pin"])
            return False

        result_auth_user_pin = self.account_manager.auth_user_pin(
            input(ATM_PIN_MSG["input_pin"])
        )
        # AccountManagerに判定のみを依頼
        if result_auth_user_pin:
            print(ATM_PIN_MSG["correct_input_pin"])
            return True
        elif result_auth_user_pin is False:
            attempt_check -= 1
            return self.execute_auth_user_pin(attempt_check)
