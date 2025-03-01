### 24. 基本的な関数の定義と呼び出し
print("24.基本的な関数の定義と呼び出し-------------------------")


# 2つの整数を受け取り、その和を返す関数 `add` を定義してください。
def add(num1: int, num2: int) -> int:
    return num1 + num2


# その後、関数を使って `3` と `5` の和を表示してください。
total = add(3, 5)
print(total)

### 25. 関数の引数と返り値
print("25.関数の引数と返り値し------------------------------")


# 1つの整数を受け取り、その値が偶数か奇数かを判定して文字列 "even" または "odd" を返す関数
# `even_or_odd` を定義してください。
def even_or_odd(num: int) -> str:
    if num % 2 == 0:
        return "even"
    elif num % 2 == 1:
        return "odd"


# その後、関数を使って `4` と `7` の結果を表示してください。
even = even_or_odd(4)
print(even)
odd = even_or_odd(7)
print(odd)

### 26. 複数の引数
print("26.複数の引数------------------------------------")
# 3つの文字列を受け取り、それらをスペースで連結して返す関数 `concatenate_strings` を定義してください。
# その後、関数を使って "Hello", "world", "!" を連結した結果を表示してください。
print("パターン1----------------------------------")


def concatenate_strings1(str1: str, str2: str, str3: str) -> str:
    return " ".join(str1 + str2 + str3)


result1 = concatenate_strings1("Hello", "world", "!")
print(result1)

print("パターン2----------------------------------")


def concatenate_strings2(str1: str, str2: str, str3: str) -> str:
    return f"{str1} {str2} {str3}"


result2 = concatenate_strings2("Hello", "world", "!")
print(result2)

### 27. デフォルト引数
print("27.デフォルト引数----------------------------------")


# 名前を受け取って "Hello, [名前]!" というメッセージを返す関数 `greet` を定義してください。
def greet(name="Guest") -> str:
    return f"Hello, {name}!"


# 名前が指定されない場合は "Hello, Guest!" というメッセージを返すようにしてください。
say_hello = greet()
print(say_hello)
