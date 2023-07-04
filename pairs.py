#Counts the number of consecutive letter pairs
#Roche Witbooi (WTBROC002)
#20 April 2022


def pairs_letters(s,n=0,pairs=0):
    '''Counts the number of conecutive same letters in a string entered by the user
    by compairing letters and adjacent indexes'''
    
    #Base-case which terminates recursion when reaches the end of string
    if len(s)-1<=n: 
        return pairs
    else:
    #Compares adjacent letters increases pairs if letters are the same
        if s[n]==s[n+1]:
            pairs+=1
            return pairs_letters(s,n+2,pairs)
        else:
            return pairs_letters(s,n+1,pairs)
    
#Obtains message from the user   
s = input('Enter a message:\n')     
print('Number of pairs:',pairs_letters(s))