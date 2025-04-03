### **94. ファイルのCSV読み込み**
print("\n94.ファイルのCSV読み込み")
# 新しいCSVファイル `data.csv` を作成し、以下のデータを書き込み、
# その後CSVファイルを読み込んで出力するプログラムを書いてください。
# ```
# コピーする編集する
# Name,Age,Country
# Alice,25,USA
# Bob,30,UK
# Charlie,35,Canada

import csv
import os

human_info = [
    {"Name": "Alice", "Age": 25, "Country": "USA"},
    {"Name": "Bob", "Age": 30, "Country": "UK"},
    {"Name": "Charlie", "Age": 35, "Country": "Canada"},
]

current_dir = os.path.dirname(os.path.abspath(__file__))
data = "data"
data_dir = os.path.join(current_dir, data)
os.makedirs(data_dir, exist_ok=True)

data_csv_path = os.path.join(data_dir, "data.csv")
with open(data_csv_path, mode="w", newline="") as csv_file:
    # ヘッダ行
    fieldnames = ["Name", "Age", "Country"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # ヘッダ行を書き込む
    writer.writeheader()

    # 各行の書き込み。
    for row in human_info:
        writer.writerow(row)

# 読み込みと出力
with open(data_csv_path) as csv_file:
    csv_data = csv_file.read()
    print(csv_data)

# ```

# ### **95. CSVファイルのデータ抽出**
print("\n95. CSVファイルのデータ抽出")
# `data.csv` から `"Age"` 列の値をすべて取得し、平均年齢を計算して出力するプログラムを書いてください。
age_list = []
with open(data_csv_path) as csv_file:
    dataReader = csv.reader(csv_file)
    for row in dataReader:
        if row[1].isdigit():
            has_int_age = int(row[1])
            age_list.append(has_int_age)


def avg_age(nums: list[int]) -> int:
    total = 0
    for num in nums:
        total += num

    return total // len(nums)


print(f"3人の平均年齢:{avg_age(age_list)}")

# ### **96. JSONファイルの作成と読み込み**
print("\n96. JSONファイルの作成と読み込み")
# Pythonの辞書データをJSONファイル `data.json` に保存し、その後JSONファイルを読み込んで出力するプログラムを書いてください。

# 辞書データ：

# ```python
# python
# コピーする編集する
# {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York"
# }
import json

dict_data = {"name": "Alice", "age": 25, "city": "New York"}

data_json_path = os.path.join(data_dir, "data.json")

# dump(dict -> json)
with open(data_json_path, mode="w") as json_file:
    dict_to_json = json.dump(dict_data, json_file)

# load(json -> dist)
with open(data_json_path) as json_file:
    json_to_dict = json.load(json_file)
    print("更新前:", json_to_dict)

# ### **97. JSONデータの更新**
print("\n97. JSONデータの更新")

# `data.json` の `"age"` を `30` に更新し、変更後のJSONデータを出力するプログラムを書いてください。

# データの更新
json_to_dict["age"] = 30

with open(data_json_path, mode="w") as json_file:
    dict_to_json = json.dump(json_to_dict, json_file)

with open(data_json_path) as json_file:
    json_to_dict = json.load(json_file)
    print("更新後:", json_to_dict)
