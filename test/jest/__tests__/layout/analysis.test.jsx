/**
 * analysis.test.jsx: jest + enzyme test.
 *
 */

import React from 'react';
import { Route } from 'react-router-dom';
import Enzyme, { shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import { Provider } from 'react-redux';
import { createStore, combineReducers } from 'redux';
import AnalysisLayout from '../../../../src/jsx/import/layout/analysis.jsx';
import DataNewState from '../../../../src/jsx/import/redux/container/data-new.jsx';
import DataAppendState from '../../../../src/jsx/import/redux/container/data-append.jsx';
import ModelGenerateState from '../../../../src/jsx/import/redux/container/model-generate.jsx';
import ModelPredictState from '../../../../src/jsx/import/redux/container/model-predict.jsx';
import CurrentResultState from '../../../../src/jsx/import/redux/container/current-result.jsx';
import ResultsDisplayState from '../../../../src/jsx/import/redux/container/results.jsx';
import CurrentResultLink from '../../../../src/jsx/import/navigation/menu-items/current-result.jsx';
import SessionRoute from '../../../../src/jsx/import/route/session-route.jsx';
import store from '../../../../src/jsx/import/redux/store.jsx';

Enzyme.configure({ adapter: new Adapter() });

describe('AnalysisLayout Component', () => {
    const store = createStore(
        combineReducers({user, page, data, layout}),
    );

    it('should render without throwing an error', () => {
        expect(
            shallow(
                <AnalysisLayout
                    dispatchLayout={mockDispatchLayout}
                />
            ).exists(<form ref='analysisForm'>)
        ).toBe(true);
    });

    it('should render data-new route', () => {
        const wrapper = mount(
            <Provider store={store}>
                <MemoryRouter initialEntries={[ '/session/data-new' ]}>
                    <SessionRoute/>
                </MemoryRouter>
            </Provider>
        );
        expect(wrapper.find(DataNewState)).toHaveLength(1);
    });

    it('should render data-append route', () => {
        const wrapper = mount(
            <Provider store={store}>
                <MemoryRouter initialEntries={[ '/session/data-append' ]}>
                    <SessionRoute/>
                </MemoryRouter>
            </Provider>
        );
        expect(wrapper.find(DataAppendState)).toHaveLength(1);
    });

    it('should render model-generate route', () => {
        const wrapper = mount(
            <Provider store={store}>
                <MemoryRouter initialEntries={[ '/session/model-generate' ]}>
                    <SessionRoute/>
                </MemoryRouter>
            </Provider>
        );
        expect(wrapper.find(ModelGenerateState)).toHaveLength(1);
    });

    it('should render model-predict route', () => {
        const wrapper = mount(
            <Provider store={store}>
                <MemoryRouter initialEntries={[ '/session/model-predict' ]}>
                    <SessionRoute/>
                </MemoryRouter>
            </Provider>
        );
        expect(wrapper.find(ModelPredictState)).toHaveLength(1);
    });

    it('should render current-result route', () => {
        const wrapper = mount(
            <Provider store={store}>
                <MemoryRouter initialEntries={[ '/session/current-result' ]}>
                    <SessionRoute/>
                </MemoryRouter>
            </Provider>
        );
        expect(wrapper.find(CurrentResultState)).toHaveLength(1);
    });

    it('should render results route', () => {
        const wrapper = mount(
            <Provider store={store}>
                <MemoryRouter initialEntries={[ '/session/results' ]}>
                    <SessionRoute/>
                </MemoryRouter>
            </Provider>
        );
        expect(wrapper.find(ResultsDisplayState)).toHaveLength(1);
    });
});
