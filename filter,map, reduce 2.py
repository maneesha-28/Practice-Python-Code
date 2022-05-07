'''def checke(n):
    return n%2==0
    
nums=[12,34,6,9,4,67,90]
enums=list(filter(checke,nums))
print(enums)'''
from functools import reduce
nums=[12,34,6,9,4,67,90]
enums=list(filter(lambda n:n%2==0,nums))
print(enums)
doubles=list(map(lambda n: n+2,nums))
sums=reduce(lambda a,b:a+b,doubles)
print(sums)
