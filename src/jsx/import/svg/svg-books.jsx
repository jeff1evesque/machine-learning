/**
 * svg-books.jsx: append book icon.
 *
 * @SvgBooksIcon, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import colors from '../general/colors.js';
import React, { Component } from 'react';

class SvgBooksIcon extends Component {
    // initial 'state properties'
    constructor() {
        super();
        this.state = {
            inner_color: colors['gray-5'],
            outer_color: colors['gray-6'],
        }
        this.mouseOverHome = this.mouseOverHome.bind(this);
        this.mouseOutHome = this.mouseOutHome.bind(this);
    }
    // callback for mouseOver svg
    mouseOverHome(event) {
        this.setState({ inner_color: colors['green-3'] });
    }
    // callback for mouseOut svg
    mouseOutHome(event) {
        this.setState({ inner_color: colors['gray-6'] });
    }
    // triggered when 'state properties' change
    render() {
        return(
            <svg
                version='1.1'
                width='50px'
                height='50px'
                viewBox='0 0 225 225'
                preserveAspectRatio='xMidYMid meet'
                onMouseOver={this.mouseOverHome}
                onMouseOut={this.mouseOutHome}
            >
                <g
                    transform='translate(20, 265) scale(0.1, -0.1)'
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
                        fill={this.state.inner_color}
                        d={`
                            M280 1455 l0 -325 190 0 190 0 0 325 0 325 -190 0
                            -190 0 0 -325z
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
                </g>
            </svg>
        );
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default SvgBooksIcon;
