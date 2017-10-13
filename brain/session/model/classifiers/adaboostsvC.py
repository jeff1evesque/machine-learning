import sys
sys.path.insert(0, 'brain/session/model')
from adaboostgen import adaboostgen
from sklearn.svm import SVC

def adaboostsvCgenerate(model,
                collection,
                payload,
                list_error,
                learning=1.0,
                estimators=50,
                kernel):
    return adaboostgen(model,
                  False,
                  collection,
                  payload,
                  list_error,
                  learning=learning,
                  k=estimators,
                  be=SVC(kernel=kernel))
