/**
 * content.jsx: generate main content.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';

var PageLayout = React.createClass({
  // display result
    render: function() {
      // destructure router object
        const { MainContent, UserMenu, css, layout } = this.props

      // render content
        return(
            <div className='container-inner'>
                <div className='menu-container'>
                    <UserMenu layout={layout}/>
                </div>
                <div className='main'>
                    <SideBar />
                    <div className={css}>
                        <MainContent />
                    </div>
                </div>
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default PageLayout
