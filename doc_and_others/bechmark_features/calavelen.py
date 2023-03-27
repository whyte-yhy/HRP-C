
while True:
    inst_num = 0

    h_ave_len = 0
    s_ave_len = 0
    c_ave_len = 0

    nhards = 0
    nsofts = 0
    ncls = 0


    sentance=""
    while sentance != 'quit':
        inst_num += 1
        sentance = input("第"+str(inst_num)+"次输入：")
        if (sentance == 'quit'): break
        while len(sentance.split(" ")) != 5:
            sentance = input("第"+str(inst_num)+"次输入：")

        ncls = int(sentance.split(" ")[0])
        nhards = int(sentance.split(" ")[1])
        h_ave_len += float(sentance.split(" ")[2])
        nsofts = int(sentance.split(" ")[3])
        s_ave_len += float(sentance.split(" ")[4])
        c_ave_len += ((float(sentance.split(" ")[2]) * nhards + float(sentance.split(" ")[4]) * nsofts) / ncls)

    print('hard_len=' + str(round(h_ave_len/inst_num, 2)))
    print('soft_len=' + str(round(s_ave_len/inst_num, 2)))
    print('cls_len=' + str(round(c_ave_len/inst_num, 2)))
