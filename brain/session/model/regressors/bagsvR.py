import sys
sys.path.insert(0, 'brain/session/model')
from baggen import baggen
from sklearn.svm import SVR


def bagsvRgenerate(model,
                collection,
                payload,
                list_error,
                feat=1.0,
                samp=1.0,
                btrees=10,
                kernel,
                random_state=None):
    return baggen(model,
                  True,
                  collection,
                  payload,
                  list_error,
                  feat=feat,
                  samp=samp,
                  k=btrees,
                  be=SVR(kernel=kernel),
                  random_state=random_state)
