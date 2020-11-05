f = open("datasets/dga_train_examples.txt")
f2 = open("datasets/dga_mg.txt","w")
for line in f:
    line = line.replace("\t"," # ")
    f2.write(line)
f.close()
f2.close()