# ### **98. バイナリファイルの読み書き**
print("\n98. バイナリファイルの読み書き")
# 新しいバイナリファイル `binary.dat` を作成し、バイトデータ `b'\x48\x65\x6C\x6C\x6F'` を書き込むプログラムを書いてください。
# その後、ファイルを読み取り、内容を出力してください。
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
bin = "bin"
bin_dir = os.path.join(current_dir, bin)
os.makedirs(bin_dir, exist_ok=True)

data_bin_path = os.path.join(bin_dir, "binary.dat")
b_str = b"\x48\x65\x6C\x6C\x6F"

with open(data_bin_path, mode="wb") as bin_file:
    bin_file.write(b_str)

with open(data_bin_path, mode="rb") as bin_file:
    bin_read = bin_file.read()
    bin_decode = bin_read.decode()
    print(bin_decode)


# ### **99. 例外処理の基本**
# 以下のコードを実行したときに発生する例外をtry-except文を使って適切に処理してください。
print("\n99. 例外処理の基本")
# ```python

# num = int(input("数値を入力してください: "))
# result = 100 / num
# print("結果:", result)

# ```

# **期待する処理:**

# - `num` に `0` を入力した場合は、ゼロ除算の例外を適切に処理する。
# - `num` に数値以外の値を入力した場合は、`ValueError` を適切に処理する。

# ---

try:
    num = int(input("数値を入力してください: "))
    result = 100 / num
    print("結果:", result)
except ZeroDivisionError as e:
    print(f"{num}より大きい数字を入力してください。\n{e}")
except ValueError as e:
    print(f"整数を入力してください。\n{e}")


# ### **100. 複数の例外の処理**
print("\n100. 複数の例外の処理")
# 以下のコードを修正し、複数の異なる例外 (`ZeroDivisionError` や `ValueError`) を個別に処理してください。

# ```python

# def divide_numbers():
#     num1 = int(input("1つ目の数値を入力してください: "))
#     num2 = int(input("2つ目の数値を入力してください: "))
#     result = num1 / num2
#     print("結果:", result)

# divide_numbers()

# ```

# **期待する処理:**

# - `num2` に `0` を入力した場合は「ゼロで割ることはできません」と表示する。
# - 数値以外を入力した場合は「無効な入力です」と表示する。


# ---
def divide_numbers():
    try:
        num1 = int(input("1つ目の数値を入力してください: "))
        num2 = int(input("2つ目の数値を入力してください: "))
        try:
            result = num1 / num2
            print("結果:", result)
        except ZeroDivisionError:
            print("ゼロで割ることはできません")

    except ValueError:
        print("無効な入力です")


divide_numbers()

# ### **101. try-except-finally の活用**
print("\n101. try-except-finally の活用")
# 以下のコードを修正し、`finally` ブロックを追加して、処理の最後に「処理が終了しました」と表示してください。

# ```python

# def open_file():
#     file_name = input("開くファイル名を入力してください: ")
#     file = open(file_name, "r")
#     content = file.read()
#     print(content)
#     file.close()

# open_file()

# ```

# **期待する処理:**

# - 存在しないファイルを開こうとした場合は `FileNotFoundError` を処理し、「ファイルが見つかりません」と表示する。
# - `finally` ブロックで「処理が終了しました」と表示する。


def open_file():
    file_name = input("開くファイル名を入力してください: ")
    try:
        file = open(file_name)
        content = file.read()
        print(content)
        file.close()
    except FileNotFoundError:
        print("ファイルが見つかりません")
    finally:
        print("処理が終了しました")


open_file()
