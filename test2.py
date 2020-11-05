import sys
import pickle
import re
import numpy as np
from sklearn.calibration import CalibratedClassifierCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from sklearn import metrics
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
    for line in open('datasets/testaa3.txt'):
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

    text_clf = Pipeline([(('tlidf'),TfidfVectorizer()), ('clf', SGDClassifier(loss = 'modified_huber')),])
    #text_clf = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', SGDClassifier(loss='log')),])

    text_clf.fit(D['train']['x'], D['train']['y'])
    #calibrator = CalibratedClassifierCV(text_clf, cv='prefit')

    #model = calibrator.fit(D['train']['x'], D['train']['y'])
    predicted = text_clf.predict(D['test']['x'])

    filename = 'models/modelV53.sav'
    pickle.dump(text_clf, open(filename, 'wb'))
    print(metrics.classification_report(digits=6, y_true=D['test']['y'], y_pred =predicted))
    y_prob = text_clf.predict_proba(D['test']['x'])
    #print(metrics.roc_auc_score(D['test']['y'],y_prob,multi_class='ovo'))
if __name__ == '__main__':
    sys.exit(hentai())