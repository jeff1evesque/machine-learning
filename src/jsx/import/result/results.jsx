/**
 * results.jsx: list all prediction result, with link to corresponding
 *              prediction result item.
 *
 * @CurrentResultDisplay, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React, { Component } from 'react';
import { Table } from 'react-bootstrap';
import { NavLink } from 'react-router-dom';
import { setLayout, setContentType, setSpinner } from '../redux/action/page.jsx';
import ajaxCaller from '../general/ajax-caller.js';

class ResultsDisplay extends Component {
    // initial 'state properties'
    constructor() {
        super();
        this.state = {
            titles: null,
            status: null,
        };
    }
    componentWillMount() {
        // update redux store
        const actionLayout = setLayout({ layout: 'analysis' });
        this.props.dispatchLayout(actionLayout);

        const actionContentType = setContentType({ layout: 'result' });
        this.props.dispatchContentType(actionContentType);
    }
    // call back: get all titles, and nid from server side
    componentDidMount() {
        // ajax arguments
        const ajaxEndpoint = '/retrieve-prediction-titles';
        const ajaxArguments = {
            endpoint: ajaxEndpoint,
            data: null,
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
                    const results = asynchObject;

                    // enumerate and store response
                    this.setState(Object.assign({}, results));
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
    render() {
        // local variables
        const status = this.state.status;
        const titles = this.state.titles;

        // generate result
        if (status == 0 && titles && titles.length > 0) {
            var resultList = (
                <Table className='result-row' responsive>
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>session_id</th>
                            <th>session_title</th>
                            <th>date_created</th>
                        </tr>
                    </thead>
                    <tbody>
                        {
                            titles.map((cells, trIdx) => {
                                if (cells.length == 3) {
                                    return (
                                        <tr key={`tr-${trIdx}`}>
                                            <td key={`td-index-${trIdx}`}>{trIdx}</td>
                                            <td key={`td-sid-${trIdx}`}>{cells[0]}</td>
                                            <td key={`td-title-${trIdx}`}>
                                                <NavLink
                                                    to={`/session/current-result?nid=${cells[0]}`}
                                                    key={`link-title-${trIdx}`}
                                                >
                                                    {cells[1]}
                                                </NavLink>
                                            </td>
                                            <td key={`td-date-${trIdx}`}>{cells[2]}</td>
                                        </tr>
                                    );
                                }
                                else {
                                    return null;
                                }
                            })
                        }
                    </tbody>
                </Table>
            );
        } else {
            var resultList = (
                <div className='result-list'>Sorry, no results available!</div>
            );
        }

        // display result
        return (
            <div className='result-container'>
                <h2>Your Results</h2>
                <div>{resultList}</div>
            </div>
        );
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default ResultsDisplay;
