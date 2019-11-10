import os

# debug level: 1 = some, 2 = more
debug = 1

with open("checkup.conf", "r") as f:
    i = 1
    for line in f:
        if line[0] == '#' or line[0] == ' ' or line[0] == '\n':
            pass
        else:
            if debug >= 2:
                print("parsing",line,end='')
            args = line.strip().split(" ")
            if debug >= 2:
                print("args",args)
            if args[0] == "Interval":
                if debug >= 1:
                    print("Setting Interval to",args[1])
                Interval = int(args[1])
            if args[0] == "Notify":
                if debug >= 1:
                    print("Will notify",args[1])
                Notify = args[1]
            if args[0] == "Host":
                if debug >= 2:
                    print("Adding host",args[1])
                parts = args[1].split("@")
                if debug >= 1:
                    print("Adding host",parts[0],"located at",parts[1])
                Host = parts[0]
                Address = parts[1]



        #print("line",i,":",line,end='')
        #i = i+1
    

