def division(a,b):
    try:
        answer = a/b
    except ZeroDivisionError:
        print('cannot divide by zero')
    except TypeError:
        print('Wrong Type')
    except NameError:
        print("name not difined inside")
    else:
        print('answer')
    finally:
        print('end')

division(6,0)
division(0,42)
division(100,50)
division('science',1)
division('science',0)
#ask prof about this
division(a,1)

try:
    division(x,1)
except NameError:
    print('Name not defined outside')
