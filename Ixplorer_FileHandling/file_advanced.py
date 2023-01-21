##################################################################
# 1 Kb small chunks 

with open('large_file.txt', 'r') as f:
    while True:
        chunk = f.read(1024)
        if not chunk:
            break
        print(chunk)
        
##################################################################
# glob to get all txt files in the directory 

import glob

txt_files = glob.glob('*.txt')

for file in txt_files:
    with open(file, 'r') as f:
        print(f.read()) 
        
##################################################################
# read .gz file using gzip library

import gzip

with gzip.open('compressed_file.gz', 'rb') as f:
    print(f.read())
    
##################################################################
