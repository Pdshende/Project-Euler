'''
Multiples of 3 and 5
Show HTML problem content  

Problem 1


If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

# To check time excexution I use time library for minimum time 

import time
start  = time.time()
print(sum(i for i in range(10001) if i%3 == 0 or i%5 == 0))
end = time.time()
print((end*start/(10**18)))


# Output:  233168
