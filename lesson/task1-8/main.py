# ### 28. キーワード引数

print("\n28.キーワード引数")
# 幅と高さを受け取り、長方形の面積を計算して返す関数 `calculate_area` を定義してください。
# 関数呼び出し時にキーワード引数を使って幅 `5`、高さ `10` で計算した結果を表示してください。
def calculate_area(width=5, height=10):
    return width * height


area = calculate_area()
print(area)


# ### 29. 可変長引数
print("\n29.可変長引数")
# 複数の整数を受け取り、それらの合計を返す関数 `sum_all` を定義してください。その後、関数を使って `1, 2, 3, 4, 5` の合計を表示してください。

def sum_all(*args):
    return sum(args)


total = sum_all(1, 2, 3, 4, 5)
print(total)

# ### 30. タプルの作成とアクセス
print("\n30.タプルの作成とアクセス")
# タプル `(1, 2, 3, 4, 5)` を作成し、タプルの最初の要素と最後の要素を表示してください。
sample_tuple = (1, 2, 3, 4, 5)
print(sample_tuple[0])
print(sample_tuple[-1])

# ### 31. タプルの要素の確認
print("\n 31.タプルの要素の確認")
# タプル `(10, 20, 30, 40, 50)` に `30` が含まれているかどうかを確認するコードを書いてください。
sample_tuple = (10, 20, 30, 40, 50)
print(30 in sample_tuple)
