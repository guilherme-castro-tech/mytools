from math import floor

def ways_get_on_top(n:int)->int:
    #We wanna develop an algorithm such that given a stair with n steps
    #calculate how many ways a person could get on top if the person 
    #may go up 1 or 2 steps. Basically find all sollutions of n = j.1 +k.2
    #for j and k given n. 
    #We can see j = n-2k
    #For j >= 0 : n>=2k or k = {0,1,2,...,floor(n/2)} 
    # in this way the number of sulutions is  floor(n/2) + 1
    ways = floor(n/2)+1
    
    return ways