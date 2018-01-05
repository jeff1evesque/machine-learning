/**
 * home-page.jsx: main homepage for entire application.
 *
 * @HomePage, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React, { Component } from 'react';
import { NavLink } from 'react-router-dom';
import { setLayout } from '../redux/action/page.jsx';
import AnimateCollisions from '../animation/animate.jsx';

class HomePage extends Component {
    componentWillMount() {
        const action = setLayout({ layout: 'analysis' });
        this.props.dispatchLayout(action);
    }
    render() {
        return (
            <div className='main-full-span home'>
                <h1>{'Welcome!'}</h1>
                <AnimateCollisions />
                <NavLink
                    activeClassName='active'
                    className='btn mn-2'
                    to='session'
                >
                    {'Begin Analysis'}
                </NavLink>
            </div>
        );
    }
}

HomePage.propTypes = {
    dispatchLayout: PropTypes.func,
}

// indicate which class can be exported, and instantiated via 'require'
export default HomePage;
