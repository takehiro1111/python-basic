"""前提となる環境設定."""

from datetime import datetime

# 現在時刻を取得
dt_now = datetime.now()

# datetime型から文字列に変換
DATETIME_STR = dt_now.strftime("%Y%m%d%H%M%S")

FIELDS = ["ID", "商品名", "JANコード"]

MENU_INPUT_MSG = "ご希望の処理を番号で入力してください。\n(1:既存商品データの表示 / 2:商品データの新規登録 / 3:商品データの削除 / 4.CSVファイルの生成 / 5.CSVファイルのimport / 6.終了 )"
