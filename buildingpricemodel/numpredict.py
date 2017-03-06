from random import random,randint
import math

def wineprice(rating, age):
    peak_age = rating-50
    
    price = rating/2
    if age > peak_age:
        price=price*(5-(age-peak_age))
    else:
        price=price*(5*(age+1)/peak_age)
    
    if price<=0: price=0
    return price

#build data set for wing
def winset1():
    rows=[]
    for i in range(300):
        rating=random()*50+50
        age=random()*50
        
        price=wineprice(rating, age)
        
        price*=(random()*0.4+0.8)
        rows.append({'input':(rating, age),'result':price})
    return rows

def euclidean(v1, v2):
    d=0.0
    for i in range(len(v1)):
        d+=(v1[i]*v2[i])**2 #**: 3**2=3*3=9  3**3=3*3*3=27
    return math.sqrt(d)