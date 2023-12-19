""""
module which contain 2 complicated functions:
*function which sum digit of randon number
*function which get a number and returns of it a pallindrom
note:you cant use them unless u tried simp.py functions
"""


def digitSum(num):
    temp=0
    num=abs(num)
    while (num>0):
        temp=temp+(num%10)
        num //= 10
    return temp    



def pallindrom(num1):
    num1 = num1.lower()
    num1 = ''.join(char for char in num1 if char.isalnum())
    start = 0
    end = len(num1) - 1
    while start < end:
        if num1[start] != num1[end]:
            return False  
        start += 1
        end -= 1

    return True  