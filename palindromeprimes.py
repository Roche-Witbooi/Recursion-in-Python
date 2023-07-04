#Determines and displays numbers in range entered theat are palindromes and prime
#Roche Witbooi (WTBROC002)
#21 April 2022
import sys
sys.setrecursionlimit (30000)

def is_palidrome(n): 
    if n==n[::-1]:
        return True
    else:
        return False
    

def is_prime(n,factor=2):

    if n < 2:
        
        return False
    else:
        if n==factor:

            return True
        else:
            if n == 2: 
                return True
            elif n% factor == 0:
           
                return False
            else:
                return is_prime(n,factor+1)
           
           
def is_palindrome_prime(n='x',m='x'):
    if n=='x'or m =='x' or n>m:
        return False
    elif is_palidrome(str(n)):
        
        if is_prime(n):
            print(n)
            
            is_palindrome_prime(n+1,m)
        else:
            is_palindrome_prime(n+1,m)            
    else:
        is_palindrome_prime(n+1,m)
        
    
#Obtains the values for the range of numbers    
N = eval(input('Enter the starting point N: \n'))
M = eval(input('Enter the ending point M: \n'))
print('The palindromic primes are:')
is_palindrome_prime(N,M)