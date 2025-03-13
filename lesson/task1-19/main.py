### 65. クラス内で別のクラスを使用する


# `Engine`というクラスを作成し、以下の属性を持たせてください:
# - `horsepower`: 整数
class Engine:
    def __init__(self, horsepower: int) -> None:
        self.horsepower = horsepower


# 次に`Car`クラスを作成し、`Engine`クラスのインスタンスを`engine`属性として持たせてください。
# `Car`クラスの`get_engine_power`というメソッドで`horsepower`を返すようにしてください。
class Car(Engine):
    def __init__(self, horsepower: int) -> None:
        self.engine = Engine(horsepower)

    def get_engine_power(self):
        return self.engine.horsepower


car = Car(20)
print(car.get_engine_power())


# ### 66. クラス変数の使用
# `Student`クラスを作成し、`name`（文字列）と`score`（整数）の属性を持たせてください。
# また、全体の生徒数をカウントするためのクラス変数`student_count`を追加してください。
# インスタンスが作成されるたびに`student_count`が1増えるようにしてください。
class Student:
    # クラス変数
    student_count = 0

    def __init__(self, name, score):
        self.name = name
        self.score = score
        Student.student_count += 1

    def count(self):
        return Student.student_count


# クラスインスタンス
student = Student("takehiro1111", 80)
print(Student.student_count)

student2 = Student("sato", 100)
print(Student.student_count)


# ### 67. プロパティの使用
# `BankAccount`クラスを作成し、`balance`（残高）をプライベートな属性として持たせてください。
# また、`deposit`（預入）と`withdraw`（引出）のメソッドを作成し、プロパティ`balance`を介して残高を取得できるようにしてください。
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False


bank_account = BankAccount(30)
print(f"Current balance: {bank_account.balance}")

bank_account.deposit(500)
print(f"After deposit: {bank_account.balance}")

bank_account.withdraw(200)
print(f"After withdrawal: {bank_account.balance}")

# ### 68. 演算子のオーバーロード

# `Vector`というクラスを作成し、2つの属性`x`と`y`を持たせてください。このクラスで`+`演算子をオーバーロードして、
# 2つの`Vector`オブジェクトを足し合わせて新しい`Vector`を返すようにしてください。
