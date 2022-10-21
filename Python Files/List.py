Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list = ['aa', 'bb', 'cc', 'dd']
>>> list
['aa', 'bb', 'cc', 'dd']
>>> type(list)
<class 'list'>
>>> len(list)
4
>>> list[0]
'aa'
>>> list910
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list910
NameError: name 'list910' is not defined
>>> list[1]
'bb'
>>> list[2]
'cc'
>>> list[3]
'dd'
>>> list[4]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    list[4]
IndexError: list index out of range
>>> list.index('aa')
0
>>> list.index('cc')
2
>>> list.append('ee')
>>> list
['aa', 'bb', 'cc', 'dd', 'ee']
>>> len(list)
5
>>> list.pop(4)
'ee'
>>> list
['aa', 'bb', 'cc', 'dd']
>>> len(list)
4
>>> list.remove('aa')
>>> list
['bb', 'cc', 'dd']
>>> len(list)
3
>>> list.insert(0, 'aa')
>>> list
['aa', 'bb', 'cc', 'dd']
>>> len(list)
4
>>> list.insert(2, 'xx')
>>> list
['aa', 'bb', 'xx', 'cc', 'dd']
>>> list.remove('xx')
>>> list
['aa', 'bb', 'cc', 'dd']
>>> list.append('aa')
>>> list
['aa', 'bb', 'cc', 'dd', 'aa']
>>> len(list)
5
>>> list.count('aa')
2
>>> list.count('cc')
1
>>> list.pop(4)
'aa'
>>> list
['aa', 'bb', 'cc', 'dd']
>>> list.reverse()
>>> list
['dd', 'cc', 'bb', 'aa']
>>> list[0]
'dd'
>>> list.index('dd')
0
>>> list.reverse()
>>> list
['aa', 'bb', 'cc', 'dd']
>>> list.append('ee')
>>> list
['aa', 'bb', 'cc', 'dd', 'ee']
>>> len(list)
5
>>> list[1:3]
['bb', 'cc']
>>> list[:3]
['aa', 'bb', 'cc']
>>> list[3:]
['dd', 'ee']
>>> list[:]
['aa', 'bb', 'cc', 'dd', 'ee']
>>> list
['aa', 'bb', 'cc', 'dd', 'ee']
>>> list
['aa', 'bb', 'cc', 'dd', 'ee']
>>> list + list
['aa', 'bb', 'cc', 'dd', 'ee', 'aa', 'bb', 'cc', 'dd', 'ee']
>>> list + list[:3]
['aa', 'bb', 'cc', 'dd', 'ee', 'aa', 'bb', 'cc']
>>> list[:3] + list[3:]
['aa', 'bb', 'cc', 'dd', 'ee']
>>> list + list + list
['aa', 'bb', 'cc', 'dd', 'ee', 'aa', 'bb', 'cc', 'dd', 'ee', 'aa', 'bb', 'cc', 'dd', 'ee']
>>> list_2 = []
>>> list_2
[]
>>> len(list_2)
0
>>> list_2 = list
>>> list_2
['aa', 'bb', 'cc', 'dd', 'ee']
>>> len(list_2)
5
>>> list_3 = []
>>> list_3
[]
>>> LIST_3.append('aaa')
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    LIST_3.append('aaa')
NameError: name 'LIST_3' is not defined
>>> list_3.sppend('aaa')
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    list_3.sppend('aaa')
AttributeError: 'list' object has no attribute 'sppend'
>>> list_3.append('aaa')
>>> list_3
['aaa']
>>> list_3.append('bbb')
>>> list_3
['aaa', 'bbb']
>>> 