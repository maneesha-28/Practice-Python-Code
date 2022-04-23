#to create and open a file
f=open("My first file.txt","w")
x="Hi! I'm Manisha."
y="Let's learn Python"
#to write into the file
f.write(x)
f.write("\n")
f.write(y)
f.close()
f=open("My first file.txt","r")
y=f.read()
print(y)
f.close()
