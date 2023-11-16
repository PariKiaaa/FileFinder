import os
import io
from ctypes import windll
import string

def get_drives():
    bitmask = windll.kernel32.GetLogicalDrives()
    drives = [letter for letter, mask in zip(string.ascii_uppercase, map(int, bin(bitmask)[:1:-1])) if mask]
    return drives

def scan_and_write_files(extension):
    target_files = []
    for drive in get_drives():
        for root, dirs, files in os.walk(f"{drive}:\\"):
            for file in files:
                if extension in file:
                    file_path = os.path.join(root, file)
                    target_files.append(file_path)

    with io.open('result.txt', 'a', encoding="utf-8") as result_file:
        result_file.write('\n'.join(target_files) + '\n')



file_extension = 'jpg'
scan_and_write_files(file_extension)
