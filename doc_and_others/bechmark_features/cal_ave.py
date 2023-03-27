inst_num = 0

nvars = 0
ncls = 0
nhards = 0
nhardlen = 0
nsofts = 0
nsoftlen = 0
soft_weight = 0

sentance=""
while sentance != 'quit':
    sentance = input("第"+str(inst_num+1)+"次输入：")
    if (sentance == 'quit'): break
    while len(sentance.split(" ")) != 7:
        sentance = input("第"+str(inst_num+1)+"次输入：")

    inst_num += 1
    nvars += int(sentance.split(" ")[0])
    ncls += int(sentance.split(" ")[1])
    nhards += int(sentance.split(" ")[2])
    nhardlen += float(sentance.split(" ")[3])
    nsofts += int(sentance.split(" ")[4])
    nsoftlen += float(sentance.split(" ")[5])
    soft_weight += float(sentance.split(" ")[6])


print("nvars=" + str(round(nvars/inst_num)))
print("ncls=" + str(round(ncls/inst_num)))
print("nhards=" + str(round(nhards/inst_num)))
print("nhardlen=" + str(round(nhardlen/inst_num)))
print("nsofts=" + str(round(nsofts/inst_num)))
print("nsoftlen=" + str(round(nsoftlen/inst_num)))
print("soft_weight=" + str(round(soft_weight/inst_num)))
