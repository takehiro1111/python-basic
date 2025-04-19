# ## 商品マスター登録プログラムを作成する

# 以下の仕様を満たすプログラムを作成してください。

# ### メインメニュー

# ユーザーに以下の選択肢を提示し、対応する機能を実行するプログラムを作成します：

# 1. **商品一覧表示**
# 2. **商品登録**
# 3. **商品削除**
# 4. **商品CSV出力**
# 5. **終了**
# ---
from crud import ProductManager
from csv_manage import CSVManager


def main():
    csv_manager = CSVManager()
    product_manager = ProductManager(csv_manager)
    product_manager.choice_process()

    return


if __name__ == "__main__":
    main()
