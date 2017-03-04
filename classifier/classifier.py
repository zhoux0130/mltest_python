
import re
import math

def getwords(doc):
    splitter=re.compile('\\W*')
    print doc
    # Split the words by non-alpha characters
    words=[s.lower() for s in splitter.split(doc) 
           if len(s)>2 and len(s)<20]

    # Return the unique set of words only
    return dict([(w,1) for w in words])

class classifier:
    def __init__(self, features, file=None):
        self.fc = {}
        self.cc = {}
        self.features = features
          
    def incfc(self,f,cat):
        self.fc.setdefault(f,{})
        self.fc[f].setdefault(cat,0)
        self.fc[f][cat] += 1
    def incc(self, cat):
        self.cc.setdefault(cat,0)
        self.cc[cat] += 1
        
    def fcount(self, f, cat):
        if f in self.fc and cat in self.fc[f]:
            return float(self.fc[f][cat])
        return 0.0
    
    def catcount(self, cat):
        if cat in self.cc:
            return float(self.cc[cat])
        return 0.0
    def totalcount(self):
        return sum(self.cc.values()) #cc.values
    
    def categories(self):
        return self.cc.keys(); # cc.keys
    
    def train(self, item, cat):
        feature = self.features(item); #feature is what
        
        for f in feature:
            self.incfc(f, cat)
        
        self.incc(cat)
   
    #calculate the properbility of P(A|B)     
    def fprob(self, f, cat):
        if self.catcount(cat) == 0: return 0
        
        pb = self.catcount(cat)
        pa = self.fcount(f, cat)
        
        prob = pa/pb # float() ??
        return prob
        
    # reset prob by weight
    def weightedprob(self,f,cat,prf,weight=1.0,ap=0.5):
        basicprob = self.fprob(f,cat)
        totals=sum([self.fcount(f,c) for c in self.categories()])
        bp=((weight*ap)+(totals*basicprob))/(weight+totals)
        return bp
    
    def sampletrain(self):
        self.train('the quick brown fox jumps over the lazy dog', 'good')
        self.train('make quick money in the online casino', 'bad')
        self.train('Nobody owns the water', 'good')
        self.train('the quick rabbit jumps fences', 'good')
        self.train('buy pharmaceuticals now', 'bad')

class naivebayes(classifier):
    def docprob(self,item,cat):
        features=self.features(item)
        
        p = 1
        for f in features: p*=self.weightedprob(f,cat,self.fprob)
        return p
    
    # get P(A|B)*P(A) A:Category B:Document
    def prob(self, item, cat):
        catprob = self.catcount(cat)/self.totalcount()
        docprob = self.docprob(item, cat)
        return docprob*catprob
        