source_path = "compare_3.0new_and__satlc.txt"
target_path = "detail_results_3.0andsatlc18.txt"

source_file = open(source_path, "r")
target_file = open(target_path, "w")

win_dict = dict()


def extract_class(line):
    tmp_str = line.split("/")[-1]
    return tmp_str.split("-")[0]
    
    
def extract_score(line):
    score = 0
    if line.find("equal") != -1:
        score = 0
    if line.find("origin win") != -1:
        score = -1
    if line.find("now win") != -1:
        score = 1
    return score
    
    
def write_to_target(target):
    for key in win_dict:
        target.write(key + ": " + str(win_dict[key]) + "\n")
    target.write("\n")
    
    
for line in source_file:
    if line.find("MS18") != -1 and line.find("unweighted") != -1:
        tmp_key = extract_class(line)
        tmp_val = extract_score(line)
        if tmp_key not in win_dict:
            win_dict[tmp_key] = 0
        win_dict[tmp_key] += tmp_val


write_to_target(target_file)

source_file.close()
target_file.close()