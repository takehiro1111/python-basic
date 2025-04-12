# ### **114. ジェネレータの基本**
print("\n114. ジェネレータの基本")
# 次の `simple_generator` は `yield` を使用して `"Hello"` と `"Generator"` を順番に返します。
# このジェネレータを適切に呼び出し、出力を確認してください。


# ```python
def simple_generator():
    yield "Hello"
    yield "Generator"


gen = simple_generator()

print(next(gen))
print(next(gen))

# ```

# **期待される出力**

# ```
# Hello
# Generator

# ```

# ---

# ### **115. ジェネレータの next() メソッド**
print("\n115. ジェネレータの next() メソッド")
# 次の `counter` ジェネレータは `start` から `end` までの数値を 1 ずつ `yield` します。
# このジェネレータを `next()` を使って 3 回実行し、それぞれの値を出力してください。


# ```python
def counter(start, end):
    while start <= end:
        yield start
        start += 1


gen = counter(1, 5)

print(next(gen))
print(next(gen))
print(next(gen))

# ```

# **期待される出力**

# ```
# 1
# 2
# 3

# ```

# ---

# ### **116. for ループを使ったジェネレータの実行**
print("\n116. for ループを使ったジェネレータの実行")
# 次の `even_numbers` ジェネレータは 0 から `n` までの偶数を `yield` します。
# このジェネレータを `for` ループを使って実行し、出力してください。


# ```python
def even_numbers(n):
    yield from range(0, n + 1, 2)


gen = even_numbers(6)

for i in range(4):
    print(next(gen))

# ```

# **期待される出力（n=6 の場合）**

# ```
# 0
# 2
# 4
# 6

# ```

# ---

# ### **117. ジェネレータ式**
print("\n117. ジェネレータ式")
# リスト `[1, 2, 3, 4, 5]` を元に、各要素の 2 倍を `yield` するジェネレータ式を作成し、`
# for` ループで出力してください。

# ```python
numbers = [1, 2, 3, 4, 5]


def to_double_nums(nums: list[int]):
    for num in nums:
        yield num * 2


gen = to_double_nums(numbers)

for i in range(len(numbers)):
    print(next(gen))

# ```

# **期待される出力**

# ```
# 2
# 4
# 6
# 8
# 10

# ```
