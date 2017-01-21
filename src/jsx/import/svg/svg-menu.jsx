/**
 * svg-menu.jsx: append menu toggle icon.
 *
 * @SvgMenu, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';

var SvgMenu = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            color: '#333',
            activate_menu: false,
        };
    },
  // callback for mouseOver
    mouseOverIcon: function(event) {
        this.setState({color: '#2d2d2d'});
    },
  // callback for mouseOut
    mouseOutIcon: function(event) {
        this.setState({color: '#333'});
    },
  // callback for clickMenu
  //
  //   @activate_menu, is accessible to parent component
  //
    clickMenu: function(event) {
        var bool_toggle = !this.state.activate_menu;
        this.setState({activate_menu: bool_toggle});
        this.props.onChange({activate_menu: true});
    },
  // triggered when 'state properties' change
    render: function() {
        return(
            <svg version='1.0' xmlns='http://www.w3.org/2000/svg' width='18px'
                height='24px' viewBox='0 0 12 16'
                preserveAspectRatio='xMidYMid meet' aria-hidden='true'
                onMouseOver={this.mouseOverIcon}
                onMouseOut={this.mouseOutIcon}
                onClick={this.clickMenu}
            >

                <path style={{fill:this.state.color}} d={`M11.41 9H.59C0
                    9 0 8.59 0 8c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0
                    1-.59 1h.01zm0-4H.59C0 5 0 4.59 0 4c0-.59 0-1
                    .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zM.59
                    11H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1H.59C0 13 0 12.59
                    0 12c0-.59 0-1 .59-1z`}
                />

            </svg>
        )
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default SvgMenu
