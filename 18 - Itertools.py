# Itertools have two type of functions available : The first type is unbound iterator e.g. 
# - count, 
# - repeat and 
# - cycle, 
# the second type is more like : 
# - product,
# - permutation/combination types

import itertools as it
from time import sleep

def simulate(a):
    sleep(0.25)
    print(a) #print(a, end='') does not respect the delay. Why?
    print()
values = ['^_^', 'o_o', "'_'", 'O_O']
signal = it.cycle(values)
for _ in range(20):
	simulate(next(signal))
  
  '''
  It outputs :
  
  ^_^                                                                                                                              
                                                                                                                                 
  o_o                                                                                                                              
                                                                                                                                 
  '_'                                                                                                                              
                                                                                                                                 
  O_O                                                                                                                              
                                                                                                                                 
  ^_^                                                                                                                              
                                                                                                                                 
  o_o                                                                                                                              
                                                                                                                                 
  '_'                                                                                                                              
                                                                                                                                 
  O_O
  
  '''
