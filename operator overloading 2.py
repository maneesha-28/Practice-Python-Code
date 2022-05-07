class A:
    def __init__(self,a):
        self.a=a
    def __add__(self,o):
        return self.a+o.a
o1=A(12)
o2=A(17)
o3=o1+o2
print(o3)
