/**
 * analysis.test.jsx: jest + enzyme test.
 *
 */

import React from 'react';
import { MemoryRouter } from 'react-router';
import Enzyme, { mount } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import { Provider } from 'react-redux';
import { createStore, combineReducers } from 'redux';
import user from '../../../../src/jsx/import/redux/reducer/login.jsx';
import layout from '../../../../src/jsx/import/redux/reducer/layout.jsx';
import page from '../../../../src/jsx/import/redux/reducer/page.jsx';
import data from '../../../../src/jsx/import/redux/reducer/data.jsx';
import SessionRoute from '../../../../src/jsx/import/route/session-route.jsx';
import ResultRoute from '../../../../src/jsx/import/route/result-route.jsx';
import AnalysisLayout from '../../../../src/jsx/import/layout/analysis.jsx';
import DataNewState from '../../../../src/jsx/import/redux/container/data-new.jsx';
import DataAppendState from '../../../../src/jsx/import/redux/container/data-append.jsx';
import ModelGenerateState from '../../../../src/jsx/import/redux/container/model-generate.jsx';
import ModelPredictState from '../../../../src/jsx/import/redux/container/model-predict.jsx';
import CurrentResultState from '../../../../src/jsx/import/redux/container/current-result.jsx';
import ResultsDisplayState from '../../../../src/jsx/import/redux/container/results.jsx';
import store from '../../../../src/jsx/import/redux/store.jsx';
import jsdom from 'jsdom';

Enzyme.configure({ adapter: new Adapter() });

describe('AnalysisLayout Component', () => {
    const mockDispatchLayout = jest.fn();
    const store = createStore(
        combineReducers({user, page, data, layout}),
    );

    it('analysisForm should exist', () => {
        const wrapper = mount(
            <AnalysisLayout
                dispatchLayout={mockDispatchLayout}
            />
        );
        expect(wrapper.contains(<form ref='analysisForm'>)).toBeTruthy();
    });

    it('url should render DataNewState component', () => {
        const wrapper = mount(
            <Provider store={store}>
                <MemoryRouter initialEntries={[ '/session/data-new' ]}>
                    <SessionRoute/>
                </MemoryRouter>
            </Provider>
        );
        expect(wrapper.contains(DataNewState)).toBeTruthy();
    });

    it('url should render DataAppendState component', () => {
        const wrapper = mount(
            <Provider store={store}>
                <MemoryRouter initialEntries={[ '/session/data-append' ]}>
                    <SessionRoute/>
                </MemoryRouter>
            </Provider>
        );
        expect(wrapper.find(DataAppendState)).toBeTruthy();
    });

    it('url should render ModelGenerateState component', () => {
        const wrapper = mount(
            <Provider store={store}>
                <MemoryRouter initialEntries={[ '/session/model-generate' ]}>
                    <SessionRoute/>
                </MemoryRouter>
            </Provider>
        );
        expect(wrapper.find(ModelGenerateState)).toBeTruthy();
    });

    it('url should render ModelPredictState component', () => {
        const wrapper = mount(
            <Provider store={store}>
                <MemoryRouter initialEntries={[ '/session/model-predict' ]}>
                    <SessionRoute/>
                </MemoryRouter>
            </Provider>
        );
        expect(wrapper.find(ModelPredictState)).toBeTruthy();
    });

    it('url should render CurrentResultState component', () => {
        const wrapper = mount(
            <Provider store={store}>
                <MemoryRouter initialEntries={[ '/session/current-result' ]}>
                    <ResultRoute/>
                </MemoryRouter>
            </Provider>
        );
        expect(wrapper.find(CurrentResultState)).toBeTruthy();
    });

    it('url should render ResultsDisplayState component', () => {
        const wrapper = mount(
            <Provider store={store}>
                <MemoryRouter initialEntries={[ '/session/results' ]}>
                    <ResultRoute/>
                </MemoryRouter>
            </Provider>
        );
        expect(wrapper.find(ResultsDisplayState)).toBeTruthy();
    });
});
