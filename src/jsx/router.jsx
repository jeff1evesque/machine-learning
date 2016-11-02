/**
 * router.jsx: defines react-router tree.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import { Router, Route, browserHistory } from 'react-router'
import NavBar from './import/navigation/nav_bar.jsx';
import DataNew from './import/session-type/data_new.jsx';
import DataAppend from './import/session-type/data_append.jsx';
import ModelGenerate from './import/session-type/model_generate.jsx';
import ModelPredict from './import/session-type/model_predict.jsx';

// constant: general layout
const MainLayout = (props) => (
    <div>
        <NavBar />
        {props.children}
    </div>
);

var AppRouter = React.createClass({
  // display result
    render: function() {
        {/* return:
            @this.props.indexRoute, defined from parent component.
            @history, is required per 'react-router's ability to handle url:

                - [GitHub-URL]/issues/2727#issuecomment-258030214
        */}
        return(
            <Router history={browserHistory}>
                <Route path='/' component={this.props.indexRoute} >
                    <Route component={MainLayout}>
                        <Route
                            path='/data-new'
                            component={DataNew}
                        />
                        <Route
                            path='/data-append'
                            component={DataAppend}
                        />
                        <Route
                            path='/model-generate'
                            component={ModelGenerate}
                        />
                        <Route
                            path='/model-predict'
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

