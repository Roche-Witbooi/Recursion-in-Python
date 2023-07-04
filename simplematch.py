# Determines if given pattern matches the word
# Roche Witbooi (WTBROC002)
# 20 April 2022

def match(pattern,word):
    '''Compares pattern entered by the user to the word entered '''
    
    #Terminates recursion when word or pattern have no values     
    if pattern =='' or word =='' or (word =='' and pattern =='') :   
        return False
    #Returns True if the pattern without ? matches  word or only on charater entered
    elif pattern== word :
        return True
    #
    elif len(word)==1 and pattern=='?':
        return True
        
    else:
    #Removes the first letter if found in both the word and the pattern and adds it the end of respective words
        if word[0]== pattern[0]:
            return match(pattern[1:]+pattern[0],word[1:]+word[0])
        
    #Removes the letter and ? from pattern and coressponding letter
        elif pattern[0] == '?':
            return match(pattern[1:],word[1:])
       
        
    
