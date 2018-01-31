/**
 * range-slider.jsx: create responsive range slider.
 *
 * @RangeSlider, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React, { Component } from 'react'
import Slider from 'react-rangeslider'
import { setRangeSlider } from '../redux/action/page.jsx';
import PropTypes from 'prop-types';

class RangeSlider extends Component {
    // prob validation: static method, similar to class A {}; A.b = {};
    static propTypes = {
        dispatchRangeSlider: PropTypes.func,
        max: PropTypes.number,
        min: PropTypes.number,
        step: PropTypes.number,
        tooltip: PropTypes.bool,
        value: PropTypes.number,
        type: PropTypes.string,
    }

    constructor (props, context) {
        super(props, context)
        this.state = {
            min: -10,
            max: 10,
            tooltip: false,
            step: 0.5,
            value: 0,
        }
    }

    handleChange = (value) => {
        const type = this.props.type;
        this.setState({
            value: value
        });

        const action = setRangeSlider({ type: type, penalty: value });
        this.props.dispatchRangeSlider(action);
    }

    render() {
        const min = this.props.min ? this.props.min : this.state.min;
        const max = this.props.max ? this.props.max : this.state.max;
        const tooltip = this.props.tooltip ? this.props.tooltip : this.state.tooltip;
        const step = this.props.step ? this.props.step : this.state.step;
        const value = this.props.value ? this.props.value : this.state.value;

        return (
            <div className='slider'>
                <Slider
                    max={max}
                    min={min}
                    onChange={this.handleChange}
                    step={step}
                    tooltip={tooltip}
                    value={value}
                />
                <div className='slider-value'>{value}</div>
            </div>
        )
    }
}

export default RangeSlider
