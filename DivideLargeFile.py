import os.path
import fileinput
import sys

print("""
Divide Large CSV File in Python
- Pass # Of Rows per file
- Pass Main File Name
- Ctr+C to interrupt at anytime
""")

filesize = int(input("Enter # of Rows for each file (e.g. 150000):"))
if filesize > 150000 or filesize == 0 or filesize < 0:
    sys.exit(f"\nError: Incorrect Filesize {filesize} entered.\n")


filename =  str(input("Enter Filename (e.g. juldec2016.csv): "))
if os.path.isfile(filename) == False:
    sys.exit(f"\nError: File {filename} Not Exist.\n")


fout = None
num_lines = sum(1 for line in open(filename))
print(f"Total # of Rows in {filename} = {num_lines}")
for (i, line) in enumerate(fileinput.FileInput(filename)):
    if i % filesize == 0:
        if fout: fout.close()
        fout = open('output/output%d.csv' % (i/filesize), 'w')
        num_lines = num_lines - filesize
        print(f"Current Filesize = {num_lines} --> Writing {filesize} rows to output{int(i/filesize)}.csv")
    fout.write(line)
fout.close()
