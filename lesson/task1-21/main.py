# ### 73. プロパティを使用したクラス


# `Temperature`というクラスを作成し、`celsius`という属性を持たせてください。
# `fahrenheit`というプロパティを作成し、摂氏（Celsius）から華氏（Fahrenheit）への
# 変換を行うゲッターを実装してください。また、`fahrenheit`のセッターを作成し、
# 華氏から摂氏に変換して`celsius`に値を設定できるようにしてください。
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 1.8) + 32  # 摂氏 -> 華氏

    @fahrenheit.setter
    def fahrenheit(self, fahrenheit):
        self._celsius = (fahrenheit - 32) / 1.8  # 華氏 -> 摂氏


# 呼び出し
temperature = Temperature(30)  # 摂氏30
print(f"摂氏:{temperature._celsius}")
print(f"華氏:{temperature.fahrenheit}")

temperature.fahrenheit = 50  # 華氏50
print(f"華氏を50°Fに設定")
print(f"摂氏: {temperature._celsius}°C")
print(f"華氏: {temperature.fahrenheit}°F")


# ### 74. クラスメソッドとスタティックメソッドの違い
# `Calculator`というクラスを作成し、以下のメソッドを持たせてください:
class Calculator:
    class_name = "Calculator"

    @staticmethod
    def add(a, b):
        print(a + b)

    @staticmethod
    def multiply(a, b):
        print(a * b)

    @classmethod
    def info(cls):
        print(f"これは{cls.class_name}クラスです")


# - `@staticmethod`として`add(a, b)`と`multiply(a, b)`を作成し、それぞれ足し算と掛け算を行う。
# - `@classmethod`として`info()`を作成し、`"これはCalculatorクラスです"`というメッセージを出力する。

# staticmethod
Calculator.add(1, 2)
Calculator.multiply(1, 2)

# classmethod
Calculator.info()


# ### 75. 抽象クラス
# `Vehicle`という抽象クラスを作成し、`move`という抽象メソッドを定義してください。
# 次に、このクラスを継承して`Car`と`Bicycle`というクラスを作成し、それぞれの`move`メソッドを実装してください。
# `Car`では`"車が走ります"`、`Bicycle`では`"自転車が走ります"`と表示されるようにしてください。
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        print("車が走ります")


class Bicycle(Vehicle):
    def move(self):
        print("自転車が走ります")


car = Car()
car.move()

bicycle = Bicycle()
bicycle.move()

# ### 76. デコレータの利用

# `Product`というクラスを作成し、`price`という属性を持たせてください。
# 次に、`price_with_tax`というプロパティを作成し、消費税を加えた金額を返すゲッターを実装してください。
# 消費税率は8%として計算してください。


class Product:
    TAX_RATE = 0.08

    def __init__(self, price):
        self._price = price

    @property
    def price_with_tax(self):
        return self._price

    @price_with_tax.setter
    def price_with_tax(self, amount):
        self._price = amount + (amount * self.TAX_RATE)


product = Product(30)
print(f"税抜き:{product._price}")

product.price_with_tax = 30
print(f"税込み:{product.price_with_tax}")
