/**
 * spinner.jsx: create ajax spinner container.
 *
 * @Spinner, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';

const Spinner = () => <div className="sending" />;
// triggered when 'state properties' change

// indicate which class can be exported, and instantiated via 'require'
export default Spinner;
