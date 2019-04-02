#hash tablosu
import random

def myCreateHashTable(N):
    myTable=[]
    for i in range(N):
        myTable.append(0)
    return myTable
def my_hash(size,numberToBeInserted):
    return numberToBeInserted%size
def insertMyHashTable(myTable,numberToBeInserted):
    isCollission=False
    index=my_hash(len(myTable),numberToBeInserted)
    if(myTable[index]==1):
        isCollission=True
    else:
        myTable[index]=1
        #myTable[index]=numberToBeInserted
    return isCollission

m_h_1=myCreateHashTable(13)
#print(insertMyHashTable(m_h_1,17)),print(insertMyHashTable(m_h_1,30))
c=0
for s in range(10):
    number=random.randint(0,1000)
    if(insertMyHashTable(m_h_1,number)==True):
        c=c+1
    #return c

def myTest(size=13,numberOfInsert=10):
    m_h_1=myCreateHashTable(size)
    c=0
    for s in range(numberOfInsert):
        #number=random.choice([0,1,2,3,4,5,6,7,8,9])
        number=random.randint(0,10000)
        if(insertMyHashTable(m_h_1,number)==True):
            c=c+1
    return c
print(myTest(103,50))
