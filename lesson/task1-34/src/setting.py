"""前提となる環境設定."""

from datetime import datetime

# 現在時刻を取得
dt_now = datetime.now()

# datetime型から文字列に変換
DATETIME_STR = dt_now.strftime("%Y%m%d%H%M%S")

FIELDS = ["ID", "商品名", "JANコード"]
