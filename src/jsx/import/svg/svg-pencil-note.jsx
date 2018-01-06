/**
 * svg-pencil-note.jsx: append pencil note icon.
 *
 * @SvgPencilNote, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import colors from '../general/colors.js';
import React, { Component } from 'react';

class SvgPencilNote extends Component {
    constructor() {
        super();
        this.state = {
            pencil_color: colors['gray-5'],
            inner_color: colors['gray-5'],
            outer_color: colors['gray-6'],
        }
        this.handleMouseOver = this.handleMouseOver.bind(this);
        this.handleMouseOut = this.handleMouseOut.bind(this);
    }

    handleMouseOver(event) {
        this.setState({ inner_color: colors['green-3'] });
    }

    handleMouseOut(event) {
        this.setState({ inner_color: colors['gray-5'] });
    }

    render() {
        return(
            <svg
                enableBackground='new 0 0 45 45'
                height='28px'
                onMouseOut={this.handleMouseOut}
                onMouseOver={this.handleMouseOver}
                preserveAspectRatio='xMidYMid meet'
                version='1.1'
                viewBox='0 0 512 512'
                width='45px'
                x='0px'
                xmlns='http://www.w3.org/2000/svg'
                y='0px'
            >
                <g>
                    <path
                        d={`
                            M448, 177.14V 448c 0, 35.344 -28.656, 64 -64, 64H 64c
                            -35.344, 0 -64 -28.656 -64 -64V 128c 0 -35.344, 28.656
                            -64, 64 -64h 270.844l -63.969, 64H 64v 320h 320V
                            241.156L 448, 177.14z
                        `}
                        fill={this.state.outer_color}
                    />
                    <path
                        d={`
                            M444.125, 0 L421.5, 22.625 l67.875, 67.891L 512, 67.875L
                            444.125, 0z
                        `}
                        fill={this.state.pencil_color}
                    />
                    <path
                        d={`
                            M398.875, 45.25L 376.25, 67.875 l67.875, 67.891 l22.625
                            -22.625L 398.875, 45.25z
                        `}
                        fill={this.state.pencil_color}
                    />
                    <path
                        d={`
                            M150, 294.188 l67.875, 67.875L 421.5, 158.406l -67.875
                            -67.891L 150, 294.188z
                        `}
                        fill={this.state.inner_color}
                    />
                    <path
                        d='M128, 384h 64l -64 -64V 384z'
                        fill={this.state.pencil_color}
                    />
                </g>
            </svg>
        );
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default SvgPencilNote;
