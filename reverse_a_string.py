#using loop
def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str
  
s = "Hello! I'm Manisha Nair"
print ("The original string  is : ",end="")
print (s)
print ("The reversed string is : ",end="")
print (reverse(s))


#using recursion
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
  
s = "Hello! I'm Manisha Nair"
  
print ("The original string  is : ",end="")
print (s)
  
print ("The reversed string is : ",end="")
print (reverse(s))
