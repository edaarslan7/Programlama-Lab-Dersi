#-------------soru 6:lab uygulamalarında kelime frekanslarının oldugu fonksiyonu hash yapısını listeye aktaran fonksiyon
#b)tersini yani iki boyutlu listeyi hash yapısına altaran fonk------------------
#m*n boyutlarında btün elemanları -1 olan 2 boyutlu bir liste oluştur
import random
from math import sqrt

def myFunctionCreate(m: int,n: int):
    myList=[]
    for i in range(m):
        myList.append([])
        for j in range(n):
            #s=random.randint(-1,1)
            s=-1
            myList[i].append(s)
    return myList

def myFunctionPrint(myList):
    m=len(myList)
    n=len(myList[0])
    for i in range(m):
        for j in range(n):
            print(myList[i][j],end=" ")
        print( )

#my2ndArray=myFunctionCreate(3,2)
#myFunctionPrint(my2ndArray)

def myFunctionConvertToHash(myList):
    myDict={}
    m=len(myList)
    n=len(myList[0])
    for i in range(m):
        for j in range(n):
            myDict[(i,j)]=myList[i][j]
            #print(myList[i][j],end=" ")
        #print( )
    return myDict

def myFunctionPrintHash(myHashList):
    print("  ")
    for key in myHashList:
        print(myHashList[key],end=" ")


#myList=(myFunctionCreate(3,2))
#myFunctionPrintHash(myFunctionConvertToHash(myList))

def myFunctionHashToList(myHashList):
    myList=[]
    m = int(sqrt(len(myHashList)))
    for i in range(m):
        myList.append([])
        for j in range(m):
            #s=random.randint(-1,1)
            s=-1
            myList[i].append(s)
    for i in range(m):
        for j in range(m):
            myList[i][j]=myHashList[(i,j)]
            #print(myList[i][j],end=" ")
        #print( )
    return myList

myHashList={(0,0):2,(0,1):5,(1,0):4,(1,1):2}
#myFunctionPrint(myFunctionHashToList(myFunctionConvertToHash(myList)))
print(myFunctionHashToList(myHashList))