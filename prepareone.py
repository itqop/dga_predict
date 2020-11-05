import random
"""
f = open('inall.txt', 'r')
f1 = open('testaa3.txt', 'w')
a = []
t = ""
op =[]
for line in f:
    op = line.split("#")
    text = line[0:line.index(".")]
    if(len(text)>3):
        for i in range(len(text)-2):
            t+= text[i:i+3] + " "
    else:
        t = text +" "
    a.append(t+ "#"+op[1])
    t = ""
random.shuffle(a)
for line in a:
    f1.write(line)
f.close()
f1.close()"""

f = open('datasets/all_dga.txt', 'r')
f1 = open('datasets/all_legit.txt', 'r')
f3 = open('datasets/inall.txt', 'r')
f2 = open('datasets/testQ.txt','w')
a = []
for line in f:
    a.append(line)
for line in f1:
    a.append(line)
for line in f3:
    line = line.replace(" #", "")
    a.append(line)
random.shuffle(a)
op =[]
for line in a:
    t = ""
    if len(line) <2:
        continue
    op = line.split(" ")
    text = line[0:line.index(".")]
    if (len(text) > 3):
        for i in range(len(text) - 2):
            t += text[i:i + 3] + " "
    else:
        t = text + " "
    if (int(op[1]) >=1):
        q = 1
    else: q = 0
    f2.write(t+ "# "+str(q)+"\n")
f.close()
f1.close()
f2.close()