/**
 * analysis.jsx: general analysis layout.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 */

import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import { Route } from 'react-router-dom';
import NavBar from '../navigation/nav-bar.jsx';
import DataNewState from '../redux/container/data-new.jsx';
import DataAppendState from '../redux/container/data-append.jsx';
import ModelGenerateState from '../redux/container/model-generate.jsx';
import ModelPredictState from '../redux/container/model-predict.jsx';
import CurrentResultState from '../redux/container/current-result.jsx';
import ResultsDisplayState from '../redux/container/results.jsx';
import CurrentResultLink from '../navigation/menu-items/current-result.jsx';
import ajaxCaller from '../general/ajax-caller.js';
import Submit from '../general/submit-button.jsx';
import checkValidString from '../validator/valid-string.js';
import checkValidFloat from '../validator/valid-float.js';
import setCurrentResult from '../redux/action/current-result.jsx';
import {
    setSvButton,
    setGotoResultsButton,
    setLayout,
    setSpinner
} from '../redux/action/page.jsx';
import { BreakpointRender } from 'rearm/lib/Breakpoint';
import breakpoints from '../general/breakpoints.js';

class AnalysisLayout extends Component {
    // initial 'state properties'
    constructor() {
        super();
        this.state =  {
            ajax_done_result: null,
            ajax_done_error: null,
            ajax_fail_error: null,
            ajax_fail_status: null,
        };
        this.handleSubmit = this.handleSubmit.bind(this);
        this.storeResults = this.storeResults.bind(this);
    }
    // define properties after update
    componentDidUpdate() {
        // update state using react-route properties
        if (
            !!this.props.sessionType &&
            this.props.sessionType != this.state.session_type
        ) {
            this.setState({ session_type: this.props.sessionType });
        }

        if (
            !!this.props.sessionTypeValue &&
            this.props.sessionTypeValue != this.state.session_type_value
        ) {
            this.setState({
                session_type_value: this.props.sessionTypeValue,
            });
        }
    }
    // define properties before mount
    componentWillMount() {
        this.setState({
            session_type: this.props.sessionType,
            session_type_value: this.props.sessionTypeValue,
        });

        // update redux store: define overall page layout
        const action = setLayout({ layout: 'analysis' });
        this.props.dispatchLayout(action);
    }
    // send form data to serverside on form submission
    handleSubmit(event) {
        // prevent page reload
        event.preventDefault();

        // local variables
        const sessionType = this.props.page.content_type;
        if (
            sessionType == 'data_new' ||
            sessionType == 'data_append' ||
            sessionType == 'model_generate' ||
            sessionType == 'model_predict'
        ) {
            const ajaxEndpoint = '/load-data';
            const formData = new FormData(this.refs.analysisForm);
            formData.append('session_type', sessionType);

          // model_generate: append penalty, gamma
            if (
                this.props &&
                this.props.page &&
                this.props.page.slider
            ) {

                if (!!this.props.page.slider.penalty) {
                    formData.append('penalty', this.props.page.slider.penalty);
                }

                if (!!this.props.page.slider.gamma) {
                    formData.append('gamma', this.props.page.slider.gamma);
                }
            }

            const ajaxArguments = {
                endpoint: ajaxEndpoint,
                data: formData,
            };

            // boolean to show ajax spinner
            var action = setSpinner({'spinner': true});
            this.props.dispatchSpinner(action);

            // asynchronous callback: ajax 'done' promise
            ajaxCaller(
                (asynchObject) => {
                    // Append to DOM
                    if (asynchObject && asynchObject.error) {
                        this.setState({ ajax_done_error: asynchObject.error });
                    } else if (asynchObject) {
                        this.setState({ ajax_done_result: asynchObject });
                        this.storeResults();
                    } else {
                        this.setState({ ajax_done_result: null });
                    }
                    // boolean to hide ajax spinner
                    var action = setSpinner({'spinner': false});
                    this.props.dispatchSpinner(action);
                },
                // asynchronous callback: ajax 'fail' promise
                (asynchStatus, asynchError) => {
                    if (asynchStatus) {
                        this.setState({ ajax_fail_status: asynchStatus });
                        console.log(`Error Status: ${asynchStatus}`);
                    }
                    if (asynchError) {
                        this.setState({ ajax_fail_error: asynchError });
                        console.log(`Error Thrown: ${asynchError}`);
                    }
                    // boolean to hide ajax spinner
                    var action = setSpinner({'spinner': false});
                    this.props.dispatchSpinner(action);
                },
                // pass ajax arguments
                ajaxArguments,
            );
        }
    }
    // update redux store
    storeResults() {
        const serverObj = this.state.ajax_done_result ? this.state.ajax_done_result : false;
        const resultSet = serverObj.result ? serverObj.result : false;
        const confidence = resultSet.confidence ? resultSet.confidence : false;

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
                    decision_function: confidence.decision_function,
                }),
            };
            this.props.dispatchCurrentResult(setCurrentResult(payload));

            // update redux store
            const gotoResultsButton = setGotoResultsButton({ button: { goto_results: true } });
            this.props.dispatchGotoResultsButton(gotoResultsButton);
        } else if (
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
                    r2: confidence.score,
                }),
            };
            this.props.dispatchCurrentResult(setCurrentResult(payload));

            // update redux store
            const gotoResultsButton = setGotoResultsButton({ button: { goto_results: true } });
            this.props.dispatchGotoResultsButton(gotoResultsButton);
        } else {
            // update redux store
            const gotoResultsButton = setGotoResultsButton({ button: { goto_results: false } });
            this.props.dispatchGotoResultsButton(gotoResultsButton);
        }
    }
    showAnalysisContent() {
        if (
            this.props &&
            this.props.page &&
            this.props.page.button
        ) {
            const button = this.props.page.button;
            var submitBtn = button.submit_analysis ? <Submit cssClass='btn mn-2 btn-primary' /> : null;

            if (
                this.state.ajax_done_result &&
                !!this.state.ajax_done_result.type &&
                this.state.ajax_done_result.type == 'model-predict'
            ) {
                var resultBtn = button.goto_results ? <CurrentResultLink /> : null;
            }
        }

        return (
            {/*
                @analysisForm, referenced within 'handleSubmit' callback
            */}
            <div>
                <form
                    onSubmit={this.handleSubmit}
                    ref='analysisForm'
                    className='analysis-container'
                >
                    <Route
                        exact
                        path='/session/data-new'
                        component={DataNewState}
                    />
                    <Route
                        exact
                        path='/session/data-append'
                        component={DataAppendState}
                    />
                    <Route
                        exact
                        path='/session/model-generate'
                        component={ModelGenerateState}
                    />
                    <Route
                        exact
                        path='/session/model-predict'
                        component={ModelPredictState}
                    />
                    {submitBtn}
                    {resultBtn}
                </form>
                <div>
                    <Route
                        exact
                        path='/session/current-result'
                        component={CurrentResultState}
                    />
                    <Route
                        exact
                        path='/session/results'
                        component={ResultsDisplayState}
                    />
                </div>
            </div>
        );
    }
    render() {
        return (
            <div className='row'>
                <BreakpointRender breakpoints={breakpoints} type='viewport'>
                    {bp => (
                        if (isGte('large')) {
                            <div>
                                <div className='col-sm-3'>
                                    <NavBar />
                                </div>
                                <div className='col-sm-9'>
                                    {this.showAnalysisContent()}
                                </div>
                            </div>
                        } else {
                            <div>
                                <div className='col-sm-12'>
                                    {this.showAnalysisContent()}
                                </div>
                            </div>
                        }
                    }
                </BreakpointRender>
            </div>
        );
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default AnalysisLayout;
