class Myerror(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise Myerror(2*2)
except Myerror as e:
    print(e.value)




#raise Myerror('hello')
#raise Myerror(2*2)
