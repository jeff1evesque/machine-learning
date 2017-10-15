/**
 * submit-button.jsx: append dynamic submit button.
 *
 * @Submit, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';

const Submit = (prosp) => {
  // triggered when 'state properties' change

  const buttonValue = this.props.btnValue ? this.props.btnValue : 'Submit';
  const clickCallback = this.props.onClick ? this.props.onClick : '';
  const cssClass = this.props.cssClass ? this.props.cssClass : 'form-submit';

  return (
    <input
      type="submit"
      className={cssClass}
      onClick={clickCallback}
      value={buttonValue}
    />
  );
};

// indicate which class can be exported, and instantiated via 'require'
export default Submit;
