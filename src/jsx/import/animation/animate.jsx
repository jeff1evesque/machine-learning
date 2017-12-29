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

import React from 'react'
import * as d3 from 'd3'
import {withFauxDOM} from 'react-faux-dom'

class MyReactComponent extends React.Component {
    componentDidMount() {
        const w = window.innerWidth;
        const h = window.innerHeight;
        const faux = this.props.connectFauxDOM('svg', 'collision');

        let nodes = d3.range(200).map(function () {
          return { r: Math.random() * 12 + 4 };
        });

        let root = nodes[0];
        let color = d3.scaleOrdinal().range(d3.schemeCategory10);

        root.radius = 0;
        root.fixed = true;

        const forceX = d3.forceX(w / 2).strength(0.015);
        const forceY = d3.forceY(h / 2).strength(0.015);

        var svg = d3.select(faux)
          .attr('width', w)
          .attr('height', h)
          .append('g');

        svg.selectAll('circle')
            .data(nodes.slice(1))
            .enter()
            .append('circle')
            .attr('r', function (d) { return d.r; })
            .style('fill', function (d, i) { return color(i % 3); });

        root.radius = 0;
        root.fixed = true;

        function ticked(e) {
            svg.selectAll('circle')
            .attr('cx', function (d) { return d.x; })
            .attr('cy', function (d) { return d.y; });
        };

        let force = d3.forceSimulation()
            .velocityDecay(0.2)
            .force('x', forceX)
            .force('y', forceY)
            .force('collide', d3.forceCollide().radius(function (d) {
                if (d === root) {
                    return Math.random() * 50 + 100;
                }
                return d.r + 2;
            }).iterations(5))
            .nodes(nodes).on('tick', ticked);

        svg.on('mousemove', function () {
            root.fx = d3.event.pageX;
            root.fy = d3.event.pageY;
            force.alphaTarget(0.3).restart();//reheat the simulation
            this.props.animateFauxDOM(3500);
        });
        this.props.animateFauxDOM(3500);
    }

    render() {
        return (
            <div>{this.props.collision}</div>
        )
    }
}

MyReactComponent.defaultProps = {
  collision: 'loading'
}

export default withFauxDOM(MyReactComponent)
