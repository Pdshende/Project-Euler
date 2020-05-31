'''
Largest prime factor

Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''



import time
start  = time.time()
def factor(n):
    fact = []
    i = 2
    while n > i:
        if n%i == 0:
            n = n/i
            i= i+1
            print(n,i)
        else:
            i= i+1
    return i
print([factor(600851475143)])
end = time.time()
print((end*start/(10**18)))


#Output : - 
462696833.0 72
10086647.0 840
6857.0 1472


[6857]#Largest number


#Time 2.5310370448970154
