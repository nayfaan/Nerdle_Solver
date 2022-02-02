from copy import deepcopy as dcopy

def run(sol_list, color_profile):
    all_match = []
    for sol in sol_list:
        for i, val in enumerate(color_profile['G']):
            if sol[i] in val:
                all_match.append(sol)
                
    temp = dcopy(all_match)
    all_match = []
    for sol in temp:
        for i, val in color_profile['Y'].items():
            if sol[i] not in val:
                all_match.append(sol)
    
    return all_match

if __name__ == "__main__":
    run()