import time
import sys
# recursion examples

# Example 1 - Fibonacci Series
inputnumber = 1000000

#----------with recursion------------#
'''
existingvalues = {}
def fib_series(n):
    if(n <= 1):
        return n
    else:
        if(n in existingvalues):
            value = existingvalues[n]
        else:
            value = fib_series(n-1) + fib_series(n-2)
            existingvalues[n] = value
        return value

sys.setrecursionlimit(100000)
starttime1 = time.time()
print(fib_series(inputnumber))
endtime1 = time.time()
print('Time elapsed-', 1000000000*(endtime1 - starttime1))
# print(existingvalues.values())
'''



#----------with iteration------------#
def fib_series(i):
    a = 0
    b = 1
    c = 0
    count = 0
    while (count < i):
        c = a + b
        a = b
        b = c
        count = count + 1
    print(c)

starttime2 = time.time()
fib_series(inputnumber-1)
endtime2 = time.time()
print('Time elapsed-', 1000*(endtime2 - starttime2))
