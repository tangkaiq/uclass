def puzzle(lst):
  ''' (list of int) -> list of int
  
  Solve the puzzle.
  '''
  i = 0
  while i < len(lst) - 1:
    if lst[i] + 1 == lst[i + 1]:
      lst[i] = 2 * lst[i] + 1
      lst.pop(i + 1)
      i = 0
    else:
      i = i + 1
  return lst
  
if __name__ == '__main__':
    import time
    items = list(range(10000))

    # start the clock
    start = time.time()
    
    puzzle(items)
        
    end = time.time()
    print("It took ", end - start, "to solve the puzzle without using any ADTs")
  