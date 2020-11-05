import sys
import pickle
from test1 import clean3
from test1 import clean4
from sklearn.metrics import accuracy_score
def aione():
    predd = []
    filename = 'model.sav'
    model = pickle.load(open(filename, 'rb'))
    pred = clean3(input())
    predd.append(pred)
    print(model.predict(predd)[0])
def aiacc():
    zz = []
    f1 = open('test.txt', 'r')
    acc = 0
    filename = 'model3.sav'
    how = 0
    model = pickle.load(open(filename, 'rb'))
    for line in f1:
        how+=1
        ret = line.split("#")[1]
        line = line.split("#")[0]
        zz.append(clean3(line))
        predicted = model.predict(zz)
        zz = []
        if predicted == ret:
            acc += 1
    print(acc / how)
    f1.close()
if __name__ == '__main__':
    #sys.exit(aione())
    sys.exit(aiacc())