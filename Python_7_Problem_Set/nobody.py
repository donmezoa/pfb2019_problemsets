#!/usr/bin/env python3

import re




with open ("Python_07_nobody.txt","r") as nobody:
	for line in nobody:
		line = line.rstrip()
		found=re.findall(r"Nobody",line)
		if found:
#			print(found)
			replaced = line.replace("Nobody","Billy")
			print(replaced)

