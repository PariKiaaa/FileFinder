#This program will create a "result.txt" file
#If the file alreay exists, please delete its data, or just delete the file

import os
import string
import io
from ctypes import windll

#find all drives
def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    return drives

#just for test in some drives
# get_drives = ['E']

#choose the file extention
fo = 'abcdefg'

#for each folder in each drive, write the path of all files with "fo" format in the file "result.txt"
for drive in get_drives():
	for r, d, f in os.walk(f"{drive}:\\"):
	    for file in f:
	        filepath = os.path.join(r, file)
	        if fo in file:
	        	with io.open('result.txt','a',encoding="utf-8") as jpg:
	        		jpg.write(f'{os.path.join(r, file)}\n')
