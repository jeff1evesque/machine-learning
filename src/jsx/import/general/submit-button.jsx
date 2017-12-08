/**
 * submit-button.jsx: append dynamic submit button.
 *
 * @Submit, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React, { Component } from 'react';

class Submit extends Component {
    // triggered when 'state properties' change
    render() {
        const disabled = this.props.btnDisabled ? true : false;
        const buttonValue = this.props.btnValue ? this.props.btnValue : 'Submit';
        const clickCallback = this.props.onClick ? this.props.onClick : '';
        const cssClass = this.props.cssClass ? this.props.cssClass : 'form-submit';

        return (
            <input
                disabled={disabled}
                type='submit'
                className={cssClass}
                onClick={clickCallback}
                value={buttonValue}
            />
        );
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default Submit;
