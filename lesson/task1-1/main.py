"""task1-1."""

# 1. 基本的な変数の宣言
# 以下の指定された条件に合うような値を変数に代入して宣言してください。
# また宣言した変数を出力してください。

# 整数（int） number: 5
number: int = 5
# 文字列（string） text: "test"
text: str = "test"
# 論理型（boolean） flag: a

flag: bool = True
# None型 test: None
test: None = None
# 浮動小数点数（float） pi: 3.14
pi: float = 3.14

# 2. 基本的な計算
# 整数型の2つの変数を宣言してください。2つの変数を用いて、足す、引く、かける、割る、割った余りを出力してください。
num_1 = 3
num_2 = 5

total = num_1 + num_2
print("2-1.足す", total)

difference = num_1 - num_2
print("2-2.引く", difference)

product = num_1 * num_2
print("2-3.かける", product)

quotient = num_1 / num_2
print("2-4.割る", quotient)

remainder = num_1 % num_2
print("2-5.余り", remainder)

# 3. 条件式と論理型（boolean）について
# 初期値がFalseである論理型の変数を宣言してください。
# 問題2で宣言した2つの変数を足した結果が偶数であれば、論理型の変数にTrueを代入してください。
is_even = False
if total % 2 == 0:
    is_even = True
print("3.条件式と論理型（boolean）", is_even)

# 4. 条件式
# 設問3のboolean型の変数を利用した条件式を作成し、以下のように出力してください。
# 偶数なら「偶数です」
# 奇数なら「奇数です」
if is_even:
    print("4.条件式", "偶数です")
else:
    print("4.条件式", "奇数です")
