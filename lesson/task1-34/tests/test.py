import csv
import os
import random

from prettytable import PrettyTable


def display_products(field_name, row_data) -> None:
    """商品一覧の表形式での表示 (prettytable使用)"""
    if not row_data:
        print("登録されている商品はありません。")
        return

    # テーブルの作成
    table = PrettyTable(field_names=field_name)

    # データの追加
    for product in row_data:
        table.add_row(product)

    print("\n===== 商品一覧 =====")
    print(table)


current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)


csv_file_path = os.path.join(current_dir, "test.csv")
print(csv_file_path)

with open(csv_file_path, newline="") as csv_file:
    header_name = next(csv.reader(csv_file, delimiter=","))
    csv_reader = csv.reader(csv_file, delimiter=",")
    print(header_name)

    data_list = []
    for row in csv_reader:
        print("@".join(row))
        data_list.append(row)

print(data_list)

display_products(header_name, data_list)
