## 自作関数
l = [1, 2, 3, 4, 5]


# 最大値-------------------------
def max_num(lst=l):
    max_element = lst[0]
    for i in lst:
        if i > max_element:
            max_element = i

    return max_element


max = max_num()
print(max)


# 最小値-------------------------
def min_num(lst=l):
    min_element = lst[0]
    for i in lst:
        if i < min_element:
            min_element = i

    return min_element


min = min_num()
print(min)


# 合計-------------------------
def total_num(lst=l):
    total_element = 0
    for i in lst:
        total_element += i

    return total_element


total = total_num()
print(total)


## 以下は生成AIに出して貰ってます。
def bubble_sort(arr):
    """
    バブルソート
    隣接する要素を比較して入れ替えを繰り返す
    時間複雑度: O(n²)
    """
    n = len(arr)
    # リストのコピーを作成して元のリストを変更しないようにする
    result = arr.copy()

    for i in range(n):
        # 各パスで最も大きい要素が右端に移動するので、
        # 内側のループでは未ソートの部分のみを見る
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                # 大きい要素を右に移動
                result[j], result[j + 1] = result[j + 1], result[j]

    return result


def selection_sort(arr):
    """
    選択ソート
    未ソート部分から最小値を選んで、ソート済み部分の末尾に追加する
    時間複雑度: O(n²)
    """
    n = len(arr)
    result = arr.copy()

    for i in range(n):
        # 未ソート部分の最小値のインデックスを探す
        min_idx = i
        for j in range(i + 1, n):
            if result[j] < result[min_idx]:
                min_idx = j

        # 最小値を未ソート部分の先頭と交換
        result[i], result[min_idx] = result[min_idx], result[i]

    return result


def insertion_sort(arr):
    """
    挿入ソート
    ソート済み部分に新しい要素を適切な位置に挿入する
    時間複雑度: O(n²)
    """
    n = len(arr)
    result = arr.copy()

    for i in range(1, n):
        key = result[i]
        j = i - 1

        # keyより大きい要素は右にずらす
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1

        # 適切な位置にkeyを挿入
        result[j + 1] = key

    return result


def merge_sort(arr):
    """
    マージソート
    分割統治法を使用する
    時間複雑度: O(n log n)
    """
    if len(arr) <= 1:
        return arr.copy()

    # リストを分割
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # マージ
    return merge(left, right)


def merge(left, right):
    """
    ソート済みの2つのリストをマージする
    """
    result = []
    i = j = 0

    # 両方のリストからより小さい要素を取り出す
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 残りの要素を追加
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def quick_sort(arr):
    """
    クイックソート
    分割統治法を使用する
    時間複雑度: 平均 O(n log n)、最悪 O(n²)
    """
    if len(arr) <= 1:
        return arr.copy()

    result = arr.copy()
    _quick_sort_helper(result, 0, len(result) - 1)
    return result


def _quick_sort_helper(arr, low, high):
    if low < high:
        # 分割インデックスを取得
        pi = partition(arr, low, high)

        # 分割インデックスの前後をソート
        _quick_sort_helper(arr, low, pi - 1)
        _quick_sort_helper(arr, pi + 1, high)


def partition(arr, low, high):
    # ピボットとして最後の要素を選択
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        # ピボット以下の要素を左側に集める
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # ピボットを正しい位置に配置
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# テスト
if __name__ == "__main__":
    test_arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(f"元のリスト: {test_arr}")
    print(f"バブルソート: {bubble_sort(test_arr)}")
    print(f"選択ソート: {selection_sort(test_arr)}")
    print(f"挿入ソート: {insertion_sort(test_arr)}")
    print(f"マージソート: {merge_sort(test_arr)}")
    print(f"クイックソート: {quick_sort(test_arr)}")
