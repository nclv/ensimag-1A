import sys
import os

def extractPrimitives(fileName, destName):
    f = open(fileName, "r")
    print("Needed primitives:")
    print("------------------")
    br = False
    cnt = 0
    while (not br):
        line = f.readline()
        if 'Primitives' in line:
            br = (cnt == 1)
            cnt += 1
    f.readline()
    f.readline()
    line = f.readline()
    while (line != "\n"):
        print(line[:-1])
        line = f.readline()
    f.close()

def extractUtilization(fileName, destName):
    f = open(fileName, "r")
    print("Real utilization:")
    print("-----------------")
    for line in f.readlines():
        if 'Slice LUTs' in line:
            number  = line.split("|")[2].strip()
            perc    = line.split("|")[5].strip()
            print("LUT6s : {} ({}%)".format(number, perc))
        if 'Register as Flip Flop' in line:
            number  = line.split("|")[2].strip()
            perc    = line.split("|")[5].strip()
            print("Flops : {} ({}%)".format(number, perc))
        if ('Block RAM Tile' in line)  and ('Note' not in line):
            number  = line.split("|")[2].strip()
            perc    = line.split("|")[5].strip()
            print("BRAMs : {} ({}%)".format(number, perc))
        if 'DSPs' in line:
            number  = line.split("|")[2].strip()
            perc    = line.split("|")[5].strip()
            print("DSPs  : {} ({}%)".format(number, perc))
    f.close()
    print("")

def extractClock(fileName):
    f = open(fileName, "r")
    clock = ''
    slack = ''
    for line in f.readlines():
        if 'Clock' in line:
            clock = float(line.split("|")[1].strip())
        if 'Slack' in line:
            slack = float(line.split("|")[1].strip())
    f.close()
    print("Timing analysis:")
    print("----------------")
    if (clock == '' or slack == ''):
        print("No clock was found in design.\n")
        return
    path = (clock-slack)
    freq = (1.0/(path*pow(10, -9)))/pow(10,6)
    print("Clock : %4.2f ns" % clock)
    print("Slack : %4.2f ns" % slack)
    print("Path  : %4.2f ns" % path)
    print("Freq  : %4.2f MHz" % freq)

if __name__=="__main__":
    if (len(sys.argv) != 4):
        sys.exit("Usage python parse_report.py <utilizationReport> <timingReport> <destinationReport>")
    print("\n--------- Résumé ----------\n")
    extractClock(sys.argv[3])
    extractUtilization(sys.argv[1], sys.argv[3])
    extractPrimitives(sys.argv[1], sys.argv[3])
