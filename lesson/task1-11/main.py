### 40. じゃんけん

# 下記の要件を満たす「じゃんけんプログラム」を開発してください。
# 要件定義
# ・使用可能な手はグー、チョキ、パー
# ・勝ち負けは、通常のじゃんけん
# ・Pythonファイルの実行はコマンドラインから。
# ご自身が自由に設計して、プログラムを書いてみましょう！

import random

# じゃんけんの手札の設定

ROCK = "グー"
SCISSORS = "チョキ"
PAPER = "パー"
janken_hands = [ROCK, SCISSORS, PAPER]


INPUT_ROCK = 1
INPUT_SCISSORS = 2
INPUT_PAPER = 3

WIN = "win"
LOSE = "lose"
DRAW = "draw"

YES = "yes"
NO = "no"


def validate_hand(input_hand: str) -> bool:
    return input_hand.isdigit()


# ユーザー側の入力じゃんけんの手を入力
def input_human_hand(hands_list: list) -> str:
    hand_index = input(
        f"あなたの手を数字で入力してください（{ROCK}:{str(INPUT_SCISSORS)} / {SCISSORS}:{str(INPUT_SCISSORS)} / {PAPER}:{str(INPUT_PAPER)}）"
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
    random_index = random.randint(0, 2)
    compute_user_hand = hands_list[random_index]
    print(f"コンピューター側の手:{compute_user_hand}")

    return compute_user_hand


# 判定部分
def judge_hands(compute_hand: str, human_hand: str) -> str:
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
    if judge_result == WIN:
        return "あなたの勝ちです。"
    elif judge_result == LOSE:
        return "あなたの負けです。"
    elif judge_result == DRAW:
        return "引き分けです。"

# 結果表示
def display_result(game_result: str) -> None:
    print(game_result)

# 再戦の確認
def again_question(yes, no) -> str:
    again = input(f"再度じゃんけんしますか？({yes}/{no}) ")
    return again.lower()

# 再戦するかの分岐
def again_judge(again, yes, no):
    if again == yes:
        return main
    elif again == no:
        return "じゃんけん終了です。"

# 再戦しない場合の終了出力
def display_finish(finish: str) -> None:
    print(finish)


# メイン処理: じゃんけんの結果を出力。
def main() -> str:
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
