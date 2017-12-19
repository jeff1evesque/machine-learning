/**
 * svg-pencil-note.jsx: append pencil note icon.
 *
 * @SvgPencilNoteIcon, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import colors from '../general/colors.js';
import React, { Component } from 'react';

class SvgPencilNoteIcon extends Component {
    // initial 'state properties'
    constructor() {
        super();
        this.state = {
            pencil_color: colors['gray-5'],
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
        this.setState({ inner_color: colors['gray-5'] });
    }
    // triggered when 'state properties' change
    render() {
        return(
            <svg
                version='1.1'
                xmlns='http://www.w3.org/2000/svg'
                width='45px'
                height='28px'
                x='0px'
                y='0px'
                viewBox='0 0 512 512'
                enableBackground='new 0 0 45 45'
                preserveAspectRatio='xMidYMid meet'
                onMouseOver={this.mouseOverHome}
                onMouseOut={this.mouseOutHome}
            >
                <g>
                    <path
                        fill={this.state.outer_color}
                        d={`
                            M448, 177.14V 448c 0, 35.344 -28.656, 64 -64, 64H 64c
                            -35.344, 0 -64 -28.656 -64 -64V 128c 0 -35.344, 28.656
                            -64, 64 -64h 270.844l -63.969, 64H 64v 320h 320V
                            241.156L 448, 177.14z
                        `}
                    />
                    <path
                        fill={this.state.pencil_color}
                        d={`
                            M444.125, 0 L421.5, 22.625 l67.875, 67.891L 512, 67.875L
                            444.125, 0z
                        `}
                    />
                    <path
                        fill={this.state.pencil_color}
                        d={`
                            M398.875, 45.25L 376.25, 67.875 l67.875, 67.891 l22.625
                            -22.625L 398.875, 45.25z
                        `}
                    />
                    <path
                        fill={this.state.inner_color}
                        d={`
                            M150, 294.188 l67.875, 67.875L 421.5, 158.406l -67.875
                            -67.891L 150, 294.188z
                        `}
                    />
                    <path
                        fill={this.state.pencil_color}
                        d='M128, 384h 64l -64 -64V 384z'
                    />
                </g>
            </svg>
        );
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default SvgPencilNoteIcon;
