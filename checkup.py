import os

with open("checkup.conf", "r") as f:
    i = 1
    for line in f:
        if line[0] == '#' or line[0] == ' ' or line[0] == '\n':
            pass
        else:
            print(line,end='')
        #print("line",i,":",line,end='')
        #i = i+1
    

