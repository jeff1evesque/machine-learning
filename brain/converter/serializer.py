import json
import numpy
from sklearn import base
from sklearn import tree


def serialize(model):
    try:
        modelv = vars(model)  # get values to serialize
    except:
        # required for tree._tree.Tree, which has no __dict__ variable
        modelv = altvars(model)

    # v.tolist() converts numpy arrays to lists
    # serialize(v) recursively converts estimators into json objects
    # [u.tolist() ... ] converts lists of numpy arrays estimators into lists of
    #    json objects

    corrected_modelv = {k:
                        v.tolist()
                        if type(v) == numpy.ndarray
                        else serialize(v)
                        if issubclass(type(v), base.BaseEstimator) or
                        type(v) == tree._tree.Tree
                        else [u.tolist()
                              if type(u) == numpy.ndarray
                              else serialize(u)
                              if issubclass(type(u), base.BaseEstimator)
                              else u
                              for u in v]
                        if type(v) == list
                        else v
                        for k, v in modelv.items()}

    # convert the above dict to json
    return json.dumps(corrected_modelv)


def altvars(obj):
    '''
        provides an alternate to the vars method which doesn't work if
        the __dict__ variable does not exist
    '''
    return dict([attr, getattr(obj, attr)]
                for attr in dir(obj) if not attr.startswith('_') and not
                callable(getattr(obj, attr)))


def deserialize(json_model):
    corrected_modelv = json.loads(json_model)

    # numpy.asarray(v) converts lists to numpy arrays
    # deserialize(v) recursively deserializes estimators
    modelv = {k: numpy.asarray(v)
              if type(v) == list
              else deserialize(v) if k == "base_estimator" and is_estimator(v)
              else v
              for k, v in corrected_modelv.items()}

    return SimpleNamespace(**modelv)


def is_estimator(j):
    '''
        checks whether an object is valid json
    '''
    try:
        json.loads(j)
    except ValueError:
        return False
    return True


# borrowed from python 3.3 documentation
class SimpleNamespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        keys = sorted(self.__dict__)
        items = ("{}={!r}".format(k, self.__dict__[k]) for k in keys)
        return "{}({})".format(type(self).__name__, ", ".join(items))

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
