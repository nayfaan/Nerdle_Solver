from services.list_combo import run as list_combo
from services.match_colors import run as match_colors

def run():
    all_valid = "1280-*="
    color_profile = {"Y": {0: "2",
                           1: "*",
                           2: "-",
                           3: "=8",
                           4: "=",
                           5: "",
                           6: "",
                           7: "1"},
                     "G": ["1",
                           "0",
                           "",
                           "",
                           "",
                           "",
                           "=",
                           "2"]}
    for color in color_profile.values():
        if not len(color) == length:
            raise ValueError("Color profile length mismatch.")
    
    all_sol = list_combo(all_valid, length)
    #print(all_sol)
    sol = match_colors(all_sol, color_profile)
    print(sol)

if __name__ == "__main__":
    length = 8
    run()