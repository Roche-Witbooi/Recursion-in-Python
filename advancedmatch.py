# Determines if given pattern matches the word
# Roche Witbooi (WTBROC002)
# 23 April 2022

def match(pattern,word):
    '''Compares pattern entered by the user to the word entered '''

    #terminates recursion when word or pattern have no values     
    if pattern =='' or word =='' :   
        return False
    #terminates if the pattern without ?/* match or pattern only ?/*
    elif pattern== word or pattern in['?','*'] or pattern.replace('*','')==word:
        return True
    else:
    #Removes the first letter if found in both the word and the pattern 
        if word[0]== pattern[0]:
            return match(pattern[1:],word[1:])
        
        #Removes the letter and ? from pattern and coressponding letter
        elif pattern[0] == '?':
            return match(pattern[1:],word[1:])
        
        elif pattern[0] == '*' and len(word)>1:
            #Removes the * pattern if pattern begins with #
            if pattern[1]==word[0] and pattern[0]=='*':
                return match(pattern[1:],word) 
                
            #Removes letter in both pattern and word if following letter correspond
            elif pattern[1]==word[1] or pattern[1]=='*':
                return match(pattern[1:],word[1:])   
            else:
            #Removes extra letters
                return match(pattern,word[1:])   