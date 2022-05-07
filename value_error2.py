#enter float value and type cast to int
Enter a number : 1.2
<class 'str'>
Traceback (most recent call last):
  File "F:/python/UserInput.py", line 7, in <module>
    a= int(a)
ValueError: invalid literal for int() with base 10: '1.2'

#when we enter a string(non Int) and do type casting to int
Enter a number : chem
<class 'str'>
Traceback (most recent call last):
  File "F:/python/UserInput.py", line 7, in <module>
    a= int(a)
ValueError: invalid literal for int() with base 10: 'chem'
