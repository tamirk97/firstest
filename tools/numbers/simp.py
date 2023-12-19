""""
module which contain 2 simple functions
*function which add numbers
*function which sub numbers
"""


def add(a,b):
    global used1
    used1=True
    return (a+b)
def sub(a,b):
    global used2
    used2=True
    return (a-b)

used1=False
used2=False
