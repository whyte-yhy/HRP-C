var_table = open('var_table.txt', 'r')
placingfile1 = open('solus/init_positive.txt', 'r')
placingfile2 = open('solus/final_positive.txt', 'r')


var_dict = dict()

print('init placing var table:')
for line in var_table:
    if line.startswith('c'):
        continue
    val_key = line.split(':')
    var_dict[val_key[1][:-1]] = val_key[0]

for line in placingfile1:
    for key in line.split(' '):
        if key == '':
            continue
        print(var_dict[key], end=' ')

print('\n===========================\n')

print('final placing var table:')
for line in placingfile2:
    for key in line.split(' '):
        if key == '':
            continue
        print(var_dict[key], end=' ')
        


var_table.close()
placingfile1.close()
placingfile2.close()
