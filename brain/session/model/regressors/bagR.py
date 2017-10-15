from brain.session.model.baggen import baggen

def bagRgenerate(
    model,
    collection,
    payload,
    list_error,
    feat=1.0,
    samp=1.0
):
    '''

    Generate an ensemble bagger.

    @model, indicates the type of bagging implementation:

        - bagc, classifier bagger
        - bagr, regressor bagger

    '''

    return baggen(
        model,
        collection,
        payload,
        list_error,
        feat,
        samp,
        None
    )
