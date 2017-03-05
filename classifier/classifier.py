#from pysqlite2 import dbapi2 as sqlite
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
        
    #def setdb(self,dbfile):
        #self.con=sqlite.connect(dbfile)    
        #self.con.execute('create table if not exists fc(feature,category,count)')
        #self.con.execute('create table if not exists cc(category,count)')
          
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
    def weightedprob(self,f,cat,prf,weight=1,ap=0.5):
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
    
    def __init__(self, getfeatures):
        classifier.__init__(self, getfeatures)
        self.thresholds={}
        
    def setthreholds(self,cat,t):
        self.thresholds[cat] = t
        
    def getthreholds(self,cat):
        if cat not in self.thresholds: return 1.0
        return self.thresholds[cat]
    
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
        
    def classify(self, item, default=None):
        probs={}
        #get prob max category
        max = 0.0
        for cat in self.categories():
            probs[cat] = self.prob(item,cat)
            if probs[cat]>max:
                max = probs[cat]
                best = cat
                
        for cat in probs:
            if cat == best: continue
            if probs[cat]*self.getthreholds(best)>probs[best]:return default
            
        return best
    
class fisherclassifier(classifier):
    def cprob(self, f, cat):
        clf = self.fprob(f,cat)
        
        if clf == 0: return 0
        
        freqsum = sum([self.fprob(f, c) for c in self.categories()])
        
        p = clf/freqsum
        return p
    
    #def fisherprob(self, item, cat):
        #p = 1
        #features = self.features(item)
        #for f in features:
            #p*=(self.weightedprob(f, cat, self.cprob))
        
        #fscore=-2*math.log(p)
        #return self.invchi2(fscore, len(features)*2)
    
    #def invchi2(self, chi, df):
        #m = chi / 2.0
        #sum = term = math.exp(-m)
        #for i in range(1, df//2):
            #term *= m/i
            #sum += term
        #return min(sum, 1.0)
        
    def fisherprob(self,item,cat):
        # Multiply all the probabilities together
        p=1
        features=self.features(item)
        for f in features:
            p*=(self.weightedprob(f,cat,self.cprob))
    
        # Take the natural log and multiply by -2
        fscore=-2*math.log(p)
    
        # Use the inverse chi2 function to get a probability
        return self.invchi2(fscore,len(features)*2)
      
    def invchi2(self,chi, df):
        m = chi / 2.0
        sum = term = math.exp(-m)
        for i in range(1, df//2):
            term *= m / i
            sum += term
        return min(sum, 1.0)   
    def __init__(self, features):
        classifier.__init__(self, features)
        self.minimums = {}
    
    def setminimum(self, cat, min):
        self.minimums[cat] = min
        
    def getminimum(self,cat):
        if cat not in self.minimums: return 0
        return self.minimums[cat]    
         
    def classify(self, item, default=None):
        best = default
        max = 0.0
        for c in self.categories():
            p=self.fisherprob(item, c)
            if p>self.getminimum(c) and p>max:
                max = p
                best = c
        return best