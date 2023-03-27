import networkx as nx
import community
import os


def cnf_to_graph(cnf_file):
    clauses = []
    with open(cnf_file, 'r') as f:
        for line in f:
            if line.startswith('c') or line.startswith('p'):
                continue
            clause = []
            literals = line.strip().split()
            for literal in literals[1:]:  # 过滤掉权重
                if literal == '0':
                    break
                clause.append(int(literal))
            clauses.append(clause)

    variables = set(abs(literal) for clause in clauses for literal in clause)
    graph = {variable: [] for variable in variables}

    for clause in clauses:
        for i in range(len(clause)):
            for j in range(i + 1, len(clause)):
                graph[abs(clause[i])].append(abs(clause[j]))
                graph[abs(clause[j])].append(abs(clause[i]))

    return graph


def computeMod(graph):
    # 创建一个无向图
    G = nx.Graph()

    # 向图中添加节点和边
    G.add_edges_from(graph)
    #G.add_edges_from(graph)
    
    # 使用Louvain算法计算模块度
    partition = community.best_partition(G)
    modularity = community.modularity(partition, G)

    #print("Partition: ", partition)
    print("Modularity: ", modularity)
    return modularity


def graph_dict_to_list(graph_dict):
    graph_list = list()
    for key in graph_dict:
        for val in graph_dict[key]:
            graph_list.append((key, val))
    return graph_list


def get_filepath_list():
    # 获取当前文件夹路径
    dir_path = os.getcwd()
    filepath_list = list()

    # 遍历文件夹下的所有文件
    for filename in os.listdir(dir_path):
        # 如果是文件，打印文件名
        if os.path.isfile(os.path.join(dir_path, filename)) and filename.endswith('.wcnf'):
            filepath_list.append(filename)
    return filepath_list

    
if __name__ == '__main__':
    mod_list = list()
    for filepath in get_filepath_list():
        graph_dict = cnf_to_graph(filepath)
        mod_list.append(computeMod(graph_dict_to_list(graph_dict)))


    sum_mod = 0    
    with open('mod_info.txt', 'a') as file1:
        for mod in mod_list:
            sum_mod += float(mod)
            file1.write(str(mod) + '\n')
        file1.write('\n' + str(sum_mod / len(mod_list)) + '\n')




















    



    
