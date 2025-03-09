# ### 45. キーの存在確認
print("\n45.キーの存在確認")
# 以下の辞書が与えられています：
# ```python

# person = {"name": "Eve", "age": 22}

# ```

# キー `"city"` が辞書に存在するか確認し、その結果を出力してください。
person = {"name": "Eve", "age": 22}
print("age" in person)

# ---

# ### 46. 辞書のすべてのキーと値をループで取得
print("\n46.辞書のすべてのキーと値をループで取得")
# 以下の辞書が与えられています：

# ```python

# person = {"name": "Frank", "age": 40, "city": "Sapporo"}

# ```
person = {"name": "Frank", "age": 40, "city": "Sapporo"}

# すべてのキーと値を `"キー: 値"` という形式で1行ずつ出力してください。
for k, v in person.items():
    print(f"{k}:{v}")

# ---

# ### 47. 辞書のマージ
print("\n47. 辞書のマージ")
# 以下の2つの辞書を1つにマージしてください：

# ```python

# dict1 = {"name": "Grace", "age": 33}
# dict2 = {"city": "Kobe", "country": "Japan"}

# ```

# マージ後の辞書を出力してください。
dict1 = {"name": "Grace", "age": 33}
dict2 = {"city": "Kobe", "country": "Japan"}

print("パターン1---------------------")
merge_dict = dict1 | dict2
print(merge_dict)

print("パターン2---------------------")
dict1_copy = dict1.copy()
dict1_copy.update(dict2)
print(dict1_copy)


# ---

# ### 48. 辞書の値を更新
print("\n48. 辞書の値を更新")
# 以下の辞書でキー `"age"` の値を `45` に更新してください：

# ```python

# person = {"name": "Henry", "age": 40, "city": "Sendai"}

# ```

# 更新後の辞書を出力してください。
person = {"name": "Henry", "age": 40, "city": "Sendai"}
person["age"] = 45
print(person)
