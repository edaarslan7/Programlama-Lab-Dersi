#soru 4: kendisine aktarılan bir listedeki sayıların ortalamasını standart sapmasını return eden bir fonk yazınız (mean,std)
from math import sqrt

list=[1,2,3,4,5]

def mean(array):
    toplam=0
    for i in range(len(array)):
        toplam += array[i]
    return toplam/len(array)

print(mean(list))

def std(array):
    toplam=0
    ort=mean(list)
    for i in range(len(array)):
        toplam += (array[i]-ort)**2
    return sqrt(toplam/(len(array)-1))

print(std(list))
