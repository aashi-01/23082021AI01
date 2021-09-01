Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #2#
>>> 5**9
1953125
>>> 3//2
1
>>> 7//3
2
>>> 7/3
2.3333333333333335
>>> 6==6
True
>>> a=20
>>> a+=30
>>> a%=3
>>> print(a)
2
>>> True * False
0
>>> True & False
False
>>> True and False
False
>>> ((6>3) and (7<4) or (18==3)) and (9>3)
False
>>> True is False
False
>>> False in 'False'
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    False in 'False'
TypeError: 'in <string>' requires string as left operand, not bool
>>> ((True==False) or (False>True)) and(False<=True)
False
>>> #3#
>>> s1="Nice to have it"
>>> s2="here"
>>> print(s1+" "+s2)
Nice to have it here
>>> a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a[3][1][2][0]
'hello'
>>> a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> s1="Nice to have it"
>>> s2="here"
>>> a.insert(0,s1)
>>> a.append(s2)
>>> print(a)
['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'here']
>>> numbers=[386,462,47,418,907,344,236,375,823,566,597,978,328,615,953,345,399,162,758,219,918,237,412,566,826,248,866,950,626,949,687,217,815,67,104,58,512,24,892,894,767,553,81,379,843,831,445,742,717,958,743,527]
>>> numbers.index(237)
21
>>> for i in range(22):
	if numbers[i]%2==0:
		print(numbers[i])

		
386
462
418
344
236
566
978
328
162
758
918
>>> color_list_1=set(["White","Black","Red"])
>>> color_list_2=set(["Red","Green"])
>>> color_list_1.difference(color_list_2)
{'White', 'Black'}
>>> #9#
>>> n=int(input("Enter an integer:"))
Enter an integer:5
>>> t=str(n)
>>> n1=t+t
>>> n2=t+t+t
>>> print(n+int(n1)+int(n2))
615
>>> sen=input("Enter words:")
Enter words:without,hello,bag,world
>>> sen1=sen.split(',')
>>> sen1.sort()
>>> print((' , ').join(sen1))
bag , hello , without , world
>>> 