/**
 * svg-home.jsx: append home button.
 *
 * @SvgHome, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import colors from '../general/colors.js';
import React, { Component } from 'react';

class SvgHome extends Component {
    // initial 'state properties'
    constructor() {
        super();
        this.state = {
            roof_color: colors['gray-5'],
            house_color: colors['gray-6'],
        }
        this.mouseOverImage = this.mouseOverImage.bind(this);
        this.mouseOutImage = this.mouseOutImage.bind(this);
    }
    // callback for mouseOver svg
    mouseOverImage(event) {
        this.setState({ roof_color: colors['green-3'] });
    }
    // callback for mouseOut svg
    mouseOutImage(event) {
        this.setState({ roof_color: colors['gray-5'] });
    }
    // triggered when 'state properties' change
    render() {
        const roof_color = this.props.roofColor
            ? this.props.roofColor
            : this.state.roof_color;

        const house_color = this.props.houseColor
            ? this.props.houseColor
            : this.state.house_color;

        return(
            <svg
                version='1.1'
                xmlns='http://www.w3.org/2000/svg'
                width='45px'
                height='45px'
                viewBox='0 0 626.000000 626.000000'
                preserveAspectRatio='xMidYMid meet'
                onMouseOver={this.mouseOverImage}
                onMouseOut={this.mouseOutImage}
            >
                <g
                    transform={`
                        translate(0.000000,626.000000)
                        scale(0.100000,-0.100000)
                    `}
                    stroke='none'
                >

                    <path
                        style={{fill:roof_color}}
                        d={`
                            M3020 5606 c-113 -25 -120 -31 -880 -666 -124 -103 -418
                            -348 -655 -545 -236 -196 -452 -376 -480 -399 -27 -23
                            -174 -145 -325 -271 -694 -578 -667 -554 -676 -601 -3
                            -18 -3 -45 0 -59 6 -24 225 -293 279 -344 16 -14 42 -25
                            69 -28 60 -7 29 -30 744 567 148 124 278 232 288 240 11
                            8 51 42 90 75 39 34 179 151 311 260 132 110 245 204 252
                            210 6 5 28 24 50 42 21 17 155 130 299 250 245 204 285
                            238 374 310 19 15 50 42 70 59 97 85 293 244 300 244 7 0
                            196 -154 301 -244 19 -17 55 -47 78 -66 24 -19 51 -42 61
                            -50 10 -8 107 -89 216 -180 110 -90 231 -192 270 -225 38
                            -33 89 -76 113 -95 24 -19 48 -40 54 -45 36 -31 574 -479
                            701 -584 83 -68 237 -197 342 -285 105 -89 203 -170 217
                            -181 13 -11 44 -37 68 -57 287 -241 289 -243 345 -243 42
                            0 58 5 79 25 56 51 275 321 281 345 11 46 -4 89 -49 132
                            -40 39 -191 166 -503 423 -76 63 -183 152 -236 197 l -97
                            84 -3 812 -3 812 -23 32 c-14 20 -37 36 -60 43 -50 13
                            -774 13 -824 0 -23 -7 -46 -23 -60 -43 -23 -32 -23 -34
                            -26 -425 -2 -223 -7 -392 -12 -390 -5 2 -109 87 -232 190
                            -568 477 -733 610 -786 637 -97 49 -211 62 -322 37z
                        `}
                    />

                    <path
                        style={{fill:house_color}}
                        d={`
                            M3085 4577c -23 -18 -104 -84 -180 -147 -76 -63 -220 -182
                            -320 -265 -100 -82 -199 -163 -220 -180 -21 -16 -72 -59
                            -114 -94 -42 -35 -227 -188 -411 -339 -184 -152 -401 -330
                            -481 -396 -80 -67 -216 -179 -302 -250 -127 -105 -158 -135
                            -162 -160 -3 -17 -5 -454 -3 -971 3 -891 4 -942 22 -983 25
                            -57 104 -126 160 -141 31 -8 273 -11 800 -11 l756 0 2 743
                            3 742 498 3 497 2 0 -745 0 -745 756 0 c527 0 769 3 800 11
                            56 15 135 84 160 141 18 41 19 92 22 983 2 517 0 954 -3
                            971 -6 34 -37 61 -811 694 -131 107 -324 267 -429 355 -106
                            88 -209 174 -231 190 -21 17 -108 89 -194 160 -382 318
                            -564 466 -572 464 -2 0 -21 -14 -43 -32z
                        `}
                    />

                </g>
            </svg>
        );
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default SvgHome;
