from math import sqrt

def pearson(v1, v2):
    sum1 = sum(v1)
    sum2 = sum(v2)
    sum1Sq = sum([pow(v,2) for v in v1])
    sum2Sq = sum([pow(v,2) for v in v2])
    
    pSum = sum([v1[i]*v2[i] for i in range(len(v1))])
    num = pSum - sum1*sum2/len(v1)
    den = sqrt((sum1Sq - pow(sum1,2)/len(v1))*(sum2Sq - pow(sum2,2)/len(v1)))
    
    if den == 0: return 0
    
    return 1-num/den

class bicluster:
    def __init__(self, vec,left=None,right=None,id=None,distance=None):
        self.left = left
        self.right = right
        self.id = id
        self.vec = vec
        self.distance = distance
    

def hcluster(rows):
    distances={}
    currentclustid=-1
    
    # init cluster class with the original row
    clust = [bicluster(row[i], id=i) for i in len(rows)]
    
    while len(clust) > 1:
        lowerpair = (0,1) #choose the first and second item as init node
        closest = pearson(clust[0].vec,clust[1].vec)
        
        for i in range(len(clust)):
            for j in range(i+1,len(clust)):
                if (clust[i].id,clust[j].id) not in distances: 
                    distances[(clust[i].id,clust[j].id)]=pearson(clust[i].vec,clust[j].vec)

                d=distances[(clust[i].id,clust[j].id)]             
                if(currentdistance < closest):
                    closest = currentdistance
                    lowerpair = (i,j)
                    
         # merge 2 closest bicluster into 1 bicluster
         
         
        
                
        
        
    
    
    
    