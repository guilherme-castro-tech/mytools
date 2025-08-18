from math import floor, factorial

def comb(n:int,k:int)-> int:
    n_comb = factorial(n)//(factorial(n-k)*factorial(k))
    return n_comb

def ways_get_on_top(n:int)->int:
    '''
    We wanna develop an algorithm such that given a stair with n steps
    calculate how many ways a person could get on top if the person 
    may go up 1 or 2 steps. Basically find all sollutions of n = j.1 +k.2
    for j and k given n. 
    We can see j = n-2k
    For j >= 0 : n>=2k or k = {0,1,2,...,floor(n/2)} 
    in this way the number of sulutions is  floor(n/2) + 1
    '''
    number_solution = floor(n/2)+1
    '''
    However, this method gives the number of solutions, we don't want
    just the number of solutions, we also want their combinations
    for each pair (j,k) the combinations of j+k getting k elements gives 
    our final answer
    '''
    sum_terms = 0
    for k in range(0, floor(n/2)+1):
        j = n - 2*k
        sum_terms += comb(j+k, k)
    return sum_terms

n = int(input("Digite n: "))

print(f"Número de maneiras de subir a escada: {ways_get_on_top(n)}")