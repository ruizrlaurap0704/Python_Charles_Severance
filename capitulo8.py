fname = input("Enter file name: ")
fh = open(fname)
#romeo.txt
lst = list()

for line in fh:
    words = line.split()
    for word in words:
        if word not in lst: lst.append(word)

lst.sort()
print(lst) 

fname = input("Enter file name: ")
#mbox-short.txt
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    count = count + 1
    print(words[1])

print("There were", count, "lines in the file with From as the first word")



