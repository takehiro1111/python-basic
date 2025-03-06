import random

jan = ["グー", "チョキ", "パー"]
judge = ["あいこ", "負け", "勝ち"]

# プレーヤー
print("0:グー 1:チョキ 2:パー")
p = int(input("じゃんけん・・・"))
print("プレーヤー：" + jan[p])

# モンスター
m = random.randint(0, 2)
print("モンスター：" + jan[m])

# 勝敗判定
i = (p - m) % 3
print(judge[i])


# print(-1 % 3)
# print(0 -2 // 3)
# print(0 -2 % 3)
