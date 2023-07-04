#Determines if sentence entered is a palindrome or not
#Roche Witbooi (WTBROC002)
#20 April 2022

def is_palindrome(s,i,n='',):
    ''' the string entered by the user and compares the  string 
    to original to determine if the sentence is a palindrome 
    (spelt the same originally and backwords)'''
    #Base-case if no sentence entered
    if s =='':
        return  s      
        
    #Terminates recursion when full string reversed
    elif i==-1 : 
        
    #Determines if sentence is a palindrome by comapring reversed sentence to sentence
        if s==n:
            return print('Palindrome!')
        else: 
            return print('Not a palindrome!') 
    else:
        #Build reversed sentence using indices
            n+=s[i]
            return is_palindrome(s,i-1,n)
       
            
#Obtains sentence from the user   
s = input('Enter a string:\n')
is_palindrome(s,len(s)-1)