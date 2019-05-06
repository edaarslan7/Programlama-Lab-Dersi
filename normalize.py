#normalize/gauss (
#random - mean - std - normalize - mean +-std - main+-2*std - mean3std
#buble sortta-selection-intersal sıralıycaz oran tutucaz hangisinin daha iyi oldugu bulunur
#(normalize=x-mean)/std
import random
from math import sqrt

def get_n_random_integer(n): #sayılar
    #random.seed(100)  #aynı deger uretmek ıcın saate gore
    numbers=[]
    for i in range(n):
        s=random.randint(0,100)
        numbers.append(s)
    return numbers

sayilar=get_n_random_integer(5)
print("sayilar",sayilar)


def get_mean_for_n_integer(numbers): #ortalamasını bulduk
    toplam=0
    tane=0
    for sayi in numbers:
        toplam=toplam+sayi
        tane=tane+1
    return toplam/tane

ortalama=get_mean_for_n_integer(sayilar)
print("ortalaması",ortalama)


def get_std_for_n_integer(numbers): #standart sapamasını bulduk
    toplam=0
    tane=0
    ortalama=get_mean_for_n_integer(numbers) #ortalamaya gore farkı alınarak ve kareleri alınarak bulunur 
    for sayi in numbers:
        toplam=toplam+(sayi-ortalama)**2
        tane=tane+1
    var_1=toplam/(tane-1)
    std_1=sqrt(var_1)
    return std_1

standartSapma=get_std_for_n_integer(sayilar)
print("standart sapmasi",standartSapma)


def normalizasyon(numbers):
    new_numbers=[]
    ortalama=get_mean_for_n_integer(numbers)
    standartSapma=get_std_for_n_integer(numbers)
    for x in numbers:  #sayıyı ortalamadan cıkarıp standart sapmaya boldu
        new_x=(x-ortalama)/standartSapma
        new_numbers.append(new_x)
    return new_numbers

normalize=normalizasyon(sayilar)
print("yeni normalize liste",normalize)


def get_mean_one_std_neighbor_ratio(numbers): #standart sapmanın ortalamaya yakınlıkları
    tane=0
    toplamKacSayi=0
    
    ortalama=get_mean_for_n_integer(numbers)
    standart=get_std_for_n_integer(numbers)

    low=ortalama-standart
    high=ortalama+standart
    
    for x in numbers:
        toplamKacSayi+=1
        if(x>low and x<high):
            tane+=1
    return tane/toplamKacSayi

a=get_mean_one_std_neighbor_ratio(sayilar)
print(a)


#sayilar_2=[75,32,25,14,47] #insertion sort
def insertion(numbers):  #insertion amacı swap sayısını azaltmak
    
    sayilar_2=numbers
    length_1=len(sayilar_2)
    karsilastirma_sayisi=0
    yerdegistirme=0 #swap
    print(sayilar_2)
    for i in range(1,length_1):
        for j in range(i,0,-1):
            karsilastirma_sayisi+=1
            if (sayilar_2[j]<sayilar_2[j-1]):
                #degistirme
                yerdegistirme+=1
                temp=sayilar_2[j-1]
                sayilar_2[j-1]=sayilar_2[j]
                sayilar_2[j]=temp
    #print("sıralanmıs hali",sayilar_2)
    return sayilar_2

sayilar_1=get_n_random_integer(10)
sayilar_2=insertion(sayilar_1)
print("siralanmis",sayilar_2[0])
print("karsilastırma sayısı",sayilar_2[2])
print("yer degistirme sayisi",sayilar[1])


def get_mean_of_swap_in_insertion(numTrials,numInt):  #yer degistirme sayılarını karsılastırcaz liste halinde
    swap_sayilari=[]
    for i in range(numTrials):
        sayilar_1=get_n_random_integer(numInt)
        sayilar_2=insertion(sayilar_1)
        s_1=sayilar_2[2]
        swap_sayilari.append(s_1)

    mean_1=get_mean_for_n_integer(swap_sayilari)
    std_1=get_std_for_n_integer(swap_sayilari)

    return int(mean_1),int(std_1)


print(get_mean_of_swap_in_insertion(10,10))



def bubble(arr):
    n=len(arr)

    karsilastirma_sayisi=0
    yerdegistirme=0 #swap

    for i in range(n):
        karsilastirma_sayisi+=1
        for j in range(0,n-i-1):
            
            if(arr[j]>arr[j+1]):
                yerdegistirme+=1
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
    return yerdegistirme,karsilastirma_sayisi




sayilar_1=get_n_random_integer(10)
print("sıralanmamıs",sayilar_1)
swap_sayisi=bubble(sayilar_1)
print("sıralanmıs",sayilar_1)
print("yer degistirme sayisi",swap_sayisi)
#print("karsilastirma sayisi",swap_sayisi[1])



def get_mean_of_swap_in_bubble(numTrials,numInt):  #yer degistirme sayılarını karsılastırcaz liste halinde
    swap_sayilari=[]
    for i in range(numTrials):
        sayilar_1=get_n_random_integer(numInt)
        s_1=bubble(sayilar_1)
        swap_sayilari.append(s_1[0])

    mean_1=get_mean_for_n_integer(swap_sayilari)
    std_1=get_std_for_n_integer(swap_sayilari)

    return numInt,int(mean_1),int(std_1)

random.seed(100)
result_1=get_mean_of_swap_in_insertion(10,10)
random.seed(100)
result_2=get_mean_of_swap_in_bubble(10,10)
print("insertion",result_1)
print("bubblesort",result_1)



