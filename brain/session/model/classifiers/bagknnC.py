import sys
sys.path.insert(0, 'brain/session/model')
from baggen import baggen
from sklearn import KNeighborsClassifier

def bagknnCgenerate(model,
                 collection,
                 payload,
                 list_error,
                 feat=1.0,
                 samp=1.0,
                 btrees=10,
                 k=5,
                 weights='uniform',
                 algorithm='auto',
                 leaf_size=30,
                 p=2):
    return baggen(model,
                  False,
                  collection,
                  payload,
                  list_error,
                  feat=feat,
                  samp=samp,
                  be=KNeighborsClassifier(n_neighbors=k,
                                       weights=weights,
                                       algorithm=algorithm,
                                       leaf_size=leaf_size,
                                       p=p),
                  k=btrees)
