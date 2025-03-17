# ### 77. 演算子のオーバーロード
print("\n77. 演算子のオーバーロード")


# `Time`というクラスを作成し、`hours`と`minutes`という属性を持たせてください。
# このクラスで`+`演算子をオーバーロードして、2つの`Time`オブジェクトを足し合わせた結果を
# 新しい`Time`オブジェクトとして返すようにしてください。
# 時間と分の加算が正しく行われるようにしてください（60分を超えた場合は1時間に繰り上げ）。
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __add__(self, other):
        total_hours = self.hours + other.hours
        total_minutes = self.minutes + other.minutes

        if total_minutes >= 60:
            total_hours += total_minutes // 60
            total_minutes = total_minutes % 60

        return Time(total_hours, total_minutes)

    def __str__(self):
        return f"{self.hours}h:{self.minutes}m"


time1 = Time(5, 45)
time2 = Time(4, 15)

total_time = time1 + time2
print(total_time)


# ### 78. データクラス
print("\n78. データクラス")
# `dataclasses`モジュールを使用して、`Person`クラスをデータクラスとして作成してください。
# このクラスは`name`と`age`の属性を持ち、コンストラクタ、`__repr__`、`__eq__`メソッドを自動生成させてください。
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


person = Person("takehiro1111", 30)
print(person == Person("takehiro1111", 30))
print(person == Person("suzuki", 20))


# ### 79. シングルトンパターン
print("\n79. シングルトンパターン")


# `Singleton`というクラスを作成し、このクラスが常に1つのインスタンスしか生成されないようにしてください。
# 複数のインスタンスを作成しようとした場合、最初に作成したインスタンスが返されるようにしてください。
class Singleton:
    _instance = None

    def __new__(cls, *args):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("インスタンスを作成")
        return cls._instance

    def __init__(self, name, age):
        self.name = name
        self.age = age


singleton1 = Singleton("takehiro1111", 30)
singleton2 = Singleton("suzuki", 20)

if singleton1 is singleton2:
    print("同じインスタンスです")
else:
    print("同じインスタンスではありません")

singleton1 = Singleton("takehiro1111", 30)
print(id(singleton1))
print(f"singleton1: {singleton1.name}, {singleton1.age}")

singleton2 = Singleton("suzuki", 20)
print(id(singleton2))
print(f"singleton2: {singleton2.name}, {singleton2.age}")

# ### 80. ミックスインの使用
print("\n80. ミックスインの使用")


# `LoggableMixin`というクラスを作成し、`log`というメソッドを持たせてください。
# このメソッドは`"ログ出力: {message}"`と表示します。次に、`User`というクラスを作成し、
# この`LoggableMixin`をミックスインとして使用して`User`クラスにログ出力機能を追加してください。
class LoggableMixin:
    def log(self, message):
        return f"ログ出力: {message}"


class User(LoggableMixin):  # LoggableMixinを継承
    def __init__(self, name):
        self.name = name


# 使用例
user = User("test_message")
print(user.log("継承したUserクラスのログ"))
