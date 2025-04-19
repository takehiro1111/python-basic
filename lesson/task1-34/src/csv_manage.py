"""CSVファイルの出力.
### **4. 商品CSV出力**

現在登録されている商品一覧をCSVファイルとして出力します。

- 出力先: `./csv/item_list_{現在時刻}.csv`
    - 例: `./csv/item_list_20250113123045.csv`
- ファイルに含まれる項目:
    - **ID**
    - **商品名**
    - **JANコード**
"""

import csv
import os

from setting import DATETIME_STR, FIELDS


class CSVManager:
    def __init__(self):
        self.field_names: list[str] = FIELDS

    def _create_csv_dir(self):
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_dir = os.path.join(current_dir, "csv")
        os.makedirs(csv_dir, exist_ok=True)
        return csv_dir

    def _get_csv_file_path(self) -> str:
        csv_dir = self._create_csv_dir()
        has_datetime_now = DATETIME_STR
        csv_file_path = os.path.join(csv_dir, f"item_list_{has_datetime_now}.csv")

        return csv_file_path

    def create_csv_file(self, product_data):
        csv_file_path = self._get_csv_file_path()
        with open(csv_file_path, mode="w", newline="", encoding="utf-8") as csv_file:
            field_names = self.field_names
            csv_writer = csv.writer(csv_file)

            csv_writer.writerow(field_names)

            row = [
                element for elements in product_data for element in elements.values()
            ]

            csv_writer.writerow(row)

            print("CSVファイルを作成しました。再度ご希望の処理を選択してください。")

            return True
