# Itertools have two type of functions available : The first type is unbound iterator e.g. 
# - count, 
# - repeat and 
# - cycle, 
# the second type is more like : 
# - product,
# - permutation/combination types

import itertools as it
from time import sleep

values = ['^_^', 'o_o', "'_'", 'O_O']

def simulate(a):
    sleep(0.5)
    print(a) #print(a, end='') does not respect the delay. Why?
    print()

signal = it.cycle(values)
for _ in range(20):
	simulate(next(signal))
  
'''
It outputs the following with a nice 1/2 second delay :

^_^                                                                                                                              

o_o                                                                                                                              

'_'                                                                                                                              

O_O                                                                                                                              

^_^                                                                                                                              

o_o                                                                                                                              

'_'                                                                                                                              

O_O

'''
