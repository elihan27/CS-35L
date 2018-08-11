#!/usr/bin/python                                                                                                                                                                    

import sys, argparse

class comm:
    def __init__(self, filename1, filename2):
        f1  = open(filename1, 'r')
        f2 = open(filenam2, 'r')
        self.lines1 = f1.readlines()
        self.lines2  = f2.readlines()
        f1.close()
        f2.close()

def main():
    version_msg = "%prog 2.0"
    usage_msg = """%prog [OPTION]... FILE FILE                                                                                                                                       
                                                                                                                                                                                     
The python equivalent of the comm command!"""
    input_file1 = args[0]
    input_file2 = args[1]


    deFiles = comm(input_file1, input_file2)
    size1 = len(deFiles.lines1)
    size2 = len(deFiles.lines2)
    a=0
    b=0

    while (a < size1 or b < size2):
        tmp = compare(deFiles.lines1[a], deFiles.lines[b])
        if temp==0:
            print deFiles.lines1[a]
            a=a+1
            b=b+1
        elif tmp < 0:


       f2 = open(filenam2, 'r')
        self.lines1 = f1.readlines()
        self.lines2  = f2.readlines()
        f1.close()
        f2.close()

if __name__ == "__main__":
    main()
