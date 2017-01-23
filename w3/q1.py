def f2(x):
    if x%2==1:
        raise ArithmeticError
    return x//2

def f1(x):
    while x>0:
        try:
            print(f2(x))
        except ArithmeticError:
            print('caught')
        finally:
            x=x-1
