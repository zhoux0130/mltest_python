class matchrow:
    def __init__(self,row,allnum=False):
        if allnum:
            self.data=[float(row[i]) for i in range(len(row)-1)]
        else:
            self.data=row[0:len(row)-1]
        self.match=int(row[len(row)-1])

def loadmatch(f,allnum=False):
    rows=[]
    for line in file(f):
        rows.append(matchrow(line.split(','),allnum))
    return rows

from pylab import *
def plotagematches(rows):
    xdm,ydm=[r.data[0] for r in rows if r.match==1],\
        [r.data[1] for r in rows if r.match==1]
    xdn,ydn=[r.data[0] for r in rows if r.match==0],\
        [r.data[1] for r in rows if r.match==0] 

    plot(xdm,ydm,'bo')
    plot(xdn,ydn,'b+')

    show()
    
def lineartrain(rows):
    averages={}
    counts={}
    
    for row in rows:
        cl=row.match
        average.setdefault(cl,[0.0]*(len(row.data)))
        