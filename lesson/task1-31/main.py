# ### **110. デコレータの引数付き関数**
print("\n110. デコレータの引数付き関数")
# デコレータ `my_decorator` を修正し、引数を持つ関数 `greet` に適用してください。
# デコレータは `"Calling function..."` を出力した後、関数を実行するようにしてください。
import asyncio


# ```python
def my_decorator(func):
    async def wrapper(*args):
        print("Calling function...")
        await asyncio.sleep(3)
        await func(*args)

    return wrapper


@my_decorator
async def greet(name):
    print(f"Hello, {name}!")


asyncio.run(greet("Alice"))


# ```

# **期待される出力**

# ```
# Calling function...
# Hello, Alice!

# ```

# ---

# ### **111. 複数のデコレータ**
print("\n111. 複数のデコレータ")
# 以下の `uppercase_decorator` は関数の出力を大文字に変換し
# `exclamation_decorator` は末尾に `"!"` を追加するデコレータです。
# これらを `greet` 関数に適用し、 `"hello"` を `"HELLO!"` に変換するプログラムを作成してください。


# ```python
def uppercase_decorator(func):
    def wrapper():
        result = func()
        if isinstance(result, str):
            return result.upper()

    return wrapper


def exclamation_decorator(func):
    def wrapper():
        result = func()
        if isinstance(result, str):
            return result + "!"

    return wrapper


@uppercase_decorator
@exclamation_decorator
def greet():
    return "hello"


print(greet())

# ```

# **期待される出力**

# ```
# HELLO!

# ```

# ---

# ### **112. デコレータで関数の実行時間を計測**
print("\n112. デコレータで関数の実行時間を計測")
# 以下の `timer_decorator` を完成させ、関数の実行時間を測定できるようにしてください。

# ```python
import time


def timer_decorator(func):
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        print(f"Elapsed time: {end_time - start_time:.2f} seconds")
        return result

    return wrapper


@timer_decorator
def slow_function():
    time.sleep(2.0)
    print("Function executed")


slow_function()

# ```

# **期待される出力（例）**

# ```
# Function executed
# Execution time: 2.00 seconds

# ```

# ---

# ### **113. クラスベースのデコレータ**
print("\n113. クラスベースのデコレータ")
# クラスを使ってデコレータを作成し、関数が実行されるたびに
# `"Function executed"` と表示されるようにしてください。


# ```python
class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Function executed")
        self.func()


@MyDecorator
def say_hello():
    print("Hello, world!")


say_hello()

# ```

# **期待される出力**

# ```
# Function executed
# Hello, world!

# ```
