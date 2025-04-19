"""商品の表示、登録、削除を行う機能.

# ### **1. 商品一覧表示**

# 登録されている商品のリストを以下の項目で表示します：

- ID: {商品IDのデータ}
- 商品名: {商品名}
- JANコード: {JANコード}

# ### **2. 商品登録**

# 新しい商品を登録します。

# - **商品名**: ユーザーから入力を受け付けます。
# - **JANコード**: 自動生成されます。
#     - 生成ルール: **9桁のランダムな数字** + **IDを3桁でゼロ埋めした番号**
#     - 例: 商品のIDが1の場合、JANコードは `123456789001` のようになります。

# ---

# ### **3. 商品削除**

# 指定されたIDの商品を一覧から削除します。

# - 削除する商品のIDをユーザーに入力させます。
"""

import random
import sys

from csv_manage import CSVManager
from prettytable import PrettyTable
from setting import FIELDS


class ProductManager:
    def __init__(self, csv_manager: CSVManager):
        self.csv_manager = csv_manager
        self._product_data = []
        self._product_id = 0

    #################################################
    # メニュー選択
    #################################################
    def _input_menu_num(self, attempt=3):
        if attempt == 0:
            print("再試行回数の上限を超えました。最初からやり直してください。")
            return

        try:
            menu_num = int(
                input(
                    "ご希望の処理を番号で入力してください。\n(1:既存商品データの表示 / 2:商品データの新規登録 / 3:商品データの削除 / 4.CSVファイルの生成 / 5.終了 )"
                )
            )
            return menu_num
        except TypeError:
            print("数字を入力してください。")
            self._input_menu_num(attempt - 1)

    def choice_process(self):
        menu_num: int = self._input_menu_num()

        match menu_num:
            case 1:
                return self.get_product_data
            case 2:
                return self.register_product_data()
            case 3:
                return self.delete_product_data()
            case 4:
                self.csv_manager.create_csv_file(self._product_data)
                return self.choice_process()
            case 5:
                print("商品データに対する処理を終了します。")
                sys.exit()
        return

    #################################################
    # 商品データの表示
    #################################################
    # 商品一覧表示
    @property
    def get_product_data(self):
        field_name: list[str] = FIELDS
        table = PrettyTable(field_names=field_name)

        for product_data in self._product_data:
            table.add_row(
                [product_data["ID"], product_data["商品名"], product_data["JANコード"]]
            )
        print(table)

        return self.choice_process()

    @get_product_data.setter
    def get_product_data(self, value):
        if value:
            self._product_data.append(value)

    #################################################
    # 商品データの登録
    #################################################
    # 商品データの入力
    def _input_product_name(self):
        product_name = input("商品名を入力してください。")

        return product_name

    @property
    def get_product_id(self):
        return self._product_id

    @get_product_id.setter
    def get_product_id(self, value):
        if isinstance(value, int):
            self.get_product_id = value

    # IDのフォーマット処理
    def _format_product_id(self):
        current_id = self.get_product_id
        formatted_id = f"{current_id:03d}"

        return formatted_id

    def _template_product_data(self, id, name):
        random_int = random.randint(100000000, 999999999)
        product_data = {
            "ID": id,
            "商品名": name,
            "JANコード": random_int,
        }
        return product_data

    def register_product_data(self):
        self._product_id += 1
        product_id = self._format_product_id()

        input_product_name = self._input_product_name()

        product_data = self._template_product_data(product_id, input_product_name)
        self.get_product_data = product_data
        print(self.get_product_data)

        return self.choice_process()

    #################################################
    # 商品データの削除
    #################################################
    def _get_del_product_id(self, attempt_check=3) -> int:
        if attempt_check == 0:
            print("再試行の上限を超えました。最初からやり直してください。")
            return

        product_id = input("削除する商品のIDを入力してください。")

        if not product_id.isdigit():
            print("無効な値です。数字で入力してください。")
            return self._get_del_product_id(attempt_check - 1)

        return product_id

    def delete_product_data(self):
        del_product_id = self._get_del_product_id()

        for i, element in enumerate(self._product_data):
            if del_product_id == element["ID"]:
                self._product_data.pop(i)
                print(f"ID:{del_product_id}の商品データを削除しました。")
                break

        return self.choice_process()
