import sys
import os
import csv

def main():
    src_csv = sys.argv[1]
    dst_folder = sys.argv[2]
    # join custom drives with unc paths
    dst_temp = dst_folder.split("\\")
    if "S:" == dst_temp[0]:
        dst_temp[0] = "\\gothamtg.net\shares"
    elif "T:" == dst_temp[0]:
        dst_temp[0] = "\\cofs01.gothamtg.net\\templates"
    dst_folder = "\\".join(dst_temp)
    # convert csv to dictionary
    data_dict = {}
    with open(src_csv, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            key = row[0]
            value = row[1]
            data_dict[key] = value
    # build path recursivley using key,value pairs
    # Path is built out when the constructed path key 
    # has no cooresponding value (no parent directory)
    for key,val in data_dict.items():
        endPoint = key
        rel_path = ""
        while(endPoint != None):
            rel_path = os.path.join(rel_path,endPoint)
            endPoint = data_dict.get(endPoint)
        # path manipulation for accuracy
        path_sep = rel_path.split('\\')
        reversed_path_sep = reversed(path_sep)
        final_path = '\\'.join(reversed_path_sep)
        # avoids duplicate operations and errors raised
        try:
            os.makedirs(os.path.join(dst_folder,final_path), exist_ok=True)
        except Exception as e:
            print(e)

if __name__ == "__main__":
     main()
