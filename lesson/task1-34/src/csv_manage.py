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
import random
import re
import shutil
from datetime import datetime

from logger import logger
from setting import FIELDS


class CSVManager:
    def __init__(self):
        self.field_names: list[str] = FIELDS

    def _create_csv_dir(self):
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_dir = os.path.join(current_dir, "csv")
        os.makedirs(csv_dir, exist_ok=True)
        return csv_dir

    @staticmethod
    def _create_time_stamp():
        # 現在時刻を取得
        dt_now = datetime.now()

        # datetime型から文字列に変換
        datetime_str = dt_now.strftime("%Y%m%d%H%M%S")

        return datetime_str

    def _get_csv_file_path(self) -> str:
        csv_dir = self._create_csv_dir()
        has_datetime_now = self._create_time_stamp()
        csv_file_path = os.path.join(csv_dir, f"item_list_{has_datetime_now}.csv")

        return csv_file_path

    def create_csv_file(self, product_data):
        csv_file_path = self._get_csv_file_path()
        if product_data:
            with open(
                csv_file_path, mode="w", newline="", encoding="utf-8"
            ) as csv_file:
                field_names = self.field_names

                csv_writer = csv.writer(csv_file)

                csv_writer.writerow(field_names)

                rows = [
                    [elements["ID"], elements["商品名"], elements["JANコード"]]
                    for elements in product_data
                ]

                csv_writer.writerows(rows)

                logger.info(
                    f"CSVファイルを作成しました。再度ご希望の処理を選択してください。"
                )

                return True

        logger.warning("商品データが入力されていないためファイルを生成していません。")


class ImportCSVManager(CSVManager):
    def __init__(self):
        super().__init__()
        self.import_dir = self._create_csv_dir("import")
        self.complete_dir = self._create_csv_dir("complete")
        self._product_id = 0

    def _create_csv_dir(self, dir_name):
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        import_dir = os.path.join(current_dir, dir_name)
        os.makedirs(import_dir, exist_ok=True)
        return import_dir

    def _get_import_csv_file_path(self) -> str:
        has_datetime_now = self._create_time_stamp()
        import_csv_file_path = os.path.join(
            self.import_dir, f"import_items_{has_datetime_now}.csv"
        )

        return import_csv_file_path

    def create_import_csv_file(self, product_data):
        csv_file_path = self._get_import_csv_file_path()

        try:
            if product_data:
                with open(
                    csv_file_path, mode="w", newline="", encoding="utf-8"
                ) as csv_file:
                    field_names = self.field_names
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow(field_names)

                    rows = [
                        [elements["ID"], elements["商品名"], elements["JANコード"]]
                        for elements in product_data
                    ]

                    csv_writer.writerows(rows)

                    logger.info(f"importのCSVファイルを作成しました。")

                    return True, csv_file_path
        except PermissionError as e:
            logger.warning(f"ファイルに対する権限不足でした。:{e}")
        except OSError as e:
            logger.error(f"OS関連の一般的なエラーです。:{e}")

        logger.warning("商品データが入力されていないためファイルを生成していません。")

    def _get_complete_csv_file_path(self) -> str:
        has_datetime_now = self._create_time_stamp()
        complete_csv_file_path = os.path.join(
            self.complete_dir, f"import_items_{has_datetime_now}.csv"
        )

        return complete_csv_file_path

    def _read_import_csv_file(self):
        import_file_list = [
            file
            for file in os.listdir(self.import_dir)
            if os.path.isfile(os.path.join(self.import_dir, file))
        ]

        rows = []
        for file in import_file_list:
            with open(
                os.path.join(self.import_dir, file), encoding="utf-8", newline=""
            ) as csv_file:
                reader = csv.reader(csv_file)

                # 先頭行(ヘッダー)は処理しないよう除外する。
                # ヘッダーしかないまたは空ファイルの場合はnextを使用するとエラーになるが、そもそもimport側で空データの場合はファイルを作成しないようにしている。
                for _ in range(1):
                    next(reader)

                # 2行目以降は処理する。
                for row in reader:
                    rows.append(row)

        return rows

    def _format_product_id(self):
        current_id = self._product_id
        formatted_id = f"{current_id:03d}"

        return formatted_id

    def _generate_jan_code(self, counter=0):
        random_int = str(random.randint(100000000, 999999999))
        product_id = str(self._format_product_id())
        jan_code = random_int + product_id

        return int(jan_code) + counter

    def move_csv_file_import_to_complete(self, import_result, import_csv_file_path):
        try:
            if import_result:
                shutil.move(import_csv_file_path, self.complete_dir)
                logger.info(
                    "インポート完了後、ファイルを ./complete/ ディレクトリに移動しました。"
                )
                return True
        except FileNotFoundError as e:
            logger.error(f"import用のCSVファイルが見つかりません。: {e}")

    def _check_match_import_file(self):
        file_name_head_pattern = r"^import_.*.csv"
        import_file_list = [
            file
            for file in os.listdir(self.import_dir)
            if os.path.isfile(os.path.join(self.import_dir, file))
        ]

        result_import_file_match = all(
            re.match(file_name_head_pattern, file) for file in import_file_list
        )

        return result_import_file_match, import_file_list

    def delete_import_file(self, result_move_to_complete):
        result_has_import_file, import_file_list = self._check_match_import_file()
        try:
            if result_has_import_file and result_move_to_complete:
                for file in import_file_list:
                    os.remove(os.path.join(self.import_dir, file))
                logger.info(
                    "インポート完了後、ファイルを ./complete/ ディレクトリに移動できたためimport用ファイルを削除。"
                )
                return True

            logger.warning(
                "import側でファイルが見つからないまたはcompleteディレクトリへ移動できませんでした。"
            )
        except FileNotFoundError as e:
            logger.error(f"import用のCSVファイルが見つかりません。: {e}")
