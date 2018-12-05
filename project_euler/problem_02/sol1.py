'''
Problem:
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2,
the first 10 terms will be:
                1,2,3,5,8,13,21,34,55,89,..
By considering the terms in the Fibonacci sequence whose values do not exceed n, find the sum of the even-valued terms.
e.g. for n=10, we have {2,8}, sum is 10.
'''
from __future__ import print_function

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3

n = int(raw_input().strip())
i=1
j=2 
sum=0
while(j<=n):
    if j%2 == 0:
        sum+=j
    i , j = j, i+j
print(sum)
