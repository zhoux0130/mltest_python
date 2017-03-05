import sys, treepredict
sys.path.append('./treepredict.py')

tpredict = treepredict.decisionnode()
#print(tpredict.divideset(treepredict.my_data, 2, 'yes'))




tree=treepredict.buildtree(treepredict.my_data)
#treepredict.printtree(tree)

#print(treepredict.classify(['(direct)','USA','yes',5], tree))

treepredict.prune(tree,1.0)
treepredict.printtree(tree)