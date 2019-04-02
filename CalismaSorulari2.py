#soru 2: tersten okunusu ile aynı olan kelimeleri test eden bir fonk yazınız.

def tersOkunus(myText):
     for i in myText:
        for j in reversed(myText):
            if(i==j):
                return True
            else:
                return False


print(tersOkunus('selam'))

def tersOkunus2(myText):
    if (myText == myText[::-1]):
        return True
    else:
        return False

print(tersOkunus2('sevimli'))
