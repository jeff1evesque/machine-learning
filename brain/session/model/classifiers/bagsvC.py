import sys
sys.path.insert(0, 'brain/session/model')
from baggen import baggen
from sklearn.svm import SVC

def bagsvCgenerate(model,
                collection,
                payload,
                list_error,
                feat=1.0,
                samp=1.0,
                kernel):
    return baggen(model,
                  False,
                  collection,
                  payload,
                  list_error,
                  feat,
                  samp,
                  SVC(kernel=kernel))
