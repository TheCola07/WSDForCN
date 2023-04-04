import sys
import re
import json

filePath = r"\\WSDForCN\data\baike_qa_train.json"

filewrite = r"\\WSDForCN\data\baike_qa_train.txt"

"""
name = ['AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AM']
iindex = [ 99,   99,   99,   99,   99,   99,   99,   99,   99,   99,   99,   99,   73]
str = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09']
lenght = 13

write = []
jindex = ''
for i in range(lenght):
    for j in range(iindex[i]):
        if j >= 10:
            jindex = j.__str__()
        else:
            jindex = str[j]
        filePath = "G:\Game\wiki_zh_2019\wiki_zh\\" + name[i] + "\wiki_" + jindex
        with open(filePath, 'r', encoding='utf-8') as f:
            for line in f:
                linejson = json.loads(line)
                newlinetext = linejson["text"]
                if newlinetext != '\n':
                    write.append(newlinetext)
            
with open(filewrite, mode='w', encoding="utf-8") as w:
    for i in write:
        w.write(i)

with open(filewrite, 'r', encoding='utf-8') as f:
    count = 0
    for line in f:
        count += 1
        print(line)
        if count == 5:
            break
"""

write = []
with open(filePath, 'r', encoding='utf-8') as f:
    count = 0
    for line in f:
        newtitle = str(json.loads(line)["title"]) + '\n'
        s = ''
        newline = str(json.loads(line)["answer"]).split('\r\n')
        for i in newline:
            s += i
        s += '\n'
        write.append(newtitle)
        write.append(s)
        count += 1
        if count % 100 == 0:
            print(count)

with open(filewrite, 'w', encoding='utf-8') as w:
    for i in write:
        w.write(i)
