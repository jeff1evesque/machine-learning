from brain.converter.serializer import serialize, deserialize
from sklearn import ensemble
from sklearn import svm
import numpy

def test_serialize_svc():
    X = [[0, 0], [1, 1]]
    Y = [0, 1]

    clf = svm.SVC()
    clf.fit(X, Y)

    packed_clf = serialize(clf)
    assert type(packed_clf) == str

    unpacked_clf = deserialize(packed_clf)
    assert len(unpacked_clf.predict(numpy.array([[0, 2]]))) == 1


def test_serialize_bagrf():
    X = [[0, 0], [1, 1]]
    Y = [0, 1]
    
    clf = ensemble.BaggingClassifier(
            base_estimator=ensemble.RandomForestClassifier(n_estimators=8),
            n_estimators=12)
    clf.fit(X, Y)
    packed_clf = serialize(clf)
    assert type(packed_clf) == str

    unpacked_clf = deserialize(packed_clf)

    assert len(unpacked_clf.predict(numpy.array([[0, 2]]))) == 1


def test_serialize_bagsvc():
    X = [[0, 0], [1, 1]]
    Y = [0, 1]
    
    clf = ensemble.BaggingClassifier(
            base_estimator=svm.SVC(kernel='linear'),
            n_estimators=12)
    # this has some bugged output, but it's a bug in sklearn I think
    clf.fit(X, Y)
    packed_clf = serialize(clf)
    assert type(packed_clf) == str

    unpacked_clf = deserialize(packed_clf)

    assert len(unpacked_clf.predict(numpy.array([[0, 2]]))) == 1


def test_serialize_bagsvr():
    clf = ensemble.BaggingRegressor(
            base_estimator=svm.SVR(kernel='linear'),
            n_estimators=12)

    clf.fit([[0.2, 0.3], [0.1, -1]], [0.2, 0.5])
    packed_clf = serialize(clf)
    assert type(packed_clf) == str

    unpacked_clf = deserialize(packed_clf)

    assert len(unpacked_clf.predict(numpy.array([[0, 1.2]]))) == 1


def test_serialize_boostsvr():
    clf = ensemble.AdaBoostRegressor(
            base_estimator=svm.SVR(kernel='linear'),
            n_estimators=45)

    clf.fit([[0.2, 0.3], [0.1, -1]], [0.2, 0.5])
    packed_clf = serialize(clf)
    assert type(packed_clf) == str

    unpacked_clf = deserialize(packed_clf)

    assert len(unpacked_clf.predict(numpy.array([[0, 1.2]]))) == 1
