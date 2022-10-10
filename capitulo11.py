"""
import re
hand = open('mbox-short.txt')

for line in hand:
    line = line.rstrip()
    x = re.findall('\S+@\S+', line)
    if len(x) > 0:
        print(x)

for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(x) > 0:
        print(x) 
"""
import re
hf = open('c11.txt')

suma = 0
count = 0
for line in hf:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    
    for number in x:
        suma = suma + int(number)
        count = count + 1

print(suma)
print(count)
