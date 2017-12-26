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
import * as d3 from 'd3';
import ReactFauxDOM from 'react-faux-dom';

class Animate extends Component {
    render() {
        const w = window.innerWidth;
        const h = window.innerHeight;
        const node = new ReactFauxDOM.Element('div');

        let nodes = d3.range(200).map(function() {
            return {r: Math.random() * 12 + 4};
        });

        let root = nodes[0];
        let color = d3.scaleOrdinal().range(d3.schemeCategory10);

        root.radius = 0;
        root.fixed = true;

        const forceX = d3.forceX(w / 2).strength(0.015);
        const forceY = d3.forceY(h / 2).strength(0.015);

        let force = d3.forceSimulation()
            .velocityDecay(0.2)
            .force('x', forceX)
            .force('y', forceY)
            .force('collide', d3.forceCollide().radius(function(d){
                if (d === root) {
                    return Math.random() * 50 + 100;
                }
                return d.r + 0.5;
            }).iterations(5))
            .nodes(nodes).on('tick', ticked);

            let svg = d3.select('body').append('svg')
                .attr('w', w)
                .attr('h', h);

            svg.selectAll('circle')
                .data(nodes.slice(1))
                .enter().append('circle')
                .attr('r', function(d) { return d.r; })
                .style('fill', function(d, i) { return color(i % 3); });

            function ticked(e) {
                svg.selectAll('circle')
                    .attr('cx', function(d) { return d.x; })
                    .attr('cy', function(d) { return d.y; });
            };

            svg.on('mousemove', function() {
                const p1 = d3.mouse(this);
                root.fx = p1[0];
                root.fy = p1[1];
                force.alphaTarget(0.3).restart();//reheat the simulation
            });

            return node.toReact();
        }
    };
}

// indicate which class can be exported, and instantiated via 'require'
export default Animate;
