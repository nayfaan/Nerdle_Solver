import itertools
from itertools import *

import re

def run(sol_string):
    length = 8
    for x in sol_string:
        if x not in "1234567890+-*/=":
            raise ValueError("Wrong string input.")
    if len(sol_string) <= 0 or len(sol_string) > length:
        raise ValueError("String length exceeded limit.")
    
    digits = set(sol_string)
    digits_iter = combinations_with_replacement(digits,length)
    
    all_combo=[]
    for ite in list(digits_iter):
        if len(set(ite)) == len(sol_string):
            all_combo.append(ite)
            
    all_perm = []
    for combo in all_combo:
        combo_perm_iter = list(permutations(combo,length))
        for x in combo_perm_iter:
            all_perm.append(x)
    
    all_equate = []
    all_perm_consecutive_symbols_removed = []
    for perm in all_perm:
        if not any(perm[i] == perm[i+1] and perm[i] in "+-*/=" for i in range(len(perm)-1)):
            all_perm_consecutive_symbols_removed.append(perm)
    for i, perm in enumerate(all_perm_consecutive_symbols_removed):
        all_perm_consecutive_symbols_removed[i] = re.sub('=','==',"".join(perm))
        
    for perm in all_perm_consecutive_symbols_removed:     
        try:
            if eval(perm):
                all_equate.append(re.sub("==","=",perm))
        except:
            pass
            
    return all_equate

if __name__ == "__main__":
    pass