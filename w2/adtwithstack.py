from stack import *


def puzzle2(lst):
  ''' (list of int) -> list of int
  
  Solve the puzzle.
  '''
  s = Stack()
  i = 0
  while i < len(lst):
    s.push(lst[i])
    match = True
    while match and not s.is_empty():
      right = s.pop()
      if s.is_empty():
        s.push(right)
        match = False
      else:
        left = s.pop()
        if left + 1 == right:
          s.push(left * 2 + 1)
        else:
          s.push(left)
          s.push(right)
          match = False
    i += 1
  
  lst = []
  while not s.is_empty():
    lst.append(s.pop())
  lst.reverse()
    
  return lst

if __name__ == '__main__':
    import time
    items = list(range(10000))

    # start the clock
    start = time.time()
    
    puzzle2(items)
        
    end = time.time()
    print("It took ", end - start, "to solve the puzzle using ADTs")

  
