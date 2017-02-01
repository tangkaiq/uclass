a=[1,2,3]
b=[1,2,3]
#(a,b) = 1+4+9=14
def dotProduct(a,b):
    if(a==b==[]):
        return 0
    #if(len(a)!=len(b)) raise UnequalLists
    return a[0]*b[0]+dotProduct(a[1:],b[1:])

#print(dotProduct(a,b))


#(a,b)=[2,4,6]
def addTwoLists(a,b):
    if(a==b==[]):
        return []
    #if(len(a)!=len(b)) raise UnequalLists
    return [a[0]+b[0]]+addTwoLists(a[1:],b[1:])
#print(addTwoLists(a,b))
