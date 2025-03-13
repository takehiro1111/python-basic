# ### 61. 基本的なクラスの作成
print("\n61.基本的なクラスの作成")
# `Person`というクラスを作成してください。このクラスには以下の属性があります:
# - `name`: 文字列
# - `age`: 整数
# `introduce`というメソッドを作成し、`"私の名前は{name}で、{age}歳です。"`というメッセージを出力するようにしてください。


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def introduce(self) -> str:
        return f"私の名前は{self.name}で、{self.age}歳です。"


person = Person("takehiro1111", 30)
print(person.introduce())


# ### 62. コンストラクタを持つクラスの作成
print("\n62.コンストラクタを持つクラスの作成")
# `Car`というクラスを作成し、以下の属性を持たせてください:


# - `brand`: 文字列
# - `model`: 文字列
# - `year`: 整数
# コンストラクタでこれらの属性に初期値を設定できるようにし、`get_info`というメソッドで`"{brand} {model} ({year})"`という形式で出力してください。
class Car:
    def __init__(self, brand: str, model: str, year: int) -> None:
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self) -> str:
        return f"{self.brand} {self.model} ({self.year})"


car = Car("TOYOTA", "PRIUS", 2025)
print(car.get_info())

# ### 63. メソッドを持つクラス
print("\n63.メソッドを持つクラス")


# `Rectangle`というクラスを作成し、以下の属性を持たせてください:
# - `width`: 整数
# - `height`: 整数
# `area`というメソッドを作成し、長方形の面積を計算して返すようにしてください。
class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def area(self) -> int:
        return self.width * self.height


rectangle = Rectangle(5, 10)
print(rectangle.area())

# ### 64. 継承を使用したクラス
print("\n64.継承を使用したクラス")


# `Animal`というクラスを作成し、`speak`というメソッドを作成して`"動物の鳴き声"`と表示するようにしてください。
# 次に、`Dog`というクラスを`Animal`クラスを継承して作成し、`speak`メソッドをオーバーライドして`"ワンワン"`と表示するようにしてください。
class Animal:
    def speak(self) -> str:
        return "動物の鳴き声"


class Dog(Animal):
    def speak(self) -> str:
        return "ワンワン"


animal = Animal()
print(animal.speak())

dog = Dog()
print(dog.speak())
