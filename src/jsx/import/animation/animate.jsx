/**
 * animate.jsx: animates provided 'node' from parent:
 *
 *   - https://github.com/react-d3-library/react-d3-library
 *
 * @Animate, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React, { Component } from 'react';
import rd3 from 'react-d3-library';
const RD3Component = rd3.Component;

class Animate extends Component {
  render() {
    return (
      <div>
        <RD3Component data={this.props.node} />
      </div>
    )
  }
};

// indicate which class can be exported, and instantiated via 'require'
export default Animate;
