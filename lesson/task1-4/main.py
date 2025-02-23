### 13, 図形の表示

# 0
# 00
# 000

# この図形をfor文を使って出力してください。

print("-------------13.図形の表示------------------")
shape = str(0)

for i in range(1, 3 + 1):
    print(shape * i)

### 14, 図形の表示

# 0
# 000
# 00000

# この図形をfor文を使って出力してください。
print("-------------14.図形の表示------------------")
shape = str(0)

for i in range(1, 5 + 1, 2):
    print(shape * i)

### 15, 図形の表示

# 0
# 000
# 00000
# 000
# 0

# この図形をfor文を使って出力してください。
print("-------------15.図形の表示------------------")

""" パターン1 """
shape = str(0)

for i in range(1, 5 + 1, 2):
    asc = shape * i
    print(asc)

for j in reversed(range(1, 3 + 1, 2)):
    desc = shape * j
    print(desc)

print("-------------------------------")

""" パターン2 """


def loop(start, stop, width):
    l = []
    for i in range(start, stop, width):
        nums = shape * i
        l.append(nums)

    return l


asc = loop(1, 5 + 1, 2)
desc = loop(1, 3 + 1, 2)

for i in asc:
    print(i)

for i in reversed(desc):
    print(i)
