### 41. 辞書の作成
print("\n41.辞書の作成")
# 以下のキーと値を持つ辞書 `person` を作成してください：

# - キー: "name", 値: "Alice"
# - キー: "age", 値: 25
# - キー: "city", 値: "Tokyo"
person = {"name": "Alice", "age": 25, "city": "Tokyo"}


# 作成した辞書を出力してください。
print(person)

# ### 42. 辞書から値を取得
print("\n42. 辞書から値を取得")
# 以下の辞書が与えられています：

# ```python
# person = {"name": "Bob", "age": 30, "city": "Osaka"}
# ```
person = {"name": "Bob", "age": 30, "city": "Osaka"}
# キー `"age"` に対応する値を取得し、出力してください。
print(person["age"])
# ### 43. 辞書に要素を追加
print("\n43.辞書に要素を追加")
# 以下の辞書に新しいキーと値 `"country": "Japan"` を追加してください：

# ```python

# person = {"name": "Charlie", "age": 35, "city": "Kyoto"}

# ```
person = {"name": "Charlie", "age": 35, "city": "Kyoto"}
person["country"] = "Japan"
print(person)

# 変更後の辞書を出力してください。

# ---

# ### 44. 辞書の要素を削除
print("\n44.辞書の要素を削除")
# 以下の辞書からキー `"city"` を削除してください：

# ```python

# person = {"name": "Diana", "age": 28, "city": "Nagoya"}

# ```
person = {"name": "Diana", "age": 28, "city": "Nagoya"}
# 変更後の辞書を出力してください。
person.pop("city")
print(person)
