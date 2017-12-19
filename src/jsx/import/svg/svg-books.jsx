/**
 * svg-books.jsx: append book icon.
 *
 * @SvgBooks, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import colors from '../general/colors.js';
import React, { Component } from 'react';

class SvgBooks extends Component {
    // initial 'state properties'
    constructor() {
        super();
        this.state = {
            inner_color: colors['gray-5'],
            outer_color: colors['gray-6'],
        }
        this.mouseOverIcon = this.mouseOverIcon.bind(this);
        this.mouseOutIcon = this.mouseOutIcon.bind(this);
    }
    // callback for mouseOver svg
    mouseOverIcon(event) {
        this.setState({ outer_color: colors['green-3'] });
    }
    // callback for mouseOut svg
    mouseOutIcon(event) {
        this.setState({ outer_color: colors['gray-6'] });
    }
    // triggered when 'state properties' change
    render() {
        return(
            <svg
                version='1.1'
                width='45px'
                height='45px'
                viewBox='0 0 225 225'
                preserveAspectRatio='xMidYMid meet'
                onMouseOver={this.mouseOverIcon}
                onMouseOut={this.mouseOutIcon}
            >
                <g
                    transform='translate(20, 280) scale(0.1, -0.1)'
                    stroke='none'
                >
                    <path
                        fill={this.state.outer_color}
                        d={`
                            M280 1970 l0 -90 190 0 190 0 0 90 0 90 -190 0 -190
                            0 0 -90z
                        `}
                    />
                    <path
                        fill={this.state.outer_color}
                        d={`
                            M750 1970 l0 -90 185 0 185 0 0 90 0 90 -185 0 -185
                            0 0 -90z
                        `}
                    />
                    <path
                        fill={this.state.outer_color}
                        d={`
                            M1420 1715 c-30 -7 -90 -21 -134 -30 l-78 -17 6 -41 c4
                            -23 9 -43 11 -45 3 -4 146 26 236 49 l37 9 -10 42 c-5
                            23 -10 43 -11 44 -1 1 -27 -4 -57 -11z
                        `}
                    />
                    <path
                        fill={this.state.inner_color}
                        d={`
                            M280 1455 l0 -325 190 0 190 0 0 325 0 325 -190 0
                            -190 0 0 -325z
                        `}
                    />
                    <path
                        fill={this.state.inner_color}
                        d={`
                            M1370 1512 c-63 -14 -117 -27 -119 -28 -3 -3 89 -444
                            94 -452 2 -2 225 44 257 54 14 4 15 10 3 62 -7 31 -30
                            132 -51 225 -29 132 -40 167 -53 166 -9 0 -68 -12 -131
                            -27z
                        `}
                    />
                    <path
                        fill={this.state.inner_color}
                        d={`
                            M750 1455 l0 -325 185 0 185 0 0 325 0 325 -185 0
                            -185 0 0 -325z
                        `}
                    />
                    <path
                        fill={this.state.outer_color}
                        d={`
                            M280 940 l0 -90 190 0 190 0 0 90 0 90 -190 0 -190
                            0 0 -90z
                        `}
                    />
                    <path
                        fill={this.state.outer_color}
                        d={`
                            M750 940 l0 -90 185 0 185 0 0 90 0 90 -185 0 -185
                            0 0 -90z
                        `}
                    />
                    <path
                        fill={this.state.outer_color}
                        d={`
                            M1480 961 l-113 -26 7 -40 c3 -22 8 -42 10 -44 5 -5
                            257 49 266 58 4 4 3 23 -3 44 -12 44 -11 44 -167 8z
                        `}
                        />
                </g>
            </svg>
        );
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default SvgBooks;
