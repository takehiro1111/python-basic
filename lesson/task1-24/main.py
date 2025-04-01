# ### **82. ファイルの作成**
print("\n82. ファイルの作成")
# 新しいテキストファイル `test.txt` を作成し、その中に `"Hello, Python!"` という文字列を
# 書き込むプログラムを書いてください。
# from pathlib import Path

# path = Path("test/test.txt")
# absolute_path = path.resolve()
import os

file_dir = os.path.dirname(os.path.abspath(__file__))
print(file_dir)

with open(f"{file_dir}/test.txt", mode="w") as f:
    f.write("Hello, Python!")

# ### **83. ファイルの読み込み**
print("\n83. ファイルの読み込み")
# 問題 82 で作成した `test.txt` を開き、内容を読み取って出力するプログラムを書いてください。
with open(f"{file_dir}/test.txt") as f:
    read = f.read()

print(read)

# ### **84. ファイルの追記**
print("\n84. ファイルの追記")
# `test.txt` に `"Welcome to file handling in Python."` という一文を追加で書き込むプログラムを書いてください。
# その後、ファイルの内容をすべて出力してください。
with open(f"{file_dir}/test.txt", mode="a") as f:
    f.write("\nWelcome to file handling in Python.")

with open(f"{file_dir}/test.txt") as f:
    read = f.read()

print(read)

# ### **85. ファイルの行ごとの読み込み**
print("\n85. ファイルの行ごとの読み込み")
# `test.txt` の内容を1行ずつ読み取り、各行をリストに格納し、そのリストを出力するプログラムを書いてください。
with open(f"{file_dir}/test.txt") as f:
    lines_rstrip = [line.rstrip("\n") for line in f]
    print(lines_rstrip)
