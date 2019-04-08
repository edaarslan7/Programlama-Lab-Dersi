#soru 3: n*n tane karakteri n*n matrise atayan bir fonk yazınız.
#b)kendisine aktarılan bir kelimeyi bu matris üzerinde
#soldan sağa sağdan sola yukarıdan asagıya asagıdan yukarıya dogrultularında arayıp olup olmadıgını return eden fonk yazınız.

import math
def my_str_equal(s1,s2):
    if (s1 == s2):
        return True
    else:
        return False
def matriseAktarma(myText):
    matris = []

    print(len(myText))
    if(math.sqrt(len(myText)).is_integer()==True):
        n = int(math.sqrt(len(myText)))
        for i in range(n):
            matris += [[0] * n]
        for i in range(n):
            for j in range(n):
                matris[i][j] = 0

        k=0
        for i in range(n):
            for j in range(n):
                matris[i][j]=myText[k]
                k+=1
        return matris
            #print()
    else:
        print("Sayi nxn boyutta degildir...")
def get_my_words(w_m,i,j):
    m=len(w_m)
    n=len(w_m[0])



    t_1=""
    for k in range(j,n):
        t_1+=w_m[i][k]

    t_2=""
    for k in range(j,-1,-1):
        t_2+=w_m[i][k]

    t_3 = ""
    for k in range(i,m):
        t_3+=w_m[k][j]

    t_4=""
    for k in range(i, -1,-1):
        t_4 += w_m[k][j]

    return t_1,t_2,t_3,t_4
def varMi(w_m,w_1):
    m = len(w_m)
    n = len(w_m[0])
    bool_r=False
    for i in range(m):
        for j in range(n):
            r=get_my_words(w_m,i,j)
            if ( my_str_equal(w_1,r[0]) or my_str_equal(w_1, r[1]) or my_str_equal(w_1, r[2]) or my_str_equal(w_1, r[3]) ):
                bool_r=True
    return bool_r

a=matriseAktarma('canakkale')
print(a)

#------b şıkkı------

a=matriseAktarma('canakkale')
print(a)

r_1=get_my_words(a,0,0)
print(" --------- ")
print(r_1[0])
print(r_1[1])
print(r_1[2])
print(r_1[3])
print (" *************************************************************")
print(" SONUÇ : ")
print(varMi(a,"nke"))
