# ### **90. ファイル内の特定の単語の検索**
print("\n90. ファイル内の特定の単語の検索")
# `test.txt` に `"Python"` という単語が含まれているかをチェックし、
# 含まれている場合は `"単語 'Python' が見つかりました"` と出力するプログラムを書いてください。
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
test = "test"
test_dir = os.path.join(current_dir, test)
os.makedirs(test_dir, exist_ok=True)

absolute_path = os.path.join(test_dir, "test.txt")


with open(absolute_path, mode="w") as f:
    f.write("Pythonのテスト。\n 2行目")

with open(absolute_path) as f:
    data = f.read()

if "Python" in data:
    print("単語 'Python' が見つかりました")

# ### **91. ファイルの一括読み込みと逆順表示**
print("\n91. ファイルの一括読み込みと逆順表示")
# `test.txt` の内容を一括で読み込み、行を逆順に並べて表示するプログラムを書いてください。
with open(absolute_path) as f:
    data = f.readlines()

for line in reversed(data):
    print(line.strip(" "))

# ### **92. ファイルの文字数カウント**
print("\n92. ファイルの文字数カウント")
# `test.txt` の全体の文字数をカウントし、結果を出力するプログラムを書いてください。
with open(absolute_path) as f:
    data = f.read()

print(len(data))

# ### **93. ファイルの置換**
print("\n93. ファイルの置換")
# `test.txt` の中で `"Python"` という単語を `"Programming"` に置き換え、
# 新しいファイル `updated_test.txt` に保存するプログラムを書いてください。
replace_str = data.replace("Python", "Programming")

to_replace_path = os.path.join(test_dir, "updated_test.txt")

with open(to_replace_path, mode="w") as f:
    f.write(replace_str)

with open(to_replace_path) as f:
    updated_data = f.readlines()

# 改行とスペースを除去。
for line in updated_data:
    print(line.strip(" ").rstrip("\n"))
