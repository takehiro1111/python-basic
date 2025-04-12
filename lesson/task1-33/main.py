# ### **118. 無限ジェネレータ**
print("\n118. 無限ジェネレータ")
# `infinite_counter` は 1 から始まり、無限に 1 ずつ増加するジェネレータです。
# このジェネレータを使い、最初の 5 つの値を出力してください。


# ```python
def infinite_counter():
    num = 1
    while True:
        yield num
        num += 1


gen = infinite_counter()

for i in range(5):
    print(next(gen))

# ```

# **期待される出力**

# ```
# 1
# 2
# 3
# 4
# 5

# ```

# ---

# ### **119. send() メソッドを使ったジェネレータ**
print("\n119. send() メソッドを使ったジェネレータ")
# 次の `custom_counter` は `send()` を使用してカウントを変更できます。
# 最初は 0 から始まり、`send()` で渡された値に更新されます。
# 最初の 3 回は通常の `next()` で実行し、その後 `send(10)` を使ってカウントを 10 に変更し、
# さらに 2 回 `next()` を実行してください。


# ```python
def custom_counter():
    count = 0
    while True:
        received = yield count
        if received is not None:
            count = received
        else:
            count += 1


gen = custom_counter()

for i in range(3):
    print(next(gen))

print(gen.send(10))
print(next(gen))


# ```

# **期待される出力**

# ```
# 0
# 1
# 2
# 10
# 11

# ```

# ---

# ### **120. ジェネレータの例外処理**
print("\n120. ジェネレータの例外処理")
# 次の `error_handling_generator` は `yield` で数値を返しますが、`throw(ValueError)` を呼び出すと
# `"ValueError caught!"` と表示され、処理を継続します。
# このジェネレータを実行し、`throw(ValueError)` を使って例外を発生させた後、さらに `next()` を呼び出してください。


# ```python
def error_handling_generator():
    count = 0
    while True:
        try:
            yield count
            count += 1
        except ValueError:
            print("ValueError caught!")


gen = error_handling_generator()

print(next(gen))
print(next(gen))
gen.throw(ValueError)
print(next(gen))


# ```

# **期待される出力**

# ```
# 0
# 1
# ValueError caught!
# 2

# ```
