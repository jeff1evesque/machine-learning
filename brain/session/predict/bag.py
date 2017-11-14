from flask import current_app
from brain.cache.hset import Hset
from brain.cache.model import Model


def predict(model, collection, predictors):
    probability = None
    decision_function = None
    collection_adjusted = collection.lower().replace(' ', '_')
    list_model_type = current_app.config.get('MODEL_TYPE')
    rs = [
        list_model_type[3],
        list_model_type[5],
        list_model_type[7],
        list_model_type[9]
    ]
    cs = [
        list_model_type[2],
        list_model_type[4],
        list_model_type[6],
        list_model_type[8]
    ]

    clf = Model().uncache(
        model + '_model',
        collection_adjusted
    )

    prediction = clf.predict([predictors])

    if model in cs:
        encoded_labels = Model().uncache(
            model + '_labels',
            collection_adjusted
        )

        textual_label = encoded_labels.inverse_transform(prediction)
        probability = clf.predict_proba([predictors])
        try:
            decision_function = clf.decision_function([predictors])
            dec_ret = list(decision_function[0])
        except:
            decision_function = None
            dec_ret = None
        classes = [encoded_labels.inverse_transform(x) for x in clf.classes_]

        return {
            'result': textual_label[0],
            'model': model,
            'confidence': {
                'classes': list(classes),
                'probability': list(probability[0]),
                'decision_function': dec_ret
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
