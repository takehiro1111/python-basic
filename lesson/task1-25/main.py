# ### **86. ファイルの存在チェック**

# Pythonを使って `test.txt` が存在するかどうかを確認し、存在する場合は `"ファイルが存在します"`、
# 存在しない場合は `"ファイルが見つかりません"` と出力するプログラムを書いてください。
import os

file_dir = os.path.dirname(os.path.abspath(__file__))
file_path = f"{file_dir}/test.txt"

with open(file_path, "w"):
    pass

is_file = os.path.isfile(file_path)

if is_file:
    print("ファイルが存在します")
elif is_file is False:
    print("ファイルが見つかりません")

# ### **87. ファイルの削除**
# `test.txt` を削除するプログラムを書いてください。
# 'ただし、削除前にファイルの存在を確認し、存在する場合のみ削除するようにしてください。
# if is_file:
#   os.remove(file_path)

# ### **88. ファイルのコピー**
# `test.txt` の内容を `copy_test.txt` にコピーするプログラムを書いてください。
import shutil

# ファイル作成
with open(file_path, "w") as f:
    file = f.write("コピー処理用のファイルです。")


copy_dist_file = f"{file_dir}/copy_test.txt"

if is_file:
    shutil.copyfile(file_path, copy_dist_file)

# ### **89. ファイルの行数カウント**
# `test.txt` の行数をカウントし、結果を出力するプログラムを書いてください。
with open(file_path) as f:
    lines = f.readlines()

print(f"行数:{len(lines)}")
