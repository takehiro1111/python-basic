### 36. タプルからリストへの変換

# タプル `(1, 2, 3, 4, 5)` をリストに変換し、逆順にして表示してください。
print("\n36.タプルからリストへの変換")

sample_tuple = (1, 2, 3, 4, 5)
to_list = sorted(list(sample_tuple), reverse=True)
print(to_list)

### 37. リストからタプルへの変換
# リスト `[10, 20, 30, 40, 50]` をタプルに変換し、表示してください。
print("\n37.リストからタプルへの変換")

sample_list = [10, 20, 30, 40, 50]
to_tuple = tuple(sample_list)
print(to_tuple)

# ### 38. 三項演算子１
print("\n38.三項演算子１")
# ランダムに生成された整数を持つ変数を宣言し、その変数の値が偶数であれば "even"、奇数であれば "odd" と出力するプログラムを、
# 三項演算子を使って作成してください。
import secrets

random_num = secrets.randbelow(1000)
print("even" if random_num % 2 == 0 else "odd")


# ### 39. 標準入力
print("\n39.標準入力")
# 次の仕様に従って、ユーザーの名前と年齢を入力し、最終的なメッセージを出力するプログラムを作成してください。

# 1. プログラムは「あなたの名前を教えてください。」というメッセージを出力し、ユーザーから名前の入力を受け付けます。
# 2. 名前を入力すると、「〇〇さん、あなたの年齢は何歳ですか？」というメッセージが出力され、ユーザーから年齢の入力を受け付けます。
# 3. 最後に、「〇〇さん（年齢:〇〇）、ご登録ありがとうございます！」というメッセージを出力して、プログラムを終了します。


def validate_name(user_name):
    return 1 <= len(user_name) <= 10


def validate_age(user_age):
    return user_age.isdigit()


def success_message(user_name, user_age):
    print(f"{user_name}さん（年齢:{user_age}）、ご登録ありがとうございます！")
    return True


def input_name():
    name = input("あなたの名前を教えてください。")
    if not validate_name(name):
        return input_name()

    return name


def input_age(user_name):
    age = input(f"{user_name}さん、あなたの年齢は何歳ですか？")
    if not validate_age(age):
        return input_age(age)

    return age


def main():
    name = input_name()
    age = input_age(name)

    return success_message(name, age)


if __name__ == "__main__":
    main()


# ### バリデーション

# 名前
# ・空でないこと
# ・10文字以内

# 年齢
# ・空でないこと
# ・数字であること

# ### 入出力例

# ### 入力例 1

# ```

# Micael
# 20
# ```

# ### 出力例 1

# ```makefile

# あなたの名前を教えてください。
# Micaelさん、あなたの年齢は何歳ですか？
# Micaelさん（年齢:20）、ご登録ありがとうございます！

# ```
