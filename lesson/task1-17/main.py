# 58. キーと値の入れ替え
print("\n58. キーと値の入れ替え")
# 以下の辞書でキーと値を入れ替えた新しい辞書を作成してください：

original = {"a": 1, "b": 2, "c": 3}

new_dict = {v: k for k, v in original.items()}
print(new_dict)


# 59. リストを辞書に変換
print("\n59. リストを辞書に変換")
# 以下のリストを辞書に変換してください。リストの偶数インデックスの要素をキー、奇数インデックスの要素を値とします：

data = ["name", "Alice", "age", 25, "city", "Tokyo"]
new_data = {data[i]: data[i + 1] for i in range(0, len(data), 2) if i < len(data)}

# ステップを2段階で分けなくても書けるためコメントアウト。
# for i, element in enumerate(data):
#   if i == 0 or i % 2 == 0:
#     # インデックスが0又は偶数の場合は辞書にキーをセットする。
#     new_data[element] = None
#   elif i % 2 == 1:
#     # インデックスが奇数の場合は辞書に値をセットする。
#     new_data[data[i-1]] = element

print(new_data)

# 60. 辞書を使ったグルーピング
print("\n60. 辞書を使ったグルーピング")
# 以下のリストを値ごとにグルーピングした辞書を作成してください：

data = [
    ("fruit", "apple"),
    ("fruit", "banana"),
    ("vegetable", "carrot"),
    ("fruit", "cherry"),
]
new_dict = {}

for k, v in data:
    if k not in new_dict:
        # キーがなければ辞書の要素にキーと値として空のリストを追加する。
        new_dict[k] = []
    # 　同じキーは既に存在するキーの値としてリストの要素に追加する。
    new_dict[k].append(v)

print(new_dict)
