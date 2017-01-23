try:
    raise Exception('hello','world')
except Exception as inpu:
    print(type(inpu))
    print(inpu)
    x,y=inpu.args
    print(x)
    print(y)
