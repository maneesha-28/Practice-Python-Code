'''write a python script to write the execution time for a variable in a
file where the variable is used to find the factorial using iterative 
& recursion method'''

def fact_r(x):
    y=1
    if x==1 or x==0:
        return y
    else:
        y=x*fact_r(x-1)
        return y

def fact_i(x):
    fact = 1
    for i in range(1,x+1):
        fact=fact*i
    return fact

import time as t
f=open("exe_time_comparison.txt","w")
f.write("For factorial using recursion")
f.write("\n\n")
f.write("Input Value -->Execution Time(in secs)\n")
for i in range(5,995,5):
    start = t.time()
    fact_r(i)
    end = t.time()
    total_time = end - start
    tot=str(total_time)
    f.write(str(i)+"          "+tot+" secs")
    f.write("\n")

f.write("\n\n\n")
f.write("For factorial using iteration")
f.write("\n\n")
f.write("Input Value -->Execution Time(in secs)\n")
for i in range(5,995,5):
    start = t.time()
    result = fact_i(i)
    end = t.time()
    total_time = end - start
    tot=str(total_time)
    f.write(str(i)+"          "+tot+" secs")
    f.write("\n")
f.close()
