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
    
def euclidean(v1,v2):
    d=0.0
    for i in range(len(v1)):
        d+=(v1[i]-v2[i])**2
    return math.sqrt(d)    


def getdistance(data, vec1):
    distancelist =[]
    for i in range(len(data)):
        vec2=data[i]['input']
        distancelist.append((euclidean(vec1,vec2), i))
    distancelist.sort()
    
    return distancelist

def knnestimate(data,vec1,k=5):
    dlist=getdistance(data, vec1)
    avg =0.0
    for i in range(k):
        idx=dlist[i][1]
        avg+=data[idx]['result']
    avg=avg/k
    
    return avg

#the different way to caculate weight

def invertfun(dist, num=1.0, const=0.1):
    weight = num/(dist+const)
    return weight

def subtraction(dist, const=2.0, num=1.0):
    if dist > const:
        return 0
    else:
        weight=const-dist*num
    return weight

def gaussian(dist,sigma=5.0):
    return math.e**(-dist**2/(2*sigma**2))


def weightedKNN(data, vec1, k=5, weightf=invertfun):
    distancelist = getdistance(data, vec1)
    
    totalweight=0
    avg=0.0
    for i in range(k):
        idx=distancelist[i][1]
        dist=distancelist[i][0]
        totalweight+=weightf(dist)
        avg+=weightf(dist)*data[idx]['result']
    
    avg=avg/totalweight
    return avg       

def dividedata(data,test=0.05):
    trainset=[]
    testset=[]
    
    for row in data:
        if random() < test:
            testset.append(row)
        else:
            trainset.append(row)
    
    return trainset,testset
        
        
def testalgorithm(alf,trainset,testset):
    error=0.0
    for row in testset:
        guess=alf(trainset, row['input'])
        result=row['result']
        error+=(result-guess)**2
        
    return error/len(testset)


def crossvalidate(alf,data,trials=100,test=0.05):
    error=0.0
    for i in range(trials):
        trainset,testset=dividedata(data,test)
        error+=testalgorithm(alf, trainset, testset)
    
    return error/trials


def wineset2():
    rows=[]
    for i in range(300):
        rating=random()*50+50
        age=random()*50
        aisle=float(randint(1,20))
        bottlesize=[375.0,750.0,1500.0][randint(0,2)]
        price=wineprice(rating,age)
        price*=(bottlesize/750)
        price*=(random()*0.2+0.9)
        rows.append({'input':(rating,age,aisle,bottlesize),
                     'result':price})
    return rows

