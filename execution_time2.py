#Program to calculate the execution time of a program
'''Using now() Function from datetime module'''
import datetime as d
start = d.datetime.now()
def fact(r):
    a=3.14*r*r
    return(a)
radius=int(input("Enter the radius of the circle : "))
print("Area of the circle = ",fact(radius))
end=d.datetime.now()
total_time=end-start
print("Execution time of the above program =",total_time,"hour:min:sec:microsec")
