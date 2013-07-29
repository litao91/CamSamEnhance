import os
import sys
from pScanImg import processScanImg
def main():
    in_dir = sys.argv[1]
    out_dir = sys.argv[2]
    for dir_path, subdir_list, file_list in os.walk(in_dir):
        for fname in file_list:
            full_path = os.path.join(dir_path, fname)
            out_path = os.path.join(out_dir, fname)
            print("Processing " + full_path)
            newImg = processScanImg(full_path)
            newImg.save(out_path)




if __name__ == "__main__":
    main()
