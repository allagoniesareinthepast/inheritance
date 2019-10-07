# Superclass -> (상속: attribute, method) Subclass


class Pen:
    """Superclass"""

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def disp(self):
        return "Pen"


class Munhwa(Pen):
    """Subclass"""

    def __init__(self, name, color, pen_type):
        super().__init__(name, color)
        self.pen_type = pen_type

    def disp_sub(self):
        return "Pen Type : %s" % self.pen_type


class Bic(Pen):
    def __init__(self, name, color, pen_type):
        super().__init__(name, color)
        self.pen_type = pen_type

    def disp(self):
        print(super().disp())  # superclass의 method도 상속 받고 싶을 때
        return "Pen Info : %s, %s, %s" % (self.name, self.color, self.pen_type)


p1 = Munhwa("easy glide", "blue", "gel")
print(p1.disp_sub())
print(p1.__dict__)
print(p1.disp())  # superclass method 상속되는 걸 볼 수 있음

p2 = Bic("sign pen", "black", "ball")
print(p2.__dict__)
print(p2.disp())  # 이것이 바로 >>override<< 같은 이름의 method가 있을 때, subclass를 더 우선함.
