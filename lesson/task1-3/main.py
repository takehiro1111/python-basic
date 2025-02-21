### 9. for文と条件式の組み合わせ3
# 20 ~ 50までの数字の中で2で割ったら奇数となる数字のみを出力してください
print("----------9. for文と条件式の組み合わせ3--------------------")
for i in range(20, 50 + 1):
    if i % 2 == 1:
        print(i)
# ### 10. for文と条件式の組み合わせ4
# 20 ~ 50までの数字の中で2で割ったら奇数となる数字の個数を出力してください
print("----------10. for文と条件式の組み合わせ4--------------------")
odd = []
for i in range(20, 50 + 1):
    if i % 2 == 1:
        odd.append(i)
print(len(odd))

# ### 11. for文を使用した計算
# 1000未満の「3と7の倍数」は何個あるか個数を出力してください
print("----------11. for文を使用した計算--------------------")
multiples = []
for i in range(1, 1000):
    if i % 3 == 0 and i % 7 == 0:
        multiples.append(i)
print(len(multiples))

# ### 12. for文を使用した計算2
# 1000未満の「3と7の倍数」の5番目に大きい数を出力してください
print("----------12. for文を使用した計算--------------------")
multiples_fifth = []
for i in range(1, 1000):
    if i % 3 == 0 and i % 7 == 0:
        multiples_fifth.append(i)

fifth_sorted = sorted(multiples_fifth, reverse=True)
print(fifth_sorted[4])
