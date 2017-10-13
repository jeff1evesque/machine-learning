from flask import current_app
from brain.cache.hset import Hset
from brain.cache.model import Model

def predict(model, collection, predictors):
    rs = ['adaboostknnr', 'adaboostrfr', 'adaboostsvr', 'adaboostr']
    cs = ['adaboostknnc', 'adaboostrfc', 'adaboostsvc', 'adaboostc']

    clf = Model().uncache(
        model + '_model',
        collection_adjusted
    )

    prediction = (clf.predict([predictors]))

    if model in cs:
        encoded_labels = Model().uncache(
            model + '_labels',
            collection_adjusted
        )

        textual_label = encoded_labels.inverse_transform([prediction])
        probability = clf.predict_proba(predictors)
        decision_function = clf.decision_function(predictors)
        classes = [encoded_labels.inverse_transform(x) for x in clf.classes_]

        return {
            'result': textual_label[0][0],
            'model': model,
            'confidence': {
                'classes': list(classes),
                'probability': list(probability[0]),
                'decision_function': list(decision_function[0])
            },
            'error': None
        }
    elif model in rs:
        r2 = Hset().uncache(
            model + '_r2',
            collection_adjusted
        )['result']

        return {
            'result': str(prediction[0]),
            'model': model,
            'confidence': {
                'score': r2
            },
            'error': None
        }
