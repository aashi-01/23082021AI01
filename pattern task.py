Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(1,6):
	print("*"*i)

	
*
**
***
****
*****
>>> #2#
>>> for i in range(1,6):
	print(" "*(5-i),end="")
	print("*"*i)

	
    *
   **
  ***
 ****
*****
>>> #3#
>>> for i in range(1,6):
	for j in range(1,i+1):
		print(j,end="")
	print("")

	
1
12
123
1234
12345
>>> #4#
>>> for i in range(1,6):
	t=str(i)
	print(t*i)

	
1
22
333
4444
55555
>>> #5#
>>> for i in range(1,6):
	print("*"*i,end="")
	print(" "*(10-(2*i)),end="")
	print("*"*i)

	
*        *
**      **
***    ***
****  ****
**********
>>> 