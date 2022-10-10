import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter file name: ")
html = urllib.request.urlopen(url, context=ctx).read()
print(html)

stuff = ET.fromstring(html)
lst = stuff.findall('comments/comment')
print('User count:', len(lst))
sum = 0
for item in lst:
    print('Name', item.find('name').text)
    print('Count', item.find('count').text)
    sum = sum + int(item.find('count').text)
print(sum)

