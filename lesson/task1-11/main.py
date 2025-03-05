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


# コンピュータの出し手の設定
def compute_hand(hands_list):
    random_index = random.randint(0, 2)
    compute_user_hand = hands_list[random_index]

    return compute_user_hand


# ユーザー側の入力じゃんけんの手を入力
def input_user_hand(hands_list):
    hand_index = int(
        input("あなたの手を数字で入力してください（グー:1 / チョキ:2 / パー:3）")
    )
    human_hand = hands_list[hand_index - 1]
    if human_hand in hands_list:
        return human_hand
    else:
        return input_user_hand(hands_list)


# 判定部分
def judge_hands(compute_hand, human_hand):
    if compute_hand == "グー":
        if human_hand == "チョキ":
            return "あなたの負けです。"
        elif human_hand == "パー":
            return "あなたの勝ちです。"
        elif human_hand == "グー":
            return "引き分けです。"
    elif compute_hand == "チョキ":
        if human_hand == "チョキ":
            return "引き分けです。"
        elif human_hand == "パー":
            return "あなたの負けです。"
        elif human_hand == "グー":
            return "あなたの勝ちです。"
    elif compute_hand == "パー":
        if human_hand == "チョキ":
            return "あなたの勝ちです。"
        elif human_hand == "パー":
            return "引き分けです。"
        elif human_hand == "グー":
            return "あなたの負けです。"


# メイン処理
def main():
    compute = compute_hand(janken_hands)
    human = input_user_hand(janken_hands)
    result = judge_hands(compute, human)

    return result


if __name__ == "__main__":
    janken = main()
    print(janken)
