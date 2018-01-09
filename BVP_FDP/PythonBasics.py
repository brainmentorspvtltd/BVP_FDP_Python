Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("Hello")
Hello
>>> a = 10
>>> b = 10.5
>>> type(a)
<class 'int'>
>>> type(b)
<class 'float'>
>>> a+b
20.5
>>> a-b
-0.5
>>> a*b
105.0
>>> a/b
0.9523809523809523
>>> a//b
0.0
>>> a = 12
>>> b = 5
>>> a/b
2.4
>>> a//b
2
>>> import sys
>>> sys.getsizeof(a)
28
>>> id(a)
1878312976
>>> a,b = 10,12
>>> a,b = b,a
>>> file = open('Text_1.txt')
>>> file.read()
'This is demo text file'
>>> file = open('Text_3.txt' , 'w')
>>> file.read()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    file.read()
io.UnsupportedOperation: not readable
>>> file.write('This is a sample text')
21
>>> import os
>>> os.getcwd()
'C:\\Python36'
>>> os.startfile('dhoni.mp4')
>>> os.startfile('Text_3.txt')
>>> os.system('calc')
0
>>> os.system('notepad')
0
>>> a = "Hello"
>>> print(a)
Hello
>>> a
'Hello'
>>> a*6
'HelloHelloHelloHelloHelloHello'
>>> x = 12
>>> x*6
72
>>> x**6
2985984
>>> x**2
144
>>> a
'Hello'
>>> a = "Hello"
>>> a = 'Hello'
>>> a[0]
'H'
>>> a[2]
'l'
>>> a[0:3]
'Hel'
>>> a[-1]
'o'
>>> a[:]
'Hello'
>>> a[0:]
'Hello'
>>> a[:50]
'Hello'
>>> a[::-1]
'olleH'
>>> a = "Hello world"
>>> a[0:10:2]
'Hlowr'
>>> a[::-1]
'dlrow olleH'
>>> emp = [101,102,103,104,'Ram', 'Shyam', 'Gopal', 'Ajay', 25000.00]
>>> emp
[101, 102, 103, 104, 'Ram', 'Shyam', 'Gopal', 'Ajay', 25000.0]
>>> emp[2]
103
>>> emp[0:5]
[101, 102, 103, 104, 'Ram']
>>> print(emp[0:5])
[101, 102, 103, 104, 'Ram']
>>> emp = [2,4,6,1,3,9,7,4,0,3]
>>> emp.sort()
>>> emp
[0, 1, 2, 3, 3, 4, 4, 6, 7, 9]
>>> emp.sort(reverse = True)
>>> emp
[9, 7, 6, 4, 4, 3, 3, 2, 1, 0]
>>> 9 in emp
True
>>> emp.index(9)
0
>>> emp = []
>>> emp.append(10)
>>> emp
[10]
>>> emp.append(11)
>>> emp
[10, 11]
>>> emp.append(12,13,14,15)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    emp.append(12,13,14,15)
TypeError: append() takes exactly one argument (4 given)
>>> emp.append([12,13,14,15])
>>> emp
[10, 11, [12, 13, 14, 15]]
>>> emp[2]
[12, 13, 14, 15]
>>> emp[2][2]
14
>>> emp.pop()
[12, 13, 14, 15]
>>> emp
[10, 11]
>>> emp = [10,11,12,13,14,15,16]
>>> emp.pop(3)
13
>>> emp
[10, 11, 12, 14, 15, 16]
>>> emp.insert(0,'Hello')
>>> emp
['Hello', 10, 11, 12, 14, 15, 16]
>>> emp = (10,11,12,13,14,15,16)
>>> emp
(10, 11, 12, 13, 14, 15, 16)
>>> emp[6]
16
>>> emp[0:4]
(10, 11, 12, 13)
>>> emp[0] = 'Hello'
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    emp[0] = 'Hello'
TypeError: 'tuple' object does not support item assignment
>>> emp = {'id' : 101, 'name' : 'Ram', 'age' : 17}
>>> emp[0]
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    emp[0]
KeyError: 0
>>> emp['id']
101
>>> emp['name']
'Ram'
>>> emp.keys()
dict_keys(['id', 'name', 'age'])
>>> emp.values()
dict_values([101, 'Ram', 17])
>>> emp.items()
dict_items([('id', 101), ('name', 'Ram'), ('age', 17)])
>>> emp = [{'id' : 101, 'name' : 'Ram'}, {'id' : 102, 'name' : 'Shyam'}, {'id' : 103, 'name' : 'Mohan'}]
>>> emp
[{'id': 101, 'name': 'Ram'}, {'id': 102, 'name': 'Shyam'}, {'id': 103, 'name': 'Mohan'}]
>>> emp[0]
{'id': 101, 'name': 'Ram'}
>>> emp[0]['name']
'Ram'
>>> s1 = {2,3,4,5,6}
>>> s2 = {5,6,4,8,9}
>>> s1.intersection(s2)
{4, 5, 6}
>>> s1.union(s2)
{2, 3, 4, 5, 6, 8, 9}
>>> 
