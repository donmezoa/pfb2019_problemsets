#!/usr/bin/env python3

import sys


# Define sys arguments
start_num = int(sys.argv[1])
end_num = int(sys.argv[2])

tables = range(start_num, end_num)

for table in tables:
	if table%2 != 0:
		print(table)








