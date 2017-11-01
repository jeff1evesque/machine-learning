from brain.session.model.adabooster import adaboostgen
from sklearn import KNeighborsClassifier


def adaboostknnCgenerate(
    model,
    collection,
    payload,
    list_error,
    learning=1.0,
    estimators=50,
    k=5,
    weights='uniform',
    algorithm='auto',
    leaf_size=30,
    p=2
):
    return adaboostgen(
        model,
        collection,
        payload,
        list_error,
        learning=learning,
        be=KNeighborsClassifier(
            n_neighbors=k,
            weights=weights,
            algorithm=algorithm,
            leaf_size=leaf_size,
            p=p
        ),
        bnum=estimators
    )
