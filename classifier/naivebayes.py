import sys, classifier
sys.path.append('./classifier.py')


#c1=classifier.naivebayes(classifier.getwords)
c1 = classifier.fisherclassifier(classifier.getwords)

c1.sampletrain()
#print(c1.weightedprob('money','bad', c1.cprob))

#print(c1.cprob('quick','good'))
#print(c1.fisherprob('quick rabbit','good'))


print(c1.classify('quick rabbit'))

print(c1.classify('quick money'))

c1.setminimum('bad', 0.8)
print(c1.classify('quick money'))

c1.setminimum('good', 0.4)
print(c1.classify('quick money'))


#print(c1.fprob('quick','good'))

#print(c1.weightedprob('money','good', c1.fprob))
#c1.sampletrain()
#print(c1.weightedprob('money','good', c1.fprob))
#print(c1.classify('quick money',default='unknow'))

#c1.setthreholds('bad', 3.0)

#print(c1.classify('quick money',default='unknow'))

#for i in range(10): c1.sampletrain()
#print(c1.classify('quick money',default='unknow'))
