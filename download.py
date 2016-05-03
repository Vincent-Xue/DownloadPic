# -*- coding:utf-8 -*-
import os
import urllib.request
def rename(name):
    if len(name) == 2:
        name = '00' + name + '.jpg'
    elif len(name) == 1:
        name = '000' + name + '.jpg'
    else:
        name = name + '.jpg'
    return name
   
os.chdir("D:\\download")
os.getcwd()
count = 1
name=str(count)
name = rename(name)
print(name)
url = 'http://pic1.183read.com/data/magazine/78/34278/21/549021//b_thumb/' + name
while count < 92:
    a = urllib.request.urlopen(url)
    f = open(name, "wb")
    f.write(a.read())
    f.close()
    print(url + ' Saved!')   
    count = count + 1
    name=str(count)
    name = rename(name)
    print(name)
    url = 'http://pic1.183read.com/data/magazine/78/34278/21/549021//b_thumb/' + name
    try:
        a = urllib.request.urlopen(url)
        pass
    except (Exception) as e:
        print(e) 
    else:
        pass
else:
    print(url + ' not found')
    print(a.status)
