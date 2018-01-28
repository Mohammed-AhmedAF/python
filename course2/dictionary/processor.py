fname = "names.txt"
fhandle = open(fname)
namesList = list()
count = dict()

for line in fhandle:
	namesList = line.split()
	for name in namesList:
		count[name] = count.get(name,0) + 1

print(count)
