import sys, optimization
sys.path.append('./optimization.py')

print(optimization.getminutes('19:54'))

#s=[1,4,3,2,7,3,6,3,2,4,5,3]


domain=[(0,9)]*(len(optimization.people)*2)
s=optimization.randomoptimize(domain, optimization.schedulecost)
print(optimization.schedulecost(s))
optimization.printschedule(s)