#!/usr/bin/python

'''@save_observation_label'''

from brain.database.save_observation import Save_Observation


def observation_label(self, session_type, session_id, labels):
    '''observation_label

    This method saves the list of unique independent variable labels, which can
    be expected in any given observation, into the sql database. This list of
    labels, is predicated on a supplied session id (entity id).

    '''

    # variables
    list_error = []

    # save labels
    if len(labels) > 0:
        for label_list in labels:
            for label in label_list:
                db_save = Save_Observation(
                    {
                        'label': label,
                        'id_entity': session_id
                    },
                    session_type
                )

                # save dataset element, append error(s)
                db_return = db_save.save_label()
                if not db_return['status']:
                    list_error.append(db_return['error'])

    # return
    return {'error': list_error}
