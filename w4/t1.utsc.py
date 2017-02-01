def size(stk):
    tmp = Stack()
    count=0
    while (not stk.is_empty()):
        tmp.push(stk.pop)
        count+=1
    while (not tmp.is_empty()):
        skt.push(tmp.pop)
    return count


def fib(n):
    if(n==1 or n==2):
        return 1
    else:
        return fib(n-1)+fib(n-2)
