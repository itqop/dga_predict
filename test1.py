import sys
import pickle
import re
import numpy as np
from Stemmer import Stemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

def clean3(text):
    text = text.lower()
    t = ""
    if (len(text) > 3):
        text = text[0:text.index(".")]
        for i in range(len(text) - 2):
            t += text[i:i + 3] + " "
        t += "\n"
    return t
def clean4(text):
    text = text.lower()
    t = ""
    if (len(text) > 4):
        text = text[0:text.index(".")]
        for i in range(len(text) - 3):
            t += text[i:i + 4] + " "
        t += "\n"
    return t
def load_data():
    data = {'site':[],'tag':[]}
    for line in open('testaa3.txt'):
        row = line.split("#")
        data['site'] += [row[0]]
        data['tag'] += [row[1]]
    return data
def train_test_split(data, validation_split = 0.1):
    sz = len(data['site'])
    indicates = np.arange(sz)
    np.random.shuffle(indicates)
    X = [data['site'][i] for i in indicates]
    Y = [data['tag'][i] for i in indicates]
    nb_validation_samples = int(validation_split * sz)
    return {
        'train' : {'x': X[:-nb_validation_samples], 'y' : Y[:-nb_validation_samples]},
        'test': {'x': X[:-nb_validation_samples], 'y' : Y[:-nb_validation_samples]}
    }
def hentai():
    data = load_data()

    D = train_test_split(data)

    text_clf = Pipeline([(('tlidf'),TfidfVectorizer()), ('clf', SGDClassifier(loss = 'hinge')),])

    text_clf.fit(D['train']['x'], D['train']['y'])

    predicted = text_clf.predict(D['train']['x'])
    """
    #print(0000000)
    #z = input()
    zz = []
    f1 = open('test.txt', 'r')
    acc = 0
    for line in f1:
        ret = line.split("#")[1]
        line = line.split("#")[0]
        zz.append(text_cleaner(line))
        predicted = text_clf.predict(zz)
        zz = []
        if predicted == ret:
            acc+=1
    print(acc/5819)
    f1.close()
    #z = text_cleaner(z)
    #zz.append(z)
    print(predicted[0])"""
    filename = 'model3.sav'
    pickle.dump(text_clf, open(filename, 'wb'))
if __name__ == '__main__':
    sys.exit(hentai())