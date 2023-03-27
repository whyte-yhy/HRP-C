

import re
import pyperclip as pc


txtlist = list()


'''
txtlist.append('''


''')


'''

#=============================================

txtlist.append('''
c "nvars": 558350,
c "ncls": 2308011,
c "nhards": 2290789,
c "nhard_len_stats":
c    { "min": 1, "max": 11, "ave": 2.46,
c      "stddev": 0.56 },
c "nsofts": 17222,
c "nsoft_len_stats":
c    { "min": 1, "max": 1, "ave": 1.00,
c      "stddev": 0.00 },
c "nsoft_wts": 4,
c "soft_wt_stats":
c    { "min": 1, "max": 100, "ave": 6.81,
c      "stddev": 23.22 }

''')
txtlist.append('''
c "nvars": 239450,
c "ncls": 968374,
c "nhards": 959638,
c "nhard_len_stats":
c    { "min": 1, "max": 7, "ave": 2.47,
c      "stddev": 0.55 },
c "nsofts": 8736,
c "nsoft_len_stats":
c    { "min": 1, "max": 1, "ave": 1.00,
c      "stddev": 0.00 },
c "nsoft_wts": 4,
c "soft_wt_stats":
c    { "min": 1, "max": 100, "ave": 10.23,
c      "stddev": 28.72 }

''')
txtlist.append('''

c "nvars": 440296,
c "ncls": 1752998,
c "nhards": 1747114,
c "nhard_len_stats":
c    { "min": 1, "max": 6, "ave": 2.48,
c      "stddev": 0.52 },
c "nsofts": 5884,
c "nsoft_len_stats":
c    { "min": 1, "max": 1, "ave": 1.00,
c      "stddev": 0.00 },
c "nsoft_wts": 4,
c "soft_wt_stats":
c    { "min": 1, "max": 100, "ave": 12.71,
c      "stddev": 31.90 }
''')
txtlist.append('''
c "nvars": 287144,
c "ncls": 1140473,
c "nhards": 1136209,
c "nhard_len_stats":
c    { "min": 1, "max": 6, "ave": 2.48,
c      "stddev": 0.52 },
c "nsofts": 4264,
c "nsoft_len_stats":
c    { "min": 1, "max": 1, "ave": 1.00,
c      "stddev": 0.00 },
c "nsoft_wts": 4,
c "soft_wt_stats":
c    { "min": 1, "max": 100, "ave": 10.57,
c      "stddev": 29.17 }

''')
txtlist.append('''
c "nvars": 81096,
c "ncls": 305999,
c "nhards": 302414,
c "nhard_len_stats":
c    { "min": 1, "max": 7, "ave": 2.44,
c      "stddev": 0.55 },
c "nsofts": 3585,
c "nsoft_len_stats":
c    { "min": 1, "max": 1, "ave": 1.00,
c      "stddev": 0.00 },
c "nsoft_wts": 4,
c "soft_wt_stats":
c    { "min": 1, "max": 100, "ave": 14.37,
c      "stddev": 33.75 }

''')
txtlist.append('''

c "nvars": 29796,
c "ncls": 112003,
c "nhards": 110155,
c "nhard_len_stats":
c    { "min": 1, "max": 7, "ave": 2.45,
c      "stddev": 0.57 },
c "nsofts": 1848,
c "nsoft_len_stats":
c    { "min": 1, "max": 1, "ave": 1.00,
c      "stddev": 0.00 },
c "nsoft_wts": 4,
c "soft_wt_stats":
c    { "min": 1, "max": 100, "ave": 17.97,
c      "stddev": 37.18 }
''')
txtlist.append('''

c "nvars": 21771,
c "ncls": 84424,
c "nhards": 82777,
c "nhard_len_stats":
c    { "min": 1, "max": 7, "ave": 2.46,
c      "stddev": 0.58 },
c "nsofts": 1647,
c "nsoft_len_stats":
c    { "min": 1, "max": 1, "ave": 1.00,
c      "stddev": 0.00 },
c "nsoft_wts": 4,
c "soft_wt_stats":
c    { "min": 1, "max": 100, "ave": 19.06,
c      "stddev": 38.12 }
''')
txtlist.append('''
c "nvars": 17436,
c "ncls": 63254,
c "nhards": 62252,
c "nhard_len_stats":
c    { "min": 1, "max": 7, "ave": 2.45,
c      "stddev": 0.59 },
c "nsofts": 1002,
c "nsoft_len_stats":
c    { "min": 1, "max": 1, "ave": 1.00,
c      "stddev": 0.00 },
c "nsoft_wts": 4,
c "soft_wt_stats":
c    { "min": 1, "max": 100, "ave": 29.57,
c      "stddev": 44.73 }

''')
txtlist.append('''
c "nvars": 7010,
c "ncls": 26097,
c "nhards": 25466,
c "nhard_len_stats":
c    { "min": 1, "max": 6, "ave": 2.46,
c      "stddev": 0.60 },
c "nsofts": 631,
c "nsoft_len_stats":
c    { "min": 1, "max": 1, "ave": 1.00,
c      "stddev": 0.00 },
c "nsoft_wts": 4,
c "soft_wt_stats":
c    { "min": 1, "max": 100, "ave": 29.70,
c      "stddev": 44.76 }

''')
txtlist.append('''
c "nvars": 13155,
c "ncls": 49456,
c "nhards": 48552,
c "nhard_len_stats":
c    { "min": 1, "max": 7, "ave": 2.44,
c      "stddev": 0.56 },
c "nsofts": 904,
c "nsoft_len_stats":
c    { "min": 1, "max": 1, "ave": 1.00,
c      "stddev": 0.00 },
c "nsoft_wts": 4,
c "soft_wt_stats":
c    { "min": 1, "max": 100, "ave": 17.94,
c      "stddev": 37.18 }

''')







for text in txtlist:

    ncls = re.findall(r'"ncls": (\d+),', text)[0]
    nhards = re.findall(r'"nhards": (\d+),', text)[0]
    nhard_len_ave = re.findall(r'"ave": (\d+\.\d+),\n', text)[0]
    nsofts = re.findall(r'"nsofts": (\d+),', text)[0]
    nsoft_len_ave = re.findall(r'"ave": (\d+\.\d+),\n', text)[1]


    mystr = ncls+" "+ nhards+" "+ nhard_len_ave+" "+ nsofts+" "+ nsoft_len_ave
    print(mystr)
    #pc.copy(mystr)
