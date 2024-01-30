Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print('Hello World')
Hello World
print('Hello Lion')
Hello Lion
name = 'Lion'
lastname = 'Lionnoy'
fullname = name + ' ' + lastname
print(fullname)
Lion Lionnoy
fullname = name + lastname
print(fullname)
LionLionnoy
name = สมชาย
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    name = สมชาย
NameError: name 'สมชาย' is not defined
>>> name = 'สมชาย'
>>> lastname = 'ดีมาก'
>>> print(fullname)
LionLionnoy
>>> fullname = name + lastnameprint(fullname)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    fullname = name + lastnameprint(fullname)
NameError: name 'lastnameprint' is not defined
>>> fullname = name + lastname
>>> print(fullname)
สมชายดีมาก
>>> type(name)
<class 'str'>
>>> age = 10
>>> type(age)
<class 'int'>
>>> name = 'Uncle'
>>> name.upper()
'UNCLE'
>>> name.lower()
'uncle'
>>> print(name)
Uncle
>>> name = name.upper()
>>> print(name)
UNCLE
>>> number = '1'
>>> number.zfill(5)
'00001'
>>> number = '15'
>>> number.zfill(5)
'00015'
>>> print('ลุงครับผมชื่อ{} นามสกุล{} อายุ{} ปี'.format(name,lastname,age))
ลุงครับผมชื่อUNCLE นามสกุลดีมาก อายุ10 ปี
>>> print(f'ลุงครับผมชื่อ{name} นามสกุล{lastname} อายุ{age} ปี')
ลุงครับผมชื่อUNCLE นามสกุลดีมาก อายุ10 ปี
>>> print(f'ลุงครับ ผมชื่อ{name} นามสกุล{lastname} อายุ{age} ปี')
ลุงครับ ผมชื่อUNCLE นามสกุลดีมาก อายุ10 ปี
