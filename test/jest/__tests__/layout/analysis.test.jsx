/**
 * analysis.test.jsx: jest + enzyme test.
 *
 */

import React from 'react';
import { shallow } from 'enzyme';
import AnalysisLayout from '../../../../src/jsx/import/layout/analysis.jsx';
import DataNewState from '../../../../src/jsx/import/redux/container/data-new.jsx';
import DataAppendState from '../../../../src/jsx/import/redux/container/data-append.jsx';
import ModelGenerateState from '../../../../src/jsx/import/redux/container/model-generate.jsx';
import ModelPredictState from '../../../../src/jsx/import/redux/container/model-predict.jsx';
import CurrentResultState from '../../../../src/jsx/import/redux/container/current-result.jsx';
import ResultsDisplayState from '../../../../src/jsx/import/redux/container/results.jsx';
import CurrentResultLink from '../../../../src/jsx/import/navigation/menu-items/current-result.jsx';

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
