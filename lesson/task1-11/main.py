### 40. じゃんけん

# 下記の要件を満たす「じゃんけんプログラム」を開発してください。
# 要件定義
# ・使用可能な手はグー、チョキ、パー
# ・勝ち負けは、通常のじゃんけん
# ・Pythonファイルの実行はコマンドラインから。
# ご自身が自由に設計して、プログラムを書いてみましょう！

import random

# じゃんけんの手札の設定
rock = "グー"
scissors = "チョキ"
paper = "パー"
janken_hands = [rock, scissors, paper]


# ユーザー側の入力じゃんけんの手を入力
def input_human_hand(hands_list: list) -> str:
    hand_index = input(
        f"あなたの手を数字で入力してください（{rock}:1 / {scissors}:2 / {paper}:3）"
    )

    try:
        if hand_index.isdigit():
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
    if compute_hand == rock:
        if human_hand == rock:
            return "引き分けです。"
        elif human_hand == scissors:
            return "あなたの負けです。"
        elif human_hand == paper:
            return "あなたの勝ちです。"

    elif compute_hand == scissors:
        if human_hand == rock:
            return "あなたの勝ちです。"
        elif human_hand == scissors:
            return "引き分けです。"
        elif human_hand == paper:
            return "あなたの負けです。"

    elif compute_hand == paper:
        if human_hand == rock:
            return "あなたの負けです。"
        elif human_hand == scissors:
            return "あなたの勝ちです。"
        elif human_hand == paper:
            return "引き分けです。"


# メイン処理: じゃんけんの結果を出力。
def main() -> str:
    human = input_human_hand(janken_hands)
    compute = compute_hand(janken_hands)
    result = judge_hands(compute, human)

    return result


if __name__ == "__main__":
    janken = main()
    print(janken)
