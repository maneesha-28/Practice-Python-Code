#Program to calculate the execution time of a program
'''Using Time Function'''
import time as t
start=t.time()
def fact(r):
    a=3.14*r*r
    return(a)
radius=int(input("Enter the radius of the circle : "))
print("Area of the circle = ",fact(radius))
end=t.time()
total_time=end - start
print("Execution time of this program =",total_time,"seconds")
