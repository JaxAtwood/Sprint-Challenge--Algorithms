'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) < 2: #checks if less than 2 cannot be a th
        return 0 #returning the count of zero (occurances)
    
    if word[:2] == "th": #takes first two characters
        #colon first means take the first 2
        #theater
        return 1 + count_th(word[2:])
        #colon after means leave out the first 2
        #if it's a match, runs the return will send back everything but what was sliced (first 2 letters)
    else:
        return count_th(word[1:])        
