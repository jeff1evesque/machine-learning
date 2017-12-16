/**
 * svg-user.jsx: append user icon.
 *
 * @SvgUserIcon, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React, { Component } from 'react';

class SvgUserIcon extends Component {
    // initial 'state properties'
    constructor() {
        super();
        this.state = {
            roof_color: '#808080',
            house_color: '#404040',
        }
        this.mouseOverHome = this.mouseOverHome.bind(this);
        this.mouseOutHome = this.mouseOutHome.bind(this);
    }
    // callback for mouseOver svg
    mouseOverHome(event) {
        this.setState({ body_color: '#5ca941' });
    }
    // callback for mouseOut svg
    mouseOutHome(event) {
        this.setState({ body_color: '#808080' });
    }
    // triggered when 'state properties' change
    render() {
        return(
            <svg version='1.1' xmlns='http://www.w3.org/2000/svg' width='45px'
                height='45px' x='0px' y='0px' viewBox='0 0 45 45'
                enable-background='new 0 0 45 45' xml:space='preserve'
                onMouseOver={this.mouseOverHome}
                onMouseOut={this.mouseOutHome}
            >
                <g>
	                <circle cx='256.001' cy='227.844' r='74.844'/>
	                <path style={{fill:this.state.body_color}} d={`M391.343,
                        433.041c0 -61.853 -25.654 -116.077 -64.162 -146.426c
                        -16.932, 20.482 -42.531, 33.537 -71.18, 33.537c -28.649,
                        0 -54.25 -13.055 -71.181 -33.537c -38.508, 30.349 -64.163,
                        84.573 -64.163, 146.426c 0, 0, 55.51, 19.959, 134.096,
                        19.959 S391.343, 433.041, 391.343, 433.041z`}
                    />
                </g>
            </svg>
        );
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default SvgUserIcon;
