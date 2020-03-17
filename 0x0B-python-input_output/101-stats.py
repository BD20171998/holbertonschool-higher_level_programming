#!/usr/bin/python3

import sys

stats = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0,
         '500': 0}

count = 0
filetotal = 0

try:

    for line in sys.stdin:
        a = line.split()
        filetotal += int(a[8])

        if count == 10:
            print("File size: {}".format(filetotal))
            for k, v in sorted(stats.items()):
                if v > 0:
                    print("{}: {}".format(k, v))
            count = 0

        if a[7] in stats.keys():
            stats[a[7]] += 1
            count += 1

except KeyboardInterrupt:
    print("File size: {}".format(filetotal))
    for k, v in sorted(stats.items()):
        if v > 0:
            print("{}: {}".format(k, v))
