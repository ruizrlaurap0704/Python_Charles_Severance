name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '): continue    
    words = line.split()
    hour = words[len(words)-2]
    counts[hour[0:2]] = counts.get(hour[0:2],0) + 1

for k,v in sorted(counts.items()):
    print(k,counts[k])

