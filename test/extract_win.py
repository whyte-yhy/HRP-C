import sys


class_list = ["mse21", "mse20", "mse19", "mse18"]
def get_class(line):
    global class_list
    tmp_class = None
    for cl in class_list:
        if line.find(cl) != -1:
            tmp_class = cl
            break
    return tmp_class
    

def get_family_and_status(line, of_class):
    tmp_family = None
    tmp_now_win = 0  # 0:equal, -1:fail, 1:win
    if "mse18" == of_class:
        pass
    else:
        tmp_family = line.split("/")[2]
        if line.find("equal") != -1:
            tmp_now_win = 0
        elif line.find("now win") != -1:
            tmp_now_win = 1
        else:
            tmp_now_win = -1
    return tmp_family, tmp_now_win
    

MS18_family_dict = dict()
MS19_family_dict = dict()
MS20_family_dict = dict()
MS21_family_dict = dict()
def put_class_family_and_status(family_and_status, of_class):
    global MS18_family_dict, MS19_family_dict, MS20_family_dict, MS21_family_dict
    container = dict()
    if "mse18" == of_class:
        container = MS18_family_dict
    elif "mse19" == of_class:
        container = MS19_family_dict
    elif "mse20" == of_class:
        container = MS20_family_dict
    elif "mse21" == of_class:
        container = MS21_family_dict
    family = family_and_status[0]
    status = family_and_status[1]
    if family in container:
        container[family] += status
    else:
        container[family] = status
        

def write_to_target(target):
    target.write("mse18:\n")
    for key in MS18_family_dict:
        target.write(key + ": " + str(MS18_family_dict[key]) + "\n")
    target.write("\n")

    target.write("mse19:\n")
    for key in MS19_family_dict:
        target.write(key + ": " + str(MS19_family_dict[key]) + "\n")
    target.write("\n")
    
    target.write("mse20:\n")
    for key in MS20_family_dict:
        target.write(key + ": " + str(MS20_family_dict[key]) + "\n")
    target.write("\n")
    
    target.write("mse21:\n")
    for key in MS21_family_dict:
        target.write(key + ": " + str(MS21_family_dict[key]) + "\n")
    target.write("\n")
    
        
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("error")
        sys.exit(1)
    
    file_path = "compare_3.0new_and__satlg.txt"
    file = open(file_path, "r")
    target_file = open("detail_results_" + sys.argv[1] + ".txt", "w")
    
    for line in file:
        ins_class = get_class(line)
        if ins_class=="mse18" or ins_class is None:
            continue
        ins_family_and_status = get_family_and_status(line, ins_class)
        put_class_family_and_status(ins_family_and_status, ins_class)
    
    write_to_target(target_file)
    file.close()
    target_file.close()
    
    
    
    