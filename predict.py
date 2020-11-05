import sys
import pickle
from test1 import clean3
from test1 import clean4
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn import metrics
def aione():
    predd = []
    filename = 'models/modelV43.sav'
    model = pickle.load(open(filename, 'rb'))
    pred = clean3(input())
    predd.append(pred)
    a = model.predict_proba(predd)
    print(model.predict(predd)[0])
    print(np.max(a))
def aiacc():
    zz = []
    f1 = open('datasets/test.txt', 'r')
    acc = 0
    filename = 'models/modelV43.sav'
    how = 0
    model = pickle.load(open(filename, 'rb'))
    proba = []
    truee = []
    for line in f1:
        how+=1
        ret = line.split("#")[1]
        line = line.split("#")[0]
        zz.append(clean3(line))
        predicted = model.predict(zz)
        proba.append(np.max(model.predict_proba(zz)))
        truee.append(ret)
        zz = []
        if predicted == ret:
            acc += 1
    #print(metrics.roc_auc_score(y_true= truee, y_score = proba, multi_class= 'ovo'))
    print(acc / how)
    f1.close()
if __name__ == '__main__':
    #sys.exit(aione())
    sys.exit(aiacc())