#soru 5: bri matris veriliyor. matrisin det bulan fonk yaz.☻
#b)bir matris veriliyor matris tekil midir. sorusuna cevap veren fonk☻
#c)matrisi eş olan matrise cevir her adımda elementer islemleriyle olustur.
#d)bir matriste satır ve sutunlarının toplamı en kucuk, en buyuk olan satır ve sutunlarını bulunuz.☻
#e)bir matriste kac tane 0 oldugunu bulan bir fonk yazınız.☻
#f)matristeki 0 oranı %30un altında ise bu matrisi iki boyutlu listeden bir hash yapısına aktarınız.☻
#g)0lar çok oldugu için hash yapısı ile oluşturulmuş matrisi iki boyutlu listeye aktarınız.☻
from math import sqrt


def det(matris):
    if(len(matris)>2):
        determinant = 0
        satir=len(matris)
        sutun=len(matris[0])
        m=0
        for n in range(sutun):
            newMatris = []
            for i in range(satir):
                row = []
                if (m == i):
                    continue
                for j in range(sutun):
                    if (n == j):
                        continue
                    row.append(matris[i][j])

                newMatris.append(row)
            determinant += matris[0][n]*pow(-1,n)*(det(newMatris))
            #print(newMatris,determinant,matris[0][n])
        return determinant
    else:
        return (matris[0][0]*matris[1][1] - matris[0][1]*matris[1][0])

matris=[[5,4,9,6],[4,3,8,10],[8,7,12,5],[7,5,3,9]]
#print(det(matris))

#-------------b şıkkı--------

def tekilMi(matris):
    if(det(matris)==0):
        return True
    else:
        return False

#print(tekilMi(matris))

#--------c şıkkı-------
def esMatris(matris):
    a=len(matris)-1
    m=len(matris[0])
    for i in range(m):
        matris[a][i] += int(-matris[a][i]/matris[0][i]*matris[0][i])
    return matris
matris3=[[4,8,6,1],[3,7,8,2],[5,4,6,7],[7,9,1,3]]
print(esMatris(matris3))
#print(matris3[len(matris3)-1][2]+ -matris3[len(matris3)-1][2]/matris3[0][2]*matris3[0][2])

#----------d şıkkı------------
def buyukKucuk(matris):
    satirToplam,sutunToplam = [],[]
    sutunTop,satirTop=0,0
    satir=len(matris)
    sutun=len(matris[0])
    for i in range(sutun):
        satirTop, sutunTop = 0, 0
        for j in range(satir):

            satirTop += matris[i][j]
            sutunTop += matris[j][i]

        sutunToplam.append(sutunTop)
        satirToplam.append(satirTop)
        print(satirToplam[i], sutunToplam[i])
    satirKucuk=satirToplam[0]
    sutunKucuk=sutunToplam[0]
    sutunBuyuk=sutunToplam[0]
    satirBuyuk=satirToplam[0]
    for m in range(len(satirToplam)):

        if(satirToplam[m]>satirBuyuk):
            satirBuyuk=satirToplam[m]
        else:
            satirKucuk=satirToplam[m]

    for n in range(len(sutunToplam)-1):
        if(sutunToplam[n]>sutunBuyuk):
            sutunBuyuk=sutunToplam[n]
        else:
            sutunKucuk=sutunToplam[n]

    print("Satirlarin en kucuk toplami: ",satirKucuk)
    print("Satirlarin en buyuk toplami: ",satirBuyuk)
    print("Sutunlarin en kucuk toplami: ",sutunKucuk)
    print("Sutunlarin en buyuk toplami: ",sutunBuyuk)

#buyukKucuk(matris)

#-------e şıkkı-----
def sifir(matris):
    satir=len(matris)
    sutun=len(matris[0])
    sayac=0
    for i in range(satir):
        for j in range(sutun):
            if(matris[i][j]==0):
                sayac  += 1
    return sayac

matris2=[[0,2,3],[5,0,3],[1,5,7]]

#print(sifir(matris2))

#----f şıkkı-----
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

#print(myFunctionConvertToHash(matris))

def conditionForHash(matris):
    satir=len(matris)
    sutun=len(matris[0])
    sifirSayisi=sifir(matris)
    if((sifirSayisi/(satir*sutun))<(30/100)):
        return myFunctionConvertToHash(matris)

conditionForHash(matris2)

#-----g şıkkı-----

def myFunctionHashToList(myHash):
    myList=[]
    m=int(sqrt(len(myHash)))
    for i in range(m):
        myList.append([])
        for j in range(m):
            myList[i].append(0)
    for i in range(m):
        for j in range(m):
            myList[i][j]=myHash[(i,j)]
    return myList

#print(myFunctionHashToList(conditionForHash(matris2)))