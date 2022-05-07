'''#creating attributes
class subject:
    sub1="Python"
    sub2="JavaScript"
    sub3="Rust"
print(subject.sub1)
print(subject.sub2)
print(subject.sub3)

#creating an object
ob1=subject()
print(ob1.sub1)

#changing the values of attributes
#directly using class name
subject.sub2="Solidity"
obj2=subject()
print(obj2.sub2)
obj3=subject()
obj3.sub3="Go lang"
print(obj3.sub3)
print(obj2.sub3)'''

#creating methods
class  subject:
    def __init__(self,name,code):
        self.name=name
        self.code=code
    def subname(self):
        print("The subject is ",self.name)
        print("The code is",self.code)
obj1=subject("Python",123)
print(obj1.subname())
