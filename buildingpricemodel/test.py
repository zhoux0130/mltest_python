import sys,numpredict
sys.path.append('./numpredict.py')

print(numpredict.wineprice(95.0,3.0))
print(numpredict.wineprice(95.0,8.0))

print(numpredict.wineprice(99.0,1.0))

data =numpredict.winset1()
#print(data[0])
#print(data[1])

#print(numpredict.knnestimate(data, (95.0,3.0)))
#print(numpredict.knnestimate(data, (99.0,3.0)))
#print(numpredict.knnestimate(data, (99.0,5.0)))

#print(numpredict.wineprice(99.0,5.0))
#print(numpredict.knnestimate(data, (99.0,5.0), k=1))
print(numpredict.weightedKNN(data, (99.0,5.0)))

