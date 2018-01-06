/**
 * svg-user.jsx: append user icon.
 *
 * @SvgUser, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import colors from '../general/colors.js';
import React, { Component } from 'react';

class SvgUser extends Component {
    constructor() {
        super();
        this.state = {
            body_color: colors['gray-5'],
            head_color: colors['gray-6'],
        }
        this.handleMouseOver = this.handleMouseOver.bind(this);
        this.handleMouseOut = this.handleMouseOut.bind(this);
    }

    handleMouseOver(event) {
        this.setState({ body_color: colors['green-3'] });
    }

    handleMouseOut(event) {
        this.setState({ body_color: colors['gray-5'] });
    }

    render() {
        return(
            <svg
                enableBackground='new 0 0 45 45'
                height='45px'
                onMouseOver={this.handleMouseOver}
                onMouseOut={this.handleMouseOut}
                preserveAspectRatio='xMidYMid meet'
                version='1.1'
                viewBox='0 0 512 512'
                width='45px'
                x='0px'
                xmlns='http://www.w3.org/2000/svg'
                y='0px'
            >
                <g>
	                <circle
                        cx='50%'
                        cy='42%'
                        r='80'
                        style={{fill:this.state.head_color}}
                    />
	                <path
                        d={`
                            M391.343, 433.041c0 -61.853 -25.654 -116.077 -64.162
                            -146.426c -16.932, 20.482 -42.531, 33.537 -71.18,
                            33.537c -28.649, 0 -54.25 -13.055 -71.181 -33.537c
                            -38.508, 30.349 -64.163, 84.573 -64.163, 146.426c 0,
                            0, 55.51, 19.959, 134.096, 19.959 S391.343, 433.041,
                            391.343, 433.041z
                        `}
                        style={{fill:this.state.body_color}}
                    />
                </g>
            </svg>
        );
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default SvgUser;
