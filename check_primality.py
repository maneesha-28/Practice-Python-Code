# Check primality 
'''temp=0
num=int(input("Enter a number : "))
if(num==0 or num==1):
    print("Not a prime number")
for i in range(2,num-1):
    if num%i==0:
        temp=temp+1
        break
if temp>0:
    print(num,"is not a prime number")
else:
    print(num,"is a prime number")'''

# check primality using for else
num=int(input("Enter a number : "))
if(num==0 or num==1):
    print("Not a prime number")
else:
    for i in range(2,num-1):
        if num%i==0:
            print(num,"is not a prime number")
            break

    else:
        print(num,"is a prime number")
