import fileinput

import pdb

lines = []
for line in fileinput.input():
	lines.append(line)
pdb.set_trace()
print lines


