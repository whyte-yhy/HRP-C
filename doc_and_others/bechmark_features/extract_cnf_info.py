text = '''






'''

import re
import pyperclip as pc

nvars = re.findall(r'"nvars": (\d+),', text)[0]
ncls = re.findall(r'"ncls": (\d+),', text)[0]
nhards = re.findall(r'"nhards": (\d+),', text)[0]
nhard_len_ave = re.findall(r'"ave": (\d+\.\d+),\n', text)[0]
nsofts = re.findall(r'"nsofts": (\d+),', text)[0]
nsoft_len_ave = re.findall(r'"ave": (\d+\.\d+),\n', text)[1]
soft_wt_ave = re.findall(r'"ave": (\d+\.\d+),\n', text)[2]

mystr = nvars+" "+ ncls+" "+ nhards+" "+ nhard_len_ave+" "+ nsofts+" "+ nsoft_len_ave+" "+ soft_wt_ave
print(mystr)
pc.copy(mystr)
