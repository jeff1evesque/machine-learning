/**
 * animate.jsx: animates provided 'node' from parent:
 *
 *   - https://github.com/react-d3-library/react-d3-library
 *
 * @AnimateCollisions, must be capitalized in order for reactjs to render it as
 *     a component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import * as d3 from 'd3';
import { medium_minWidth } from '../general/breakpoints';
import hex from '../general/colors.js';

class AnimateCollisions extends Component {
    constructor() {
        super();
        const width = window.innerWidth;
        const height = window.innerHeight;

        if (width < medium_minWidth) {
            var node_qty = 150;
            var radius_delta = 0;
        } else {
            var node_qty = 200;
            var radius_delta = 4;
        }

        const nodes = this.generateNodes(node_qty, radius_delta);
        const force_strength = 0.01;

        this.state = {
            nodes: nodes,
            forceX: d3.forceX(width / 2).strength(force_strength),
            forceY: d3.forceY(height / 2).strength(force_strength),
            alpha_target: .4,
            iterations: 4,
            root: nodes[0],
            width: width,
            height: height,
            velocity_decay: .1,
            radius_delta: radius_delta,
        }
        this.getColor = this.getColor.bind(this);
        this.generateNodes = this.generateNodes.bind(this);
        this.renderD3 = this.renderD3.bind(this);
    }

    componentDidMount() {
        this.renderD3();
    }

    componentWillUnmount() {
        this.state.forceSimulation.stop();
    }

    generateNodes(quantity, delta) {
        return [...Array(quantity).keys()].map(function() {
            return { r: Math.random() * (12 + delta) };
        }.bind(null, delta));
    }

    getColor() {
        const colors = this.props.colors
            ? this.props.colors
            : [hex['blue'], hex['orange'], hex['green-6']];
        return colors[Math.floor(Math.random() * colors.length)];
    }

    renderD3() {
        const svg = d3.select(ReactDOM.findDOMNode(this.refs.animation));
        const nodes = this.props.nodes ? this.props.nodes : this.state.nodes;
        const forceX = this.props.forceX ? this.props.forceX : this.state.forceX;
        const forceY = this.props.forceY ? this.props.forceY : this.state.forceY;
        const alpha = this.props.alpha ? this.props.alpha : this.state.alpha_target;
        const iterations = this.props.iterations
            ? this.props.iterations
            : this.state.iterations;
        const root = nodes[0];
        const radius_delta = this.props.radius_delta
            ? this.props.radius_delta
            : (this.state.radius_delta > 0
                ? this.state.radius_delta
                : 3);

        root.radius = 0;
        root.fixed = true;

        svg.selectAll('circle')
            .data(nodes.slice(1));

        function ticked() {
            svg.selectAll('circle')
                .attr('cx', function(d) { return d.x; })
                .attr('cy', function(d) { return d.y; });
        };

        const force = d3.forceSimulation()
            .velocityDecay(this.state.velocity_decay)
            .force('x', forceX)
            .force('y', forceY)
            .force('collide', d3.forceCollide().radius(function(d) {
                if (d === root) {
                    return (Math.random() * 50) + (radius_delta * 25);
                }
                return d.r + 2;
            }).iterations(iterations))
            .nodes(nodes).on('tick', ticked);

        svg.on('mousemove', function() {
            const p1 = d3.mouse(this);
            root.fx = p1[0];
            root.fy = p1[1];

            // reheat the simulation
            force.alphaTarget(alpha).restart();
        });

        this.setState({forceSimulation: force});
    }

    render() {
        // use React to draw all the nodes, d3 calculates the x and y
        const nodes = this.state.nodes.slice(1).map((node, index) => {
            const color = this.getColor();
            return (
                <circle
                    cx={node.x}
                    cy={node.y}
                    fill={color}
                    key={`circle-${index}`}
                    r={node.r}
                />
            );
        });

        return (
            <svg
                className='d3-absolute'
                ref='animation'
                width={this.state.width}
                height={this.state.height}
            >
                <g>{nodes}</g>
            </svg>
        )
    }
}

AnimateCollisions.propTypes = {
    colors: PropTypes.array,
    nodes: PropTypes.array,
    forceX: PropTypes.func,
    forceY: PropTypes.func,
    alpha: PropTypes.number,
    iterations: PropTypes.number,
    radius_delta: PropTypes.number,
}

export default AnimateCollisions;
