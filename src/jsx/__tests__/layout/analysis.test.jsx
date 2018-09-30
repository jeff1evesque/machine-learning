/**
 * analysis.test.jsx: jest + enzyme test.
 *
 */

import React from 'react';
import { MemoryRouter } from 'react-router';
import Enzyme, { mount, shallow } from 'enzyme';
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

// workaround for react bootstrap
global.window = new jsdom.JSDOM().window;
global.document = window.document;

describe('AnalysisLayout Component', () => {
    const mockDispatchLayout = jest.fn();
    const store = createStore(
        combineReducers({user, page, data, layout}),
    );

    it('analysisForm should exist', () => {
        const wrapper = shallow(
            <AnalysisLayout
                dispatchLayout={mockDispatchLayout}
            />
        );
        expect(wrapper.exists(<form ref='analysisForm' />)).toBe(true);
    });

    it('url should render DataNewState component', () => {
        const wrapper = mount(
            <Provider store={store}>
                <MemoryRouter initialEntries={[ '/session/data-new' ]}>
                    <SessionRoute/>
                </MemoryRouter>
            </Provider>
        );
        expect(wrapper.find(DataNewState)).toHaveLength(1);
    });

    it('url should render DataAppendState component', () => {
        const wrapper = mount(
            <Provider store={store}>
                <MemoryRouter initialEntries={[ '/session/data-append' ]}>
                    <SessionRoute/>
                </MemoryRouter>
            </Provider>
        );
        expect(wrapper.find(DataAppendState)).toHaveLength(1);
    });

    it('url should render ModelGenerateState component', () => {
        const wrapper = mount(
            <Provider store={store}>
                <MemoryRouter initialEntries={[ '/session/model-generate' ]}>
                    <SessionRoute/>
                </MemoryRouter>
            </Provider>
        );
        expect(wrapper.find(ModelGenerateState)).toHaveLength(1);
    });

    it('url should render ModelPredictState component', () => {
        const wrapper = mount(
            <Provider store={store}>
                <MemoryRouter initialEntries={[ '/session/model-predict' ]}>
                    <SessionRoute/>
                </MemoryRouter>
            </Provider>
        );
        expect(wrapper.find(ModelPredictState)).toHaveLength(1);
    });

    it('url should render CurrentResultState component', () => {
        const wrapper = mount(
            <Provider store={store}>
                <MemoryRouter initialEntries={[ '/session/current-result' ]}>
                    <ResultRoute/>
                </MemoryRouter>
            </Provider>
        );
        expect(wrapper.find(CurrentResultState)).toHaveLength(1);
    });

    it('url should render ResultsDisplayState component', () => {
        const wrapper = mount(
            <Provider store={store}>
                <MemoryRouter initialEntries={[ '/session/results' ]}>
                    <ResultRoute/>
                </MemoryRouter>
            </Provider>
        );
        expect(wrapper.find(ResultsDisplayState)).toHaveLength(1);
    });
});
