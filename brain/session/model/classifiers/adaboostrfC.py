import sys
sys.path.insert(0, 'brain/session/model')
from adabooster import adaboostgen
from sklearn import RandomForestClassifier

def adaboostrfCgenerate(
    model,
    collection,
    payload,
    list_error,
    learning=1.0,
    estimators=50,
    trees=10,
    criterion='gini',
    max_features='auto',
    max_depth=None,
    min_samples_split=2,
    min_samples_leaf=1,
    min_weight_fraction_leaf=0.,
    max_leaf_nodes=None,
    min_impurity_decrease=0.,
    bootstrap=True,
    oob_score=False,
    n_jobs=1,
    random_state=None):
    return adaboostgen(
        model,
        False,
        collection,
        payload,
        list_error,
        learning = learning,
        bnum = estimators,
        be = RandomForestClassifier(
          n_estimators=trees,
          criterion=criterion,
          max_features=max_features,
          max_depth=max_depth,
          min_samples_split=min_samples_split,
          min_samples_leaf=min_samples_leaf,
          min_weight_fraction_leaf=min_weight_fraction_leaf,
          max_leaf_nodes=max_leaf_nodes,
          min_impurity_decrease=min_impurity_decrease,
          bootstrap=bootstrap,
          oob_score=oob_score,
          n_jobs=n_jobs,
          random_state=random_state))
