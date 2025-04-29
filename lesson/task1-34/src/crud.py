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

from csv_manage import CSVManager, ImportCSVManager
from prettytable import PrettyTable
from setting import FIELDS, MENU_INPUT_MSG


class ProductManager:
    def __init__(self, csv_manager: CSVManager, import_csv_manager: ImportCSVManager):
        self.csv_manager = csv_manager
        self.import_csv_manager = import_csv_manager
        self.product_list = []
        self._product_id = 0

    #################################################
    # メニュー選択
    #################################################
    def _input_menu_num(self, attempt=3):
        if attempt == 0:
            print("再試行回数の上限を超えました。最初からやり直してください。")
            return

        try:
            menu_num = int(input(MENU_INPUT_MSG))
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
                self.csv_manager.create_csv_file(self.product_list)
                return self.choice_process()
            case 5:
                (
                    result_create_import_file,
                    csv_file_path_import,
                ) = self.import_csv_manager.create_import_csv_file(self.product_list)
                result_move_to_complete = (
                    self.import_csv_manager.move_csv_file_import_to_complete(
                        result_create_import_file, csv_file_path_import
                    )
                )
                self.import_csv_manager.delete_import_file(result_move_to_complete)
                return self.choice_process()
            case 6:
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

        for product_data in self.product_list:
            table.add_row(
                [product_data["ID"], product_data["商品名"], product_data["JANコード"]]
            )
        print(table)

        return self.choice_process()

    @get_product_data.setter
    def get_product_data(self, value):
        if value:
            self.product_list.append(value)

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

    def _generate_jan_code(self):
        random_int = str(random.randint(100000000, 999999999))
        product_id = str(self._format_product_id())
        jan_code = random_int + product_id

        return int(jan_code)

    def _template_product_data(self, id, name, jan_code):

        product_data = {
            "ID": id,
            "商品名": name,
            "JANコード": jan_code,
        }
        return product_data

    def register_product_data(self):
        self._product_id += 1
        product_id = self._format_product_id()

        input_product_name = self._input_product_name()
        jan_code = self._generate_jan_code()

        product_data = self._template_product_data(
            product_id, input_product_name, jan_code
        )
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

        for i, element in enumerate(self.product_list):
            if del_product_id == element["ID"]:
                self.product_list.pop(i)
                print(f"ID:{del_product_id}の商品データを削除しました。")
                break

        return self.choice_process()
