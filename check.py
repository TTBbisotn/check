import re
from time import sleep
from duplicate_file_remover import remove_duplicate_lines

inputfile = open('story2data.txt','r',encoding='utf-8')


outputfile = open('export/story2data.txt','w+',encoding='utf-8')

regex = r"(?:\'s profile picture\n(.*)|(\d+\-\d+\-\d+ \d+:\d+:\d+))"
# data = re.findall('\'s profile picture\n(.*)',inputfile.read())
# data = re.findall('\d+\-\d+\-\d+ \d+:\d+:\d+',inputfile.read())
data = re.findall(regex,inputfile.read(),re.MULTILINE)

# for i in data:
#     outputfile.write(i+';\n')
for i in data:
    for a in i :
        if a == '':
            pass
        else:
            outputfile.write(a+';\n')
