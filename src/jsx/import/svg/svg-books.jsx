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
    constructor() {
        super();
        this.state = {
            inner_color: colors['gray-5'],
            outer_color: colors['gray-6'],
        }
        this.handleMouseOver = this.handleMouseOver.bind(this);
        this.handleMouseOut = this.handleMouseOut.bind(this);
    }

    handleMouseOver(event) {
        this.setState({ outer_color: colors['green-3'] });
    }

    handleMouseOut(event) {
        this.setState({ outer_color: colors['gray-6'] });
    }

    render() {
        return(
            <svg
                height='45px'
                onMouseOver={this.handleMouseOver}
                onMouseOut={this.handleMouseOut}
                preserveAspectRatio='xMidYMid meet'
                version='1.1'
                viewBox='0 0 225 225'
                width='45px'
            >
                <g
                    stroke='none'
                    transform='translate(20, 280) scale(0.1, -0.1)'
                >
                    <path
                        d={`
                            M280 1970 l0 -90 190 0 190 0 0 90 0 90 -190 0 -190
                            0 0 -90z
                        `}
                        fill={this.state.outer_color}
                    />
                    <path
                        d={`
                            M750 1970 l0 -90 185 0 185 0 0 90 0 90 -185 0 -185
                            0 0 -90z
                        `}
                        fill={this.state.outer_color}
                    />
                    <path
                        d={`
                            M1420 1715 c-30 -7 -90 -21 -134 -30 l-78 -17 6 -41 c4
                            -23 9 -43 11 -45 3 -4 146 26 236 49 l37 9 -10 42 c-5
                            23 -10 43 -11 44 -1 1 -27 -4 -57 -11z
                        `}
                        fill={this.state.outer_color}
                    />
                    <path
                        d={`
                            M280 1455 l0 -325 190 0 190 0 0 325 0 325 -190 0
                            -190 0 0 -325z
                        `}
                        fill={this.state.inner_color}
                    />
                    <path
                        d={`
                            M1370 1512 c-63 -14 -117 -27 -119 -28 -3 -3 89 -444
                            94 -452 2 -2 225 44 257 54 14 4 15 10 3 62 -7 31 -30
                            132 -51 225 -29 132 -40 167 -53 166 -9 0 -68 -12 -131
                            -27z
                        `}
                        fill={this.state.inner_color}
                    />
                    <path
                        d={`
                            M750 1455 l0 -325 185 0 185 0 0 325 0 325 -185 0
                            -185 0 0 -325z
                        `}
                        fill={this.state.inner_color}
                    />
                    <path
                        d={`
                            M280 940 l0 -90 190 0 190 0 0 90 0 90 -190 0 -190
                            0 0 -90z
                        `}
                        fill={this.state.outer_color}
                    />
                    <path
                        d={`
                            M750 940 l0 -90 185 0 185 0 0 90 0 90 -185 0 -185
                            0 0 -90z
                        `}
                        fill={this.state.outer_color}
                    />
                    <path
                        d={`
                            M1480 961 l-113 -26 7 -40 c3 -22 8 -42 10 -44 5 -5
                            257 49 266 58 4 4 3 23 -3 44 -12 44 -11 44 -167 8z
                        `}
                        fill={this.state.outer_color}
                    />
                </g>
            </svg>
        );
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default SvgBooks;
