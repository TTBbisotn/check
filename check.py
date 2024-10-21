import re
from time import sleep

inputfile = open('story1data.txt','r',encoding='utf-8')

outputfile = open('export/story1data.txt','w+',encoding='utf-8')


regex = r"(?:\'s profile picture\n(.*)|dateTime (.*)\.)"
# data = re.findall('\'s profile picture\n(.*)',inputfile.read())
# data = re.findall('\d+\-\d+\-\d+ \d+:\d+:\d+',inputfile.read())
data = re.findall(regex,inputfile.read(),re.MULTILINE)

# for i in data:
#     print(data)

for i in data:
    for a in i :
        if a == '':
            pass
        else:
            outputfile.write(a+";\n")
