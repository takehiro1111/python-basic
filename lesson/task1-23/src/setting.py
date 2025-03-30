ERROR_MESSAGE = {
    "insufficient_balance": "残高不足です。",
    "not_entry": "金額が入力されていません。",
    "value_greater_than": "1以上の数字を入力してください。",
    "to_int": "数値で入力してください。",
    "invalid_amount": "適切な金額で入力してください。",
    "invalid_operation": "入力値が間違っています。画面に表示されている数字を入力してください。",
}

GUIDE_NUMBER = {
    "deposit": 1,
    "withdraw": 2,
}

GUIDE_MENU_MSG = {
    "front": f"メニュー(入金:{GUIDE_NUMBER["deposit"]} / 出金:{GUIDE_NUMBER["withdraw"]})",
    "deposit": "入金額を入力してください。",
    "withdraw": "出金額を入力してください。",
}

ATM_ID_MSG = {
    "input_user_id": "ユーザーiDを入力してください。(英文字 + 数字)",
    "exceed_limit_input_id": "ユーザーIDの入力回数を超過しました。最初からやり直してください。"
}

ATM_PIN_MSG = {
    "input_pin": "暗証番号を入力してください。",
    "type_err_input_pin": "暗証番号は数字4桁で入力してください。",
    "mistake_input_pin": "暗証番号が間違っています。再入力してください。",
    "correct_input_pin": "正しい暗証番号です。",
    "exceed_limit_input_pin": "暗証番号の入力回数を超過しました。最初からやり直してください。",
}

ATM_INPUT_MSG = {
    "exceed_limit": "無効な入力により入力回数の上限を超過しました。最初からやり直してください。"
}

def pretty_number(big_int: int)-> str:
    """金額表示の際に視認性を担保するための処理。

    Args:
        big_int (int): 口座残高

    Returns:
        str: 桁区切りを実行
    """
    return  f"{big_int:,}"
