#!/bin/python3

# spmather
# 2025-11-27
# v 0.0.1

# problems
#    1) Doesn't seem to want to write one row at a time in a few ways I tried to write it
#    2) The csv stops at \ud800 and cannot write the remainder of the nested lists
#    3) The terminal can output the values, but writing data to txt errors out as well


from pathlib import Path
import csv

def printalluni():  # Public
    """Prints all unicode characters 0x0000 through 0xFFFF"""
    file         = Path('unicode.csv')
    txtfile      = Path('text.txt')
    header       = ["Decimal","Hexidecimal","UnicodeValue"]
    writeallrows = []
            
    # create unicode characters
    for value in range(0x10000):
        try:
            unicodechar = chr(value)
            hexvalue    = hex(value).split('x')[-1]
            #t.write(f"{value},{hexvalue},{unicodechar}")
            writeallrows.append([value,hexvalue,unicodechar])
        except:
            pass

    # output to the terminal
    for row in writeallrows:
        print(f"{row}")

    #print(f"{writeallrows}")

    with txtfile.open("a") as txtf:
        for row in writeallrows:
            print(f"{row}")
            txtf.write(f"{row}")

    # write contents to csv file
    # this will error out at character \ud800
    with open(file, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for row in writeallrows:
            writer.writerows(writeallrows)

    # read contents of csv to terminal
    try:
        with open(file, mode='w', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row)
    except:
        print(f"csv is blank")

    #print(f"Csv file created at {file}")

printalluni()

# fin