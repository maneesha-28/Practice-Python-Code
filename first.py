a=float(input("Enter a number: "))
print(type(a))
b=a%2
print(b)
if a==0:
    print("You have entered zero")
elif a%2==0:
    print("Number is even")
else:
    print("Number is odd")
