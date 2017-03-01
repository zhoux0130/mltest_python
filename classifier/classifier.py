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
        self.cc.setdefault(cat,{})
        self.cc[cat] += 1
        
    def fcount(self, feature, cat):
        if feature in self.fc and cat in self.fc[f]:
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
        
        for f in featur:
            self.incfc(self, f, cat)
        
        self.incc(cat)
   
    #calculate the properbility of P(A|B)     
    def fprob(self, f, cat):
        pb = self.cc[cat]
        pa = self.fc[f][cat]
        
        prob = float(pa/pb) # float() ??
        
    # reset prob by weight
    def weightedprob(self,f,cat,prf,weight=1.0,ap=0.5):
        basicprob = fprob(f,cat)
        totals=sum([self.fcount(f,c) for c in self.categories()])
        bp=((weight*ap)+(totals*basicprob))/(weight+totals)
        return bp
    