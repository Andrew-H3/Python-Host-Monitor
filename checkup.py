import time
import os


# debug level: 0 = least, 1 = some, 2 = more
debug = 0

# parse config file for parameters
def parseConfigFile():
    global Host
    global Interval
    global Notify
    global Address
    with open("checkup.conf", "r") as f:
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


def downToUp():
    print("Alert: Host came up!")

def upToDown():
    print("Alert: Host went down!")

# loop through checks
def loop():
    if debug >= 2:
        print("Starting loop")
    firstLoop = True
    command = "ping -c 1 "+Address+"> /dev/null 2>&1"
    if debug >= 2:
        print("State command:",command)
    while(True):
        state = os.system(command)
        if state == 0:
            if debug >= 1:
                print("Host is up")
        else:
            if debug >= 1:
                print("Host is down")

        if firstLoop:
            firstLoop = False
            lastState = state
        else:
            if lastState != state:
                if state:
                    upToDown()
                else:
                    downToUp()
            lastState = state

        if debug >= 2:
            print("Finished loop")
        time.sleep(Interval)

# get things going
def startUp():
    print("Initializing....")
    print("Parsing config file....")
    parseConfigFile()
    print("Starting...")
    loop()

startUp()
