from brain.session.model.adabooster import adaboostgen
from sklearn.svm import SVC


def adaboostsvCgenerate(
    model,
    collection,
    payload,
    list_error,
    kernel,
    learning=1.0,
    estimators=50
):
    return adaboostgen(
        model,
        collection,
        payload,
        list_error,
        learning=learning,
        bnum=estimators,
        be=SVC(kernel=kernel)
    )
