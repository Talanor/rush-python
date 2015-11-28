#!/bin/python3

import os
import re

def to_delete(f):
    try:
        return re.compile(".*~|#.*#").findall(f)[0]
    except IndexError:
        return None

def clean_dir(abs_path):
    curr_files = os.listdir(abs_path)
    for f in curr_files:
        cur_path = os.path.join(abs_path, f)
        if os.path.isdir(cur_path):
            clean_dir(cur_path)
        elif to_delete(f):
            os.remove(cur_path)

def main():
    clean_dir(os.getcwd())
    
if __name__ == "__main__":
    main()
