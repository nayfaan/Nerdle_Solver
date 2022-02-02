import services.list_combo as list_combo
import services.match_colors as match_colors

def run():
    all_valid = "1280-*="
    
    all_sol = list_combo.run(all_valid)
    #sol = match_colors(all_sol)
    #print(sol)

if __name__ == "__main__":
    run()