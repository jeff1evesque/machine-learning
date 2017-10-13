import sys
sys.path.insert(0, 'brain/session/model')
from baggen import baggen

def bagRgenerate(model,
                collection,
                payload,
                list_error,
                feat=1.0,
                samp=1.0):
    return baggen(model,
                  True,
                  collection,
                  payload,
                  list_error,
                  feat,
                  samp,
                  None)
