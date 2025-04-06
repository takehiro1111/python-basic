# ### **102. 独自の例外を作成**
print("\n102. 独自の例外を作成")
# Pythonで `Exception` を継承した独自の例外 `NegativeNumberError` を作成し、
# 負の数が入力された場合に発生するようにしてください。

# ```python

# class NegativeNumberError(Exception):
#     pass

# def check_positive_number():
#     num = int(input("正の数を入力してください: "))
#     if num < 0:
#         raise NegativeNumberError("負の数は入力できません")
#     print("入力された数:", num)

# check_positive_number()

# ```

# **期待する処理:**

# - 正の数を入力すると、そのまま表示する。
# - 負の数を入力すると、`NegativeNumberError` を発生させ、「負の数は入力できません」と表示する。


class NegativeNumberError(Exception):
    pass


def check_positive_number():
    num = int(input("正の数を入力してください: "))
    if num < 0:
        raise NegativeNumberError("負の数は入力できません")
    print("入力された数:", num)


try:
    check_positive_number()
except NegativeNumberError as e:
    print(e)

# ### **103. スタックトレースを出力する**
print("\n103. スタックトレースを出力する")
# 以下のコードを修正し、`traceback` モジュールを使用して発生した例外のスタックトレースを出力してください。

# ```python
# def cause_error():
#     num1 = int(input("1つ目の数値を入力してください: "))
#     num2 = int(input("2つ目の数値を入力してください: "))
#     result = num1 / num2
#     print("結果:", result)

# try:
#     cause_error()
# except Exception as e:
#     print("エラーが発生しました。詳細:")
# 		# ここでスタックトレースを出力

# ```

# **期待する処理:**

# - `num2` に `0` を入力すると、`ZeroDivisionError` が発生し、スタックトレースが出力される。
# - 数値以外を入力すると、`ValueError` が発生し、スタックトレースが出力される。
import traceback


def cause_error():
    num1 = int(input("1つ目の数値を入力してください: "))
    num2 = int(input("2つ目の数値を入力してください: "))
    result = num1 / num2
    print("結果:", result)


try:
    cause_error()
except Exception as e:
    print(f"エラーが発生しました。詳細:\n{traceback.format_exc()}")


# ### **104. 非同期関数の基本**

# 次の `async_function` は非同期関数として定義されています。この関数を適切に実行し、
# "Hello, Async!" を出力するプログラムを作成してください。
print("\n104. 非同期関数の基本")
# ```python

# import asyncio

# async def async_function():
#     print("Hello, Async!")

# # ここに適切なコードを追加してください

# ```
import asyncio


async def async_function():
    # 学習用に意図的に3秒待機させる処理を入れています。
    await asyncio.sleep(3)
    print("Hello, Async!")


def test():
    print("test-function ")


async def main():
    test()
    await async_function()
    test()


asyncio.run(main())

# ---

# ### **105. 非同期処理の待機**
print("\n105. 非同期処理の待機")
# 次の `async_function` は `await asyncio.sleep(2)` を使用して 2 秒待機した後に
# `"Task Complete"` を出力します。この関数を適切に呼び出し、非同期処理が正しく動作することを確認してください。

# ```python

# import asyncio

# async def async_function():
#     await asyncio.sleep(2)
#     print("Task Complete")

# # ここに適切なコードを追加してください

# ```
import asyncio


async def async_function():
    await asyncio.sleep(2)
    print("Task Complete")


asyncio.run(async_function())
