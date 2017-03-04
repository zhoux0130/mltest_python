import sys, classifier
sys.path.append('./classifier.py')


c1=classifier.naivebayes(classifier.getwords)

c1.sampletrain()


#print(c1.fprob('quick','good'))

#print(c1.weightedprob('money','good', c1.fprob))
#c1.sampletrain()
#print(c1.weightedprob('money','good', c1.fprob))

print(c1.prob('quick rabbit','good'))
print(c1.prob('quick rabbit','bad'))