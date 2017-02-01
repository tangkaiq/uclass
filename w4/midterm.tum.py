def foo(i):
    if i>2:
        foo(i/2)
        foo(i/2)
        foo(i/2)
    print("foo")






def mysteryFunction(x):
    if not x:
        return []
    if x[0]%2==0:
        return [x[0]]+mysteryFunction(x[1:])
    else:
        return mysteryFunction(x[1:])+[x[0]]

 
class BinaryTree:
    def __init__(self,rootValue):
        self.root=rootValue
        self.left=None
        self.right=None


#tree=[5,[4,[11,[7,None,None],[2,None,None]],None],[8,13,[4,None,[1,None,None]]]]
#t=Node5
def count_nodes_in_binaryTree(t):
        if(t.left==t.right==None):
            return 1
        return 1+count_nodes_in_binaryTree(t.left)+count_nodes_in_binaryTree(t.right)

def has_path_sum(t,total):
    if(total==0) return True
    return(has_path_sum(t.left,total-t.value) or has_path_sum(t.right,total-t.value))


def removeDuplicates(head):
    start=head
    head=head.next
    while(head.next!=None):
        if(!head.element==head.next.element):
            head=head.next
        else:
            head.next=head.next.next
            if(head.next!=None):
                head=head.next

    return start


def is_circular(head):
    if(head.next==None) return False
    else return _is_circular(head.element,head.next)


def _is_circular(number,head):
    if(head.element==number) return True
    elif (head.next==None) return False
    else return _is_circular(number,head.next)
    
    

    
if __name__ == "__main__":

    foo(4)
    #print(mysteryFunction([1,3,5,2,4,6]))
