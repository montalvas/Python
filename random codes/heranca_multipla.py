class A:
    def m1(self):
        print('A')


class B(A):
    def m2(self):
        print('B')


class C(A):
    def m2(self):
        print('C')


class D(B, C):
    def m1(self):
        super().m1()

    def m2(self):
        super().m2()

if __name__ == '__main__':
    print(D.mro())
    d = D()
    d.m1()
    d.m2()