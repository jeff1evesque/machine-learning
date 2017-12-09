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

class RangeSlider extends Component {
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
        this.setState({
            value: value
        })
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
                    min={min}
                    max={max}
                    tooltip={tooltip}
                    step={step}
                    value={value}
                    onChange={this.handleChange}
                />
                <div className='slider-value'>{value}</div>
            </div>
        )
    }
}

export default RangeSlider
