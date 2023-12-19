from tools.col import arZip
from tools.numbers.comp import digitSum, pallindrom
from tools.numbers.simp import add, sub, used2,used1
from icecream import ic


def main():
        
        resultAdd=add(5,2)
        resultsub=sub(5,2)
        ic(resultAdd)
        ic(resultsub)
        if (used1) or (used2):
         digits=digitSum(523)
         print(digits)
         palli=pallindrom('123431')
         print(palli)
        
        else:print("you should try a simple function first")
        ar2=arZip([1,2,2],[3,4,5])
        print(ar2)

       

if __name__ == "__main__":
    main()