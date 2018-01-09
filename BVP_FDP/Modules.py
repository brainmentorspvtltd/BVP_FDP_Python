Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: C:/Users/asus/Desktop/BVP_FDP/03-Functions.py ===========
22
>>> 
=========== RESTART: C:/Users/asus/Desktop/BVP_FDP/03-Functions.py ===========
Traceback (most recent call last):
  File "C:/Users/asus/Desktop/BVP_FDP/03-Functions.py", line 11, in <module>
    add()
NameError: name 'add' is not defined
>>> 
=========== RESTART: C:/Users/asus/Desktop/BVP_FDP/03-Functions.py ===========
22
-2
>>> 
=========== RESTART: C:/Users/asus/Desktop/BVP_FDP/03-Functions.py ===========
>>> 
=========== RESTART: C:/Users/asus/Desktop/BVP_FDP/03-Functions.py ===========
<function calc.<locals>.add at 0x000001F414793E18>
>>> def add():
	print("Hello")

	
>>> add()
Hello
>>> add
<function add at 0x000001F414793E18>
>>> 
=========== RESTART: C:/Users/asus/Desktop/BVP_FDP/03-Functions.py ===========
>>> 
=========== RESTART: C:/Users/asus/Desktop/BVP_FDP/03-Functions.py ===========
22
>>> def calc(x,y):
	return x + y, x - y, x * y, x / y

>>> calc(2,5)
(7, -3, 10, 0.4)
>>> i = calc(2,5)
>>> i
(7, -3, 10, 0.4)
>>> a,b,c,d = calc(2,5)
>>> a
7
>>> b
-3
>>> c
10
>>> d
0.4
>>> 
=========== RESTART: C:/Users/asus/Desktop/BVP_FDP/03-Functions.py ===========
Traceback (most recent call last):
  File "C:/Users/asus/Desktop/BVP_FDP/03-Functions.py", line 17, in <module>
    print(a())
TypeError: 'tuple' object is not callable
>>> 
=========== RESTART: C:/Users/asus/Desktop/BVP_FDP/03-Functions.py ===========
(<function calc.<locals>.add at 0x000001F905E33E18>, <function calc.<locals>.sub at 0x000001F906BF2730>)
>>> 
=========== RESTART: C:/Users/asus/Desktop/BVP_FDP/03-Functions.py ===========
22
-2
>>> import calendar
>>> m = calendar.month(2018, 1)
>>> print(m)
    January 2018
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31

>>> from datetime import datetime
>>> from datetime import date
>>> from datetime import time
>>> now = datetime.now()
>>> print(now)
2018-01-09 13:15:58.147000
>>> now = datetime.now().date()
>>> print(now)
2018-01-09
>>> now = datetime.now().time()
>>> print(now)
13:16:34.205997
>>> 
