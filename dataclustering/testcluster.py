import sys,cluster
sys.path.append('./cluster.py')

blognames, words, data=cluster.readfile('blogdata.txt')
#clust = cluster.hcluster(data)
cluster.kcluster(data,4)

#cluster.printclust(clust, labels=blognames)


    
