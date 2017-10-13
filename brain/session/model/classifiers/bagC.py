import sys
sys.path.insert(0, 'brain/session/model')
from baggen import baggen

def bagCgenerate(model,
                collection,
                payload,
                list_error,
                feat=1.0,
                samp=1.0,
                btrees=10):
    return baggen(model,
                  False,
                  collection,
                  payload,
                  list_error,
                  feat=feat,
                  samp=samp,
                  be=None,
                  k=btrees)
