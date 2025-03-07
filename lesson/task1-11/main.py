### 40. じゃんけん

# 下記の要件を満たす「じゃんけんプログラム」を開発してください。
# 要件定義
# ・使用可能な手はグー、チョキ、パー
# ・勝ち負けは、通常のじゃんけん
# ・Pythonファイルの実行はコマンドラインから。
# ご自身が自由に設計して、プログラムを書いてみましょう！

import random

from setting import (
    DRAW,
    INPUT_PAPER,
    INPUT_ROCK,
    INPUT_SCISSORS,
    LOSE,
    NO,
    PAPER,
    ROCK,
    SCISSORS,
    WIN,
    YES,
    janken_hands,
)


def validate_hand(input_hand: str) -> bool:
    """
    ユーザーが入力した値が数字かどうかを検証する。

    Args:
        input_hand: ユーザーが入力した文字列

    Returns:
        bool: 入力が数字のみの場合はTrue、それ以外の場合はFalse
    """
    return input_hand.isdigit()


# ユーザー側の入力じゃんけんの手を入力
def input_human_hand(hands_list: list) -> str:
    """
    ユーザーにじゃんけんの手を入力してもらう。

    Args:
        hands_list: じゃんけんの手（グー、チョキ、パー）のリスト

    Returns:
        str: ユーザーが選択した手

    Raises:
        IndexError: 1-3以外の数字が入力された場合に発生するが、関数内で捕捉して再帰的に再入力を求める
    """
    hand_index = input(
        f"あなたの手を数字で入力してください（{ROCK}:{str(INPUT_ROCK)} / {SCISSORS}:{str(INPUT_SCISSORS)} / {PAPER}:{str(INPUT_PAPER)}）"
    )

    try:
        if validate_hand(hand_index):
            # ユーザーには1以上の数字を入力させるためにインデックスの帳尻合わせを実施。
            index = int(hand_index) - 1
            human_hand = hands_list[index]
            print(f"ユーザー側の手:{human_hand}")
            return human_hand
        else:
            return input_human_hand(hands_list)
    except IndexError:
        print("1-3の数字を入力してください。")
        return input_human_hand(hands_list)


# コンピュータの出し手の設定
def compute_hand(hands_list: list) -> str:
    """
    コンピュータのじゃんけんの手をランダムに選択する。

    Args:
        hands_list: じゃんけんの手（グー、チョキ、パー）のリスト

    Returns:
        str: コンピュータが選んだ手
    """
    random_index = random.randint(0, 2)
    compute_user_hand = hands_list[random_index]
    print(f"コンピューター側の手:{compute_user_hand}")

    return compute_user_hand


# 判定部分
def judge_hands(compute_hand: str, human_hand: str) -> str:
    """
    じゃんけんの勝敗を判定する。

    Args:
        compute_hand: コンピュータが選んだ手
        human_hand: ユーザーが選んだ手

    Returns:
        str: 勝ち（WIN）、負け（LOSE）、引き分け（DRAW）のいずれかの結果
    """
    if compute_hand == ROCK:
        if human_hand == ROCK:
            return DRAW
        elif human_hand == SCISSORS:
            return LOSE
        elif human_hand == PAPER:
            return WIN

    elif compute_hand == SCISSORS:
        if human_hand == ROCK:
            return WIN
        elif human_hand == SCISSORS:
            return DRAW
        elif human_hand == PAPER:
            return LOSE

    elif compute_hand == PAPER:
        if human_hand == ROCK:
            return LOSE
        elif human_hand == SCISSORS:
            return WIN
        elif human_hand == PAPER:
            return DRAW


# 結果出力
def result_output(judge_result: str) -> str:
    """
    じゃんけんの結果を文字列に変換する。

    Args:
        judge_result: 判定結果（WIN、LOSE、DRAW）

    Returns:
        str: 結果を表す日本語のメッセージ
    """
    if judge_result == WIN:
        return "あなたの勝ちです。"
    elif judge_result == LOSE:
        return "あなたの負けです。"
    elif judge_result == DRAW:
        return "引き分けです。"


# 結果表示
def display_result(game_result: str) -> None:
    """
    ゲーム結果を画面に表示する。

    Args:
        game_result: 表示するゲーム結果のメッセージ

    Returns:
        None
    """
    print(game_result)


# 再戦の確認
def again_question(yes: str, no: str) -> str:
    """
    ユーザーに再戦するかどうかを尋ねる。

    Args:
        yes: 再戦する場合の入力値
        no: 再戦しない場合の入力値

    Returns:
        str: ユーザーの回答（小文字に変換）
    """
    again = input(f"再度じゃんけんしますか？({yes}/{no}) ")
    return again.lower()


# 再戦するかの分岐
def again_judge(again: str, yes: str, no: str) -> None | str:
    """
    再戦するかどうかの判断を行う。

    Args:
        again: ユーザーの回答
        yes: 再戦する場合の入力値
        no: 再戦しない場合の入力値

    Returns:
        function or str: 再戦する場合はmain関数、しない場合は終了メッセージ
    """
    if again == yes:
        return main
    elif again == no:
        return "じゃんけん終了です。"


# 再戦しない場合の終了出力
def display_finish(finish: str) -> None:
    """
    終了メッセージを表示する。

    Args:
        finish: 表示する終了メッセージ

    Returns:
        None
    """
    print(finish)


# メイン処理: じゃんけんの結果を出力。
def main() -> str:
    """
    じゃんけんゲームのメイン処理を実行する。

    ユーザーとコンピュータのじゃんけんを実施し、結果を表示して再戦するかどうかを確認する。

    Returns:
        str or None: 再戦しない場合は終了メッセージを表示した後にNone、再戦する場合は再帰的に自身を呼び出す
    """
    human = input_human_hand(janken_hands)
    compute = compute_hand(janken_hands)
    judge_result = judge_hands(compute, human)
    result = result_output(judge_result)
    display_result(result)
    again = again_question(YES, NO)

    again_or_finish = again_judge(again, YES, NO)

    if again_or_finish == main:
        return main()
    else:
        return display_finish(again_or_finish)


if __name__ == "__main__":
    main()
