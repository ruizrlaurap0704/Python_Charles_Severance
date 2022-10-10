"""
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close() 

counts = dict()
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')
for line in fhand:
    print(line.decode().strip())
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)


# To run this, previously install BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

sum = 0
spans = soup('span')
for span in spans:    
    sum = sum + int(span.contents[0])
print(sum)
""" 
#Test: https://py4e-data.dr-chuck.net/known_by_Fikret.html
#Real: https://py4e-data.dr-chuck.net/known_by_Neve.html
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 0
position = 18
url = 'https://py4e-data.dr-chuck.net/known_by_Neve.html'
print(url)

while count < 7:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    ass = soup('a')

    count1 = 0
    for a in ass:
        count1 = count1 + 1
        if count1 == position:
            last = a.get('href')
            url = last
            print(last)
            count = count + 1

print(count)