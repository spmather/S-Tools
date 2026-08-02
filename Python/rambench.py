#!/bin/python3

# spmather
# 2025-04-30

# requires psutil installed:  Use $ pip install psutil or $ sudo apt install python3-psutil

rangelimit_var = 250000000

#######I#######S#######I#######D#######T#######
#######I#######S#######I#######D#######T#######

import datetime
import psutil

ramusage_list = []
ramusage_list.append(psutil.virtual_memory().used)
number_list   = []
start_var     = datetime.datetime.now()

#process a list of squares for every number up to -1 of the rangelimit_var variable set above
number_list = [value**2 for value in range(rangelimit_var)]

ramusage_list.append(psutil.virtual_memory().used)
end_var           = datetime.datetime.now()
timespent_var     = end_var - start_var
ramusagefinal_var = ( ramusage_list[1] - ramusage_list[0] ) / 1024 / 1024 / 1024

print(f"Worked on [{rangelimit_var}] number of squares\nCompleted in: [{timespent_var}] \nRAM used: [{ramusagefinal_var}] GB")

# notes:
#      1,000,000 uses  0.043 GB
#     10,000,000 uses  0.368 GB
#    100,000,000 uses  3.762 GB
#    250,000,000 uses  9.295 GB
#    500,000,000 uses 18.469 GB
#    750,000,000 uses 27.631 GB
#  1,000,000,000 uses 37.145 GB
#  2,000,000,000 uses 88.831 GB

# fin
