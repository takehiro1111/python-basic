# ### **106. 非同期タスクの並列実行**

# 以下の2つの非同期関数 `task1` と `task2` を並行して実行し、
# それぞれ `"Task 1 Completed"` と `"Task 2 Completed"` を出力するプログラムを作成してください。
print("\n106. 非同期タスクの並列実行")
# ```python

# import asyncio

# async def task1():
#     await asyncio.sleep(1)
#     print("Task 1 Completed")

# async def task2():
#     await asyncio.sleep(2)
#     print("Task 2 Completed")

# # ここに適切なコードを追加してください

# ```
import asyncio


async def task1():
    await asyncio.sleep(3)
    print("Task 1 Completed")


async def task2():
    await asyncio.sleep(1)
    print("Task 2 Completed")


async def main():
    task_1 = asyncio.create_task(task1())
    task_2 = asyncio.create_task(task2())

    await task_1
    await task_2


asyncio.run(main())


# ---

# ### **107. 非同期処理のキャンセル**
print("\n107. 非同期処理のキャンセル")
# 次の `async_task` は 5 秒間待機した後に `"Task Finished"` を出力します。
# しかし、実行開始から 2 秒後にタスクをキャンセルするようにしてください。

# ```python
import asyncio


async def async_task():
    try:
        await asyncio.sleep(5)
        print("Task Finished")
    except asyncio.CancelledError:
        print("Task Cancelled")


# # ここに適切なコードを追加してください
async def main():
    task = asyncio.create_task(async_task())
    await asyncio.sleep(2)
    task.cancel()


asyncio.run(main())

# ```

# ---

# ### **108. 非同期関数の結果を取得**
print("\n108. 非同期関数の結果を取得")
# 次の `async_function` は `await asyncio.sleep(1)` の後に `"Done"` を返します。
# この関数を呼び出し、結果を変数 `result` に格納して表示するプログラムを作成してください。

# ```python
# import asyncio


async def async_function():
    await asyncio.sleep(1)
    return "Done"


# # ここに適切なコードを追加してください
async def invoke_async_function():
    result = await async_function()
    print(result)


asyncio.run(invoke_async_function())

# ```

# ---

# ### **109. デコレータの基本**
print("\n109. デコレータの基本")
# 次の `my_decorator` は関数の前後で `"Start"` と `"End"` を出力するデコレータです。
# このデコレータを `hello` 関数に適用し、 `"Hello, Decorator!"` の前後に `"Start"` と
# `"End"` が表示されるようにしてください。


# ```python
def my_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")

    return wrapper


# ここに適切なコードを追加してください
@my_decorator
def hello():
    print("Hello, Decorator!")


hello()

# ```

# **期待される出力**

# ```
# Start
# Hello, Decorator!
# End

# ```
