def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("divisioin by zero")
    else:
        print("result is ",result)
    finally:
        print("At finally")


divide(2,1)
divide(2,0)
divide("a","b")
