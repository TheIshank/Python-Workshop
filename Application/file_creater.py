from random import randint
import json
import argparse
import os.path
from os import path

parser = argparse.ArgumentParser()
parser.add_argument('number', default=100, help="Number of files that you want to create.", type=int)
args = parser.parse_args()

print("Creating " + str(args.number) + " files.")

succ_fail_dict = {}
total_file_count = args.number
counter = 0
while counter < total_file_count:
    file_number = randint(8469488, 948867375647487698906874676)
    if file_number not in succ_fail_dict:
        if file_number % 10 > 5:
            succ_fail_dict[file_number] = "Success"
        else:
            succ_fail_dict[file_number] = "Failure"
        f = open('file-' + str(file_number) + '-name.dat',"wb")
        f.seek(100-1)
        f.write(b"\0")
        f.close()
        counter += 1

json.dump(succ_fail_dict, open('success-failure-dict.json', 'w+'))