'''
Largest palindrome product

Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''


import time
start  = time.time()
def palindeomic_number(n):
    number_to_string = str(n)
    number_to_string.split()
    number_to_string = number_to_string[:]
    reverse_order = number_to_string[::-1]
    return number_to_string == reverse_order

largest_number = 0
for i in range(100,1000):
    for j in range(100,1000):
        multiply = i*j
        if palindeomic_number(multiply) and  multiply > largest_number:
            largest_number = multiply
print(largest_number)
end = time.time()
print("The total excecution Time for this code is ", end*start/(10**18))



# Output : - 

906609
The total excecution Time for this code is sec 2.531050168661923

