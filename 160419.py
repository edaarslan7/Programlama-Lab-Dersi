#sınav sorusu noktalar ile ilgili olan

import random
def get_n_points(n):
    points=[]
    for i in range(n):
        x=random.randint(-10,10)
        y=random.randint(-10,10)
        points.append([x,y])
    return points

def get_center(points):
    x_s=[i for i,j in points]
    y_s=[j for i,j in points]

    x_c=sum(x_s)/len(x_s)
    y_c=sum(y_s)/len(y_s)
    return x_c,y_c

def get_distance(p_1,p_2):
    a=p_2[0]-p_1[0]
    b=p_2[1]-p_1[1]

    return (a**2+b**2)**.5

def mySelectionSort(points):
    n=len(points)
    center=get_center(points)
    s_1=0
    s_2=0
    for i in range(n):
        for j in range(i+1,n):
            a=get_distance(points[i],center)
            b=get_distance(points[j],center)
            s_1=s_1+1   #comprasion
            if(a>b):
                s_2=s_2+1   #swap
                temp=points[i]
                points[i]=points[j]
                points[j]=temp

    return points,s_1,s_2

points_1=get_n_points(10)
print(points_1)
print(mySelectionSort(points_1))


#son sinav sorusu
def maxVal(toConsider,avail):
    if(toConsider==[] or avail==0):
        result=(0,())#tuple,list,immutable
    elif(toConsider[0][2]>avail):
        result=maxVal(toConsider[1:],avail)
    else:
        nextItem=toConsider[0]
        withVal,withToTake=maxVal(toConsider[1:],avail-nextItem[2])
        withoutVal,withoutToTake=maxVal(toConsider[1:],avail)
        withVal=withVal+nextItem[1]
        if(withVal>withoutVal):
            result=(withVal,withToTake+(nextItem,))
        else:
            result=(withoutVal,withoutToTake)
    return result

item_1=['a',6,3]
item_2=['b',7,3]
item_3=['c',8,2]
item_4=['d',9,5]
items=[item_1,item_2,item_3,item_4]
print(maxVal(items,5))