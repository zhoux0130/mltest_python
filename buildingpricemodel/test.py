import sys,numpredict
sys.path.append('./numpredict.py')

print(numpredict.wineprice(95.0,3.0))
print(numpredict.wineprice(95.0,8.0))

print(numpredict.wineprice(99.0,1.0))

data =numpredict.wineset2()
#print(data[0])
#print(data[1])

#print(numpredict.knnestimate(data, (95.0,3.0)))
#print(numpredict.knnestimate(data, (99.0,3.0)))
#print(numpredict.knnestimate(data, (99.0,5.0)))

#print(numpredict.wineprice(99.0,5.0))
#print(numpredict.knnestimate(data, (99.0,5.0), k=1))
#print(numpredict.weightedKNN(data, (99.0,5.0)))
#print(numpredict.crossvalidate(numpredict.knnestimate,data))

def knn3(d,v):return numpredict.knnestimate(d,v,5)
#print(numpredict.crossvalidate(knn3,data))

#print(numpredict.crossvalidate(numpredict.weightedKNN,data))

#print(numpredict.probguess(data,[99,20],80,120))

#from pylab import *
#a=array([1,2,3,4])
#b=array([4,3,2,1])
#plot(a,b)
#show()


#t1=arange(0.0,10.0,0.1)
#plot(t1,sin(t1))

#show()

numpredict.probabilitygraph(data,(1,1),6)
