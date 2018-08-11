#!/usr/bin/python                                                               


import sys, argparse

class comm:
    def __init__(self, filename1, filename2):
        if filename1 == '-':
            self.lines1  = sys.stdin.readlines()
            f2 = open(filename2, 'r')
            self.lines2 = f2.readlines()
            f2.close()
        elif filename2 == '-':
            f1 = open(filename1, 'r')
            self.lines2  = sys.stdin.readlines()
            self.lines1 = f1.readlines()
            f1.close()
        else:
            f1  = open(filename1, 'r')
            f2 = open(filename2, 'r')
            self.lines1 = f1.readlines()
            self.lines2  = f2.readlines()
            f1.close()
            f2.close()
    def comm_print1(self, line, suppress):
        if not(suppress):
            sys.stdout.write(line)
    def comm_print2(self, line, suppress2, suppress1):
        if not(suppress2) and not(suppress1):
            sys.stdout.write("\t%s"%line)
        if not(suppress2) and (suppress1):
            sys.stdout.write(line)
        
    def comm_print3(self, line, suppress, suppress1, suppress2):
        if not(suppress) and not(suppress1) and not(suppress2): #the normal case
            sys.stdout.write("\t\t%s"%line)  
        if not(suppress) and (suppress1 != suppress2): #if suppress 1 column
            sys.stdout.write("\t%s"%line)
        if not(suppress) and (suppress1 and suppress2):
            sys.stdout.write(line)
            
             
    

def main():
    version_msg = "%prog 2.0"
    usage_msg = """%prog [OPTION]... FILE FILE                                
                                                                                
The python equivalent of the comm command!"""

    parser = argparse.ArgumentParser()
    parser.add_argument("file1", help= "the first file to compare")
    parser.add_argument("file2", help= "the second file to compare")
    parser.add_argument("-1", "--suppress1", action="store_true", help= "suppress column 1 (lines unique to file1)")
    parser.add_argument("-2", "--suppress2", action="store_true", help= "suppress column 2 (lines unique to file2)")
    parser.add_argument("-3", "--suppress3", action="store_true", help= "suppress column 3 (lines unique to file3)")
    parser.add_argument("-u", "--unsorted", action="store_true", help= "sort files, then compare line by line")

    args = parser.parse_args()


    input_file1 = args.file1
    input_file2 = args.file2
    deFiles = comm(input_file1, input_file2)
    size1 = len(deFiles.lines1)
    size2 = len(deFiles.lines2)
    
    A=args.suppress1
    B=args.suppress2
    C=args.suppress3

    a=0
    b=0
    c=0

    count=0
 

    if args.unsorted:
        while (a!=size1):
            temp= deFiles.lines1[a]
            b=0
            while (b!=size2):
                if temp== deFiles.lines2[b]:
                    if count==0:
                        deFiles.comm_print3(temp,C, A, B)
                    count=count+1
                    del deFiles.lines2[b]
                    size2= size2-1
                b=b+1
            if count==0:
                deFiles.comm_print1(temp, A)
            a=a+1
            count=0
#        sys.stdout.write("\n")
        b=0
        while (b!=size2):
            deFiles.comm_print2(deFiles.lines2[b], B, A)
            b=b+1
#        sys.stdout.write("\n")
        

    else:
        while (a!=size1 and b!=size2):
  #          if a ==3:
#                print deFiles.lines1[a],
 #               print deFiles.lines2[b]
            if deFiles.lines1[a] == deFiles.lines2[b]:
               # if (a==0) or (deFiles.lines1[a-1]!
                deFiles.comm_print3(deFiles.lines1[a],C, A, B)
                a=a+1
                b=b+1
#                print "currentsize a = ",
 #               print a
  #              print "currentsie b = ",
   #             print b

            elif deFiles.lines1[a] < deFiles.lines2[b]:
                #if (a==0) or (deFiles.lines1[a-1]!= deFiles.lines1[a]):
                deFiles.comm_print1(deFiles.lines1[a], A)
                a=a+1
    #            print "currentsize a = ",
     #           print a

            else:
               # if (b==0) or (deFiles.lines2[b-1]!= deFiles.lines2[b]):
                deFiles.comm_print2(deFiles.lines2[b], B, A)
                b=b+1
#                print "currentsize b = ",
 #               print b
#            print "current size1 = ",
 #           print a
  #          print "current size2 = ",
   #         print b


        while (a!=size1):
            deFiles.comm_print1(deFiles.lines1[a], A)
            a=a+1
        while (b!=size2):
            deFiles.comm_print2(deFiles.lines2[b], B, A)
            b=b+1

if __name__=="__main__":
    main()
