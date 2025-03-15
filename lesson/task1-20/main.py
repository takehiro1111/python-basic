# ### 69. クラスメソッドの使用
print("\n69. クラスメソッドの使用")


# `Employee`クラスを作成し、`name`と`salary`の属性を持たせてください。
# また、クラスメソッド`create_employee`を作成し、`name`と`salary`を引数として新しい`Employee`オブジェクトを生成する静的な方法を提供してください。
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def create_employee(cls, name, salary):
        return cls(name, salary)


# クラスメソッドで呼び出す。
employee1 = Employee.create_employee("sato", 3000)
employee2 = Employee.create_employee("tanaka", 5000)

print(employee1.name, employee1.salary)
print(employee2.name, employee2.salary)


# ### 70. スタティックメソッドの使用
print("\n70. スタティックメソッドの使用")


# `MathOperations`というクラスを作成し、`add`と`multiply`という2つのスタティックメソッドを作成してください。
# これらのメソッドは2つの数値を受け取り、それぞれ足し算と掛け算を行うものとします。
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


print(MathOperations.add(2, 3))
print(MathOperations.multiply(2, 3))


# ### 71. 特殊メソッド（`__str__`と`__repr__`）
print("\n71. 特殊メソッド（`__str__`と`__repr__`）")
# `Book`というクラスを作成し、以下の属性を持たせてください:

# - `title`: 文字列
# - `author`: 文字列


# このクラスで`__str__`と`__repr__`の特殊メソッドを実装し、`print()`関数でオブジェクトを出力したときに、`
# __str__`では `"タイトル: {title}, 著者: {author}"` の形式で表示され、
# `__repr__`では `"Book('{title}', '{author}')"` の形式で表示されるようにしてください。
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"タイトル: {self.title}, 著者: {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"


book1 = Book("title-1", "author-1")

print(str(book1))

book2 = Book("title-2", "author-2")
print(repr(book2))


# ### 72. 継承とポリモーフィズム
print("\n72. 継承とポリモーフィズム")
# `Shape`という抽象クラスを作成し、`area`という抽象メソッドを定義してください。
# 次に、`Circle`（円）と`Rectangle`（長方形）という2つのクラスを`Shape`クラスから継承し、それぞれの`area`メソッドを実装してください。

# - `Circle`クラスには`radius`（半径）を持たせ、面積を計算してください。
# - `Rectangle`クラスには`width`（幅）と`height`（高さ）を持たせ、面積を計算してください。
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (self.radius**2) * 3.14


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


circle_area = Circle(5)
print(circle_area.area())

rectangle_area = Rectangle(10, 5)
print(rectangle_area.area())
