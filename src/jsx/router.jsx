/**
 * router.jsx: defines react-router tree.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import { Router, Route, browserHistory } from 'react-router'
import DataNew from './import/session-type/data_new.jsx';
import DataAppend from './import/session-type/data_append.jsx';
import ModelGenerate from './import/session-type/model_generate.jsx';
import ModelPredict from './import/session-type/model_predict.jsx';
import SupportVector from './import/content/support_vector.jsx';

// constant: analysis layout
const AnalysisLayout = (props) => (
    <div className='analysis-container'>
        <SupportVector routerProp={props.children} />
    </div>
);

// application router
var AppRouter = React.createClass({
  // display result
    render: function() {
        {/* return:
            @this.props.indexRoute, defined from parent component.
            @this.props.renderSubpage, defined from parent component.
            @history, is required per 'react-router's ability to handle url:

                - [GitHub-URL]/issues/2727#issuecomment-258030214
        */}

        return(
            <Router history={browserHistory}>
                <Route component={this.props.indexRoute} >
                    <Route path='/' component={AnalysisLayout}>
                        <Route
                            path='/session/data-new'
                            component={DataNew}
                        />
                        <Route
                            path='/session/data-append'
                            component={DataAppend}
                        />
                        <Route
                            path='/session/model-generate'
                            component={ModelGenerate}
                        />
                        <Route
                            path='/session/model-predict'
                            component={ModelPredict}
                        />
                    </Route>
                </Route>
            </Router>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default AppRouter
