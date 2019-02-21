import os
import datetime
import yaml
from pprint import pprint

BUS_TIME = '時刻表.yml'

with open(BUS_TIME, 'r') as f:
    busdata = yaml.load(f)

times = datetime.datetime.now().strftime("%H:%M").split(":")

ocl = int(times[0])
minn = int(times[1])
if ocl in busdata:
    minlist = busdata[ocl]
    for index,minute in enumerate(minlist):
        if minute-1 > minn:
            print(minlist[index])
        elif minute-1 >= minn:
            print(minlist[index+1])
            break
        else:
            print("乙")


print(minlist)
print(times)
