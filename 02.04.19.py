#soru 1: bir fonksiyona text,string 2 parametre aktarılıyor (liste string search)
#a)(string) text te var ise true ya da false dönderen bir fonk yaz.
#b)string varsa textte bulundugu ilk baslangıc konumunu dönderen fonk yaz
#c)ikinci gönderilen parametre birinci paramtereden n defa bulunuyorsa bulundugu yerlerin baslangıc adreslerini liste hlainde geri dönderen fonks yaz.

#soru 2: tersten okunusu ile aynı olan kelimeleri test eden bir fonk yazınız. True False
#soru 3: n*n tane karakteri n*n matrise atayan bir fonk yazınız.
#b)kendisine aktarılan bir kelimeyi bu matris üzerinde soldan sağa sağdan sola yukarıdan asagıya asagıdan yukarıya dogrultularında arayıp olup olmadıgını return eden fonk yazınız.
#soru 4: kendisine aktarılan bir listedeki sayıların ortalamasını standart sapmasını return eden bir fonk yazınız (mean,std)
#soru 5: bri matris veriliyor. matrisin det bulan fonk yaz.
#b)bir matris veriliyor matris tekil midir. sorusuna cevap veren fonk
#c) matrisi eş olan matrise cevir her adımda elementer islemleriyle olustur.
#d)bir matriste satır ve sutunlarının toplamı en kucuk, en buyuk olan satır ve sutunlarını bulunuz.
#e)bir matriste kac tane 0 oldugunu bulan bir fonk yazınız.
#f)matristeki 0 oranı %30un altında ise bu matrisi iki boyutlu listeden bir hash yapısına aktarınız.
#g)0lar çok oldugu için hash yapısı ile oluşturulmuş matrisi iki boyutlu listeye aktarınız.
#soru 6: lab uygulamalarında kelime frekanslarının oldugu fonksiyonu hash yapısını listeye aktaran fonksiyon
#b)tersini yani iki boyutlu listeyi hash yapısına altaran fonk
#soru 7:verilen bir formule göre sayının kokunu bulma
#b)belli bir hassasiyete göre e^10 u bulma
#soru 8: hash yapısı ile gösterilen matrislere ait +,-,* işlemlerini yapan fonksiyonları yazınız.


#-------------soru 6:------------------
#m*n boyutlarında btün elemanları -1 olan 2 boyutlu bir liste oluştur
import random

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


myList=(myFunctionCreate(3,2))
myFunctionPrintHash(myFunctionConvertToHash(myList))












