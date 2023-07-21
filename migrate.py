import sys
import os
import csv

def main():
    src_csv = sys.argv[1]
    dst_folder = sys.argv[2]
    data_dict = {}
    with open(src_csv, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            key = row[0]
            value = row[1]
            data_dict[key] = value
    for key,val in data_dict.items():
        endPoint = key
        rel_path = ""
        while(endPoint != None):
            rel_path = os.path.join(rel_path,endPoint)
            endPoint = data_dict.get(endPoint)
        path_sep = rel_path.split('\\')
        reversed_path_sep = reversed(path_sep)
        final_path = '\\'.join(reversed_path_sep)
        try:
            os.makedirs(os.path.join(dst_folder,final_path))
        except:
            print("already made " + os.path.join(dst_folder,final_path))
        #print(rel_path)


if __name__ == "__main__":
     main()