### 49. 辞書の内包表記
print("\n49.辞書の内包表記")
# 以下のリストから辞書を作成してください。キーは要素そのもので、値はその要素の長さとします：

# ```python

words = ["apple", "banana", "cherry"]

# ```
# 作成した辞書を出力してください。
new_dict = {word: len(word) for word in words}
print(new_dict)


# ---

# ### 50. 複雑な辞書の操作
print("\n50.複雑な辞書の操作")
# 以下の辞書が与えられています：

# ```python

data = {
    "user1": {"name": "Ivy", "age": 29},
    "user2": {"name": "Jack", "age": 34},
    "user3": {"name": "Kate", "age": 25},
}

# ```


# すべてのユーザーの名前をリストとして取得し、出力してください。
user_list = [user_info["name"] for user_info in data.values()]
print(user_list)


# ### 51. デフォルト値の取得
print("\n51.デフォルト値の取得")
# 以下の辞書からキー `"country"` を取得してください。ただし、そのキーが存在しない場合は `"Unknown"` を返すようにしてください：

# ```python

person = {"name": "Lily", "age": 30}

# ```
# setdefault() はキーが存在しない場合に元の辞書を変更してしまう
# country = person.setdefault("country", "Unknown")
country = person.get("country", "Unknown")
print(country)

# ---

# ### 52. ネストされた辞書の値取得
print("\n52.ネストされた辞書の値取得")
# 以下の辞書から、ユーザー2の名前を取得してください：

# ```python

data = {
    "user1": {"name": "Mike", "age": 27},
    "user2": {"name": "Nina", "age": 31},
    "user3": {"name": "Oscar", "age": 22},
}

# ```
print("パターン1----------------------------")
user_id = data.get("user2")
name = user_id.get("name") if user_id else "Unknown"
print(name)

print("パターン2----------------------------")
name2 = data["user2"]["name"]
print(name2)
