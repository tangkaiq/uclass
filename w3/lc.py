'''
#ex1
lst =  [1,2,3,4,5]
[element+5 for element in lst]

'''

'''
#ex2
for pair in (zip([1],[3,4])):
    print(pair)
'''

'''
#ex3
x=[1,2]
y=[3,8]
print([a*b for a,b in zip(x,y)])
'''

'''
#ex4
print([(x,y) for x in range(2) for y in range(3)])
'''

'''
#ex5
lst = [1,2,3,4]
less2 = [num for num in lst if (num<2)]
print(less2)
'''

'''
#ex6
def is_even(x):
    return x%2==0

print(list(filter(is_even,[1,2,3,4])))
'''

'''
#ex7
def is_even(x): 
    return x%2==0

print(['even' if is_even(x) else 'odd' for x in [1,2,3,4,5,6]])
'''
