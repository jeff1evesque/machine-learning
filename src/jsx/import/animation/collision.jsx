/**
 * collision.jsx: d3js animation of ball collisions.
 *
 * @AnimateCollision, must be capitalized in order for reactjs to render it as
 *     a component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax, and requires the parent
 *       calling this component, to define the 'node' property.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import { Component } from 'react';
import rd3 from 'react-d3-library';
const RD3Component = rd3.Component;

class AnimateCollision extends Component {
    render() {
        return (
            <div>
                <RD3Component data={this.props.node} />
            </div>
        );
    }
};

// indicate which class can be exported, and instantiated via 'require'
export default AnimateCollision;
