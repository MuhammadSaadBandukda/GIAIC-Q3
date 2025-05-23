class A:
    def show(self):
        print("Show method from class A")
class B(A):
    def show(self):
        print("Show method from class B")
class C(A):
    def show(self):
        print("Show method from class C")
class D(B,C):
    def __init__(self):
        pass


d = D()
d.show()