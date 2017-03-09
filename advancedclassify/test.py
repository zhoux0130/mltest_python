import sys,advancedclassify
sys.path.append('./advancedclassify.py')

agesonly=advancedclassify.loadmatch('agesonly.csv', allnum=True)

advancedclassify.plotagematches(agesonly)