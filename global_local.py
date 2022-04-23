def user_input():
    a=int(input("Enter value 1 : "))
    b=int(input("Enter value 2 : "))
    return(a,b)
    
def add(a,b):
    return a+b;
a,b=user_input()
c=add(a,b)
print(a," + ",b," = ",c)

#num1,num2=int(input("Value 1 : "),input())
