/**
 * analysis.test.jsx: jest + enzyme test.
 *
 */

import React from 'react';
import { shallow } from 'enzyme';
import AnalysisLayout from '../../../src/jsx/import/layout/analysis.jsx'

describe('AnalysisLayout Component', () => {
    it('should render without throwing an error', () => {
        expect(shallow(<AnalysisLayout />).exists(<form ref='analysisForm'></form>)).toBe(true)
    });

    it('should render correct routes', () => {
        const wrapper = shallow(<AnalysisLayout />);
        const pathMap = wrapper.find(Route).reduce((pathMap, route) => {
            const routeProps = route.props();
            pathMap[routeProps.path] = routeProps.component;
            return pathMap;
        }, {});

        expect(pathMap['/session/data-new']).toBe(DataNewState);
        expect(pathMap['/session/data-append']).toBe(DataAppendState);
        expect(pathMap['/session/model-generate']).toBe(ModelGenerateState);
        expect(pathMap['/session/model-predict']).toBe(ModelPredictState);
        expect(pathMap['/session/current-result']).toBe(CurrentResultState);
        expect(pathMap['/session/results']).toBe(ResultsDisplayState);
    });
});
