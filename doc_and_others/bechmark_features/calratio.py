while True:
    txt = input("一行数据：").replace("|", "")
    #print(txt)
    txt = txt.split()
    #print(txt)

    nvars = int(txt[0])
    nclauses = int(txt[1])
    nhards = int(txt[2])
    nsofts = int(txt[4])

    c_v = round(nclauses / nvars, 2)
    hc_v = round(nhards / nvars, 2)
    hc_sc = round(nhards / nsofts, 2)
    hc_c = round(nhards / nclauses, 2)


    print(str(c_v))
    print(str(hc_v))
    print(str(hc_sc))
    print(str(hc_c))
