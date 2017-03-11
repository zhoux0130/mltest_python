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

print(numpredict.crossvalidate(numpredict.weightedKNN,data))



