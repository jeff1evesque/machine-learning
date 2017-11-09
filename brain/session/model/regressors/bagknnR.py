import sys
sys.path.insert(0, 'brain/session/model')
from baggen import baggen
from sklearn.neighbors import KNeighborsRegressor

def bagknnRgenerate(model,
                 collection,
                 payload,
                 list_error,
                 feat=1.0,
                 samp=1.0,
                 k=5,
                 btrees=10,
                 weights='uniform',
                 algorithm='auto',
                 leaf_size=30,
                 p=2,
                 random_state=None):
    return baggen(model,
                  True,
                  collection,
                  payload,
                  list_error,
                  feat=feat,
                  samp=samp,
                  k=btrees,
                  be=KNeighborsRegressor(n_neighbors=k,
                                       weights=weights,
                                       algorithm=algorithm,
                                       leaf_size=leaf_size,
                                       p=p),
                  random_state=random_state)
