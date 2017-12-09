/**
 * range-slider.jsx: redux store for range slider.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React from 'react';
import { connect } from 'react-redux';
import RangeSlider from '../../general/range-slider.jsx';
import setRangeSlider from '../action/range-slider.jsx';

// wraps each function of the object to be dispatch callable
const mapDispatchToProps = (dispatch) => {
    return {
        dispatchRangeSlider: dispatch.bind(setRangeSlider)
    }
}

// pass selected properties from redux state tree to component
const RangeSliderState = connect(
    null,
    mapDispatchToProps
)(RangeSlider)

// indicate which class can be exported, and instantiated via 'require'
export default RangeSliderState
