### 53. シャローコピーとディープコピー
print("\n53. シャローコピーとディープコピー")
# 以下の辞書をシャローコピーし、ディープコピーしてください。

# またコピーした後にそれぞれの任意のフィールドを変更後、シャローコピー、ディープコピー、
# originalをそれぞれ出力し、動作の違いを確認してください。

# ```python

original = {"a": {"nested": 1}, "b": 2}

# ```
print(f"コピー元:{original}\n")

# ディープコピー
## コピーした後にコピー元を変更しても既にコピーしているため影響ない。独立しているイメージ。
import copy

deep_original = copy.deepcopy(original)
original["a"]["nested"] = 100
print("Original:", original)
print("Deep Copy:", deep_original)


# ```python

original = {"a": {"nested": 1}, "b": 2}

# ```

# シャローコピー
## コピーした後にコピー元を変更するとコピー先にも変更が適用される。連動して依存しているイメージ。
shallow_original = copy.copy(original)
original["a"]["nested"] = 80
print("\nOriginal:", original)
print(f"shallow_copy:{original}")

# ---

# ### 54. 辞書のキーでソート
print("\n54. 辞書のキーでソート")
# 以下の辞書をキーでソートしてください：

# ```python

scores = {"Charlie": 85, "Alice": 92, "Bob": 78}

# ```
sorted_dict = sorted(scores.items())
print(dict(sorted_dict))


# ---

# ### 55. 辞書の値でソート
print("\n55. 辞書の値でソート")
# 以下の辞書を値でソートしてください：

# ```python

scores = {"Charlie": 85, "Alice": 92, "Bob": 78}

# ```
# lambdaのxにscoresの要素がtupleとして入るので("Charlie": 85) このtupleをx[1]で戻り値として参照している。
sorted_dict = sorted(scores.items(), key=lambda x: x[1])
print(dict(sorted_dict))

# ---

# ### 56. 辞書の比較
print("\n56. 辞書の比較")
# 以下の辞書2つが等しいか確認してください：

# ```python

dict1 = {"x": 10, "y": 20}
dict2 = {"y": 20, "x": 10}

# ```

print(dict1 == dict2)
