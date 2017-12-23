/**
 * animate.jsx: d3js animation of ball collisions.
 *
 * @Animate, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax, and requires the parent
 *       calling this component, to define the 'node' property, which will
 *       represent the d3js object.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import rd3 from 'react-d3-library';
const RD3Component = rd3.Component;

const Animate = ({ node }) => <RD3Component data={node} />;

// indicate which class can be exported, and instantiated via 'require'
export default Animate;
