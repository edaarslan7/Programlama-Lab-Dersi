#soru 1: bir fonksiyona text,string 2 parametre aktarılıyor -> list string search
#a)string text te var ise true ya da false dönderen bir fonk yaz.
#b)string varsa textte bulundugu ilk baslangıc konumunu dönderen fonk yaz
#c)ikinci gönderilen parametre birinci paramtereden n defa bulunuyorsa bulundugu yerlerin baslangıc adreslerini liste hlainde geri dönderen fonks yaz.

myText='Best Of Fitness'
#print(str(myText[2]+myText[3]))

def varMi(myText, myString):
    a=False
    for i in range(len(myText)-1):
        temp = None
        for j in range(len(myString)):
            #print(temp)
            temp=myText[i]
            for k in range(len(myString)-1):
                temp += myText[i+k+1]

        if(str(temp)==myString):
            a=True
            break

    return a
#print(varMi(myText,' Fitnes'))

def ilkKonum(myText, myString):
    for i in range(len(myText) - 1):
        temp = None
        for j in range(len(myString)):
            # print(temp)
            temp = myText[i]
            for k in range(len(myString) - 1):
                temp += myText[i + k + 1]

        if (str(temp) == myString):
            break

    return i

#print(ilkKonum(myText,'st'))

def kacDefa(myText,myString):
    n=[]
    if(len(myString)==1):
        for i in range(len(myText)):
            for j in range(len(myString)):
                if(myText[i]==myString[j]):
                    n.append(i)
    else:
        for i in range(len(myText) - 1):
            temp = None
            for j in range(len(myString)):
                # print(temp)
                temp = myText[i]
                for k in range(len(myString) - 1):
                    temp += myText[i + k + 1]
            if (str(temp) == myString):
                n.append(i)
    return n

print(kacDefa(myText,'ss'))