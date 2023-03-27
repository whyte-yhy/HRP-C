filepath1 = 'solus/init_solu.txt'
filepath2 = 'solus/final_solu.txt'

targetfile1 = open('solus/init_positive.txt', 'w')
targetfile2 = open('solus/final_positive.txt', 'w')


with open(filepath1, 'r') as file1:
    for line in file1:
        for num in line.split(' '):
            if not num.startswith('-'):
                targetfile1.write(num + ' ')


with open(filepath2, 'r') as file2:
    for line in file2:
        for num in line.split(' '):
            if not num.startswith('-'):
                targetfile2.write(num + ' ')


targetfile1.close()
targetfile2.close()
