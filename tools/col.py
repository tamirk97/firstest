""""
module which contain a function 
this function unifying 2 arrays into 1
"""
def arZip(it1,it2):
    res=[]
    len1=len(it1)
    len2=len(it2)
    if len1==len2:
         for i in range(len1):
            res.append((it1[i],it2[i]))
    else: print("use an equal arrays, dumass")  
    return res
