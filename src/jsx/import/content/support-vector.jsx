/**
 * support-vector.jsx: initial form.
 *
 * @SupportVector, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import { Link } from 'react-router-dom';
import ModelGenerateState from '../redux/container/model-generate.jsx';
import ModelPredictState from '../redux/container/model-predict.jsx';
import DataNewState from '../redux/container/data-new.jsx';
import DataAppendState from '../redux/container/data-append.jsx';
import Submit from '../general/submit-button.jsx';
import CurrentResultLink from '../navigation/menu-items/current-result.jsx';
import Spinner from '../general/spinner.jsx';
import setCurrentResult from '../redux/action/current-result.jsx';
import { setSvButton, setGotoResultsButton, setLayout } from '../redux/action/page.jsx';
import checkValidString from '../validator/valid-string.js';
import checkValidFloat from '../validator/valid-float.js';

var SupportVector = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            display_spinner: false,
            ajax_done_result: null,
            ajax_done_error: null,
            ajax_fail_error: null,
            ajax_fail_status: null
        };
    },
  // define properties before mount
    componentWillMount: function() {
        this.setState({
            session_type: this.props.sessionType,
            session_type_value: this.props.sessionTypeValue
        });

      // update redux store: define overall page layout
        const action = setLayout({'layout': 'analysis'});
        this.props.dispatchLayout(action);
    },
  // define properties after update
    componentDidUpdate: function() {
      // update state using react-route properties
        if (
            !!this.props.sessionType &&
            this.props.sessionType != this.state.session_type
        ) {
            this.setState({session_type: this.props.sessionType});
        }

        if (
            !!this.props.sessionTypeValue &&
            this.props.sessionTypeValue != this.state.session_type_value
        ) {
            this.setState({
               session_type_value: this.props.sessionTypeValue
            });
        }
    },
  // update redux store
    storeResults: function() {
        var serverObj = !!this.state.ajax_done_result ? this.state.ajax_done_result : false;
        var resultSet = !!serverObj.result ? serverObj.result : false;
        var confidence = !!resultSet.confidence ? resultSet.confidence : false;

        if (
            resultSet &&
            !!resultSet.result &&
            resultSet.model == 'svm' &&
            confidence &&
            confidence.classes &&
            confidence.classes.length > 0 &&
            confidence.classes.every(checkValidString) &&
            confidence.probability &&
            confidence.probability.length > 0 &&
            confidence.probability.every(checkValidFloat) &&
            confidence.decision_function &&
            confidence.decision_function.length > 0 &&
            confidence.decision_function.every(checkValidFloat)
        ) {
          // update redux store
            const payload = {
                type: resultSet.model,
                data: JSON.stringify({
                    result: resultSet.result,
                    classes: confidence.classes,
                    probability: confidence.probability,
                    decision_function: confidence.decision_function
                })
            }
            this.props.dispatchCurrentResult(setCurrentResult(payload));

          // update redux store
            const gotoResultsButton = setGotoResultsButton({button: {goto_results: true}});
            this.props.dispatchGotoResultsButton(gotoResultsButton);
        }
        else if (
            resultSet &&
            !!resultSet.result &&
            resultSet.model == 'svr' &&
            confidence &&
            confidence.score &&
            checkValidFloat(confidence.score)
        ) {
          // update redux store
            const payload = {
                type: resultSet.model,
                data: JSON.stringify({
                    result: resultSet.result,
                    r2: confidence.score
                })
            }
            this.props.dispatchCurrentResult(setCurrentResult(payload));

          // update redux store
            const gotoResultsButton = setGotoResultsButton({button: {goto_results: true}});
            this.props.dispatchGotoResultsButton(gotoResultsButton);
        }
        else {
          // update redux store
            const gotoResultsButton = setGotoResultsButton({button: {goto_results: false}});
            this.props.dispatchGotoResultsButton(gotoResultsButton);
        }
    },
  // triggered when 'state properties' change
    render: function() {
      // spinner
        var spinner = this.state.display_spinner ? <Spinner /> : null;
        var session = this.state.session_type ? this.state.session_type : null;

      // submit button
        if (
            this.props &&
            this.props.page &&
            this.props.page.button
        ) {
            const button = this.props.page.button;
            var submitBtn = !!button.submit_analysis ? <Submit cssClass='btn mn-2' /> : null;

            if (
                this.state.ajax_done_result &&
                !!this.state.ajax_done_result.type &&
                this.state.ajax_done_result.type == 'model-predict'
            ) {
                var resultBtn = !!button.goto_results ? <CurrentResultLink /> : null;
            }
        }

        return(
            <div>
                {session}
                {submitBtn}
                {resultBtn}
                {spinner}
            </div>
        );
    },
});

// indicate which class can be exported, and instantiated via 'require'
export default SupportVector
