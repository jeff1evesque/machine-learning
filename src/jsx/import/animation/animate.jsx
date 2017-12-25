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
        const w = 1280;
        const h = 800;
        const node = new ReactFauxDOM.Element('div');

        let nodes = d3.range(200).map(function() {
            return {radius: Math.random() * 12 + 4};
        });

        let color = d3.scaleOrdinal(d3.schemeCategory10);

        let force = d3.forceSimulation()
            .gravity(0.05)
            .charge(function(d, i) { return i ? 0 : -2000; })
            .nodes(nodes)
            .size([w, h]);

        let root = nodes[0];

        root.radius = 0;
        root.fixed = true;
        force.start();

        let svg = d3.select(node).append('svg:svg')
            .attr('width', w)
            .attr('height', h);

        svg.selectAll('circle')
            .data(nodes.slice(1))
            .enter()
            .append('svg:circle')
            .attr('r', function(d) { return d.radius - 2; })
            .style('fill', function(d, i) { return color(i % 3); });

        force.on('tick', function(e) {
            let i = 0;
            const q = d3.quadtree(nodes);
            const n = nodes.length;

            while (++i < n) {
                q.visit(collide(nodes[i]));
            }

            svg.selectAll('circle')
                .attr('cx', function(d) { return d.x; })
                .attr('cy', function(d) { return d.y; });
        });

        svg.on('mousemove', function() {
            const p1 = d3.svg.mouse(this);
            root.px = p1[0];
            root.py = p1[1];
            force.resume();
        });

        function collide(node) {
            const r = node.radius + 16;
            const nx1 = node.x - r;
            const nx2 = node.x + r;
            const ny1 = node.y - r;
            const ny2 = node.y + r;

            return function(quad, x1, y1, x2, y2) {
                if (quad.point && (quad.point !== node)) {
                    let x = node.x - quad.point.x;
                    let y = node.y - quad.point.y;
                    let l = Math.sqrt(x * x + y * y);
                    const r = node.radius + quad.point.radius;

                    if (l < r) {
                        l = (l - r) / l * .5;
                        node.x -= x *= l;
                        node.y -= y *= l;
                        quad.point.x += x;
                        quad.point.y += y;
                    }
                }

                return x1 > nx2
                    || x2 < nx1
                    || y1 > ny2
                    || y2 < ny1;
            };
        }

        return node.toReact();
    }
};

// indicate which class can be exported, and instantiated via 'require'
export default Animate;
