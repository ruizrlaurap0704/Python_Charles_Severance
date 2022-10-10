
fname = input("Enter file name: ")
#words.txt
fh = open(fname)

count = 0
for line in fh:
    count = count + 1
    print('Line Count:', count)

for line in fh:
    lineS = line.rstrip()
    print(lineS.upper())

from itertools import count
fname = input("Enter file name: ")
#mbox-short.txt
fh = open(fname)
c = 0
a = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    number = float(line[-7:])
    c = c + 1
    a = a + number
avg = a / c
print("Average spam confidence:",avg)

