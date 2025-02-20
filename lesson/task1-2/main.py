### 5. for文の基礎
print("5.for文の基礎")
# 1~10までの数字をfor文を使って出力してください
for i in range(1, 11):
    print(i)

### 6. for文の基礎２
print("6.for文の基礎")
# 35 ~ 46までの数字をfor文を使って出力してください
for i in range(35, 47):
    print(i)

### 7.for文と条件式の組み合わせ
print("7.for文と条件式の組み合わせ")
# 40 ~ 50までの数字の中で奇数の数字のみを出力してください
print("Pattern1-------------------------------------------")
odd_list = [i for i in range(40, 51) if i % 2 == 1]
for i in odd_list:
    print(i)

print("Pattern2-------------------------------------------")
for i in range(40, 51):
    if i % 2 == 1:
        print(i)

### 8. for文と条件式の組み合わせ2
print("8.for文と条件式の組み合わせ2")
# 10 ~ 25までの数字の中で3の倍数の数字のみを出力してください
print("Pattern1-------------------------------------------")
three_multiple_1 = [i for i in range(18, 26) if i % 3 == 0]
for i in three_multiple_1:
    print(i)

print("Pattern2-------------------------------------------")
three_multiple_2 = [i for i in range(18, 26, 3)]
for i in three_multiple_2:
    print(i)
