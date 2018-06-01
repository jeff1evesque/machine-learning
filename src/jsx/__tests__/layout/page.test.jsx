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
import MainRoute from '../../../../src/jsx/import/route/main-route.jsx';
import HomePageState from '../../../../src/jsx/import/redux/container/home-page.jsx';
import UserMenuState from '../../../../src/jsx/import/redux/container/user-menu.jsx';
import HeaderMenuState from '../../../../src/jsx/import/redux/container/header-menu.jsx';
import AnalysisLayoutState from '../../../../src/jsx/import/redux/container/analysis-layout.jsx';
import LoginLayout from '../../../../src/jsx/import/layout/login.jsx';
import RegisterLayout from '../../../../src/jsx/import/layout/register.jsx';
import store from '../../../../src/jsx/import/redux/store.jsx';

Enzyme.configure({ adapter: new Adapter() });

describe('PageLayout Component', () => {
    const store = createStore(
        combineReducers({user, page, data, layout}),
    );

    it('url should render HomePageState component', () => {
        const wrapper = mount(
            <Provider store={store}>
                <MemoryRouter initialEntries={[ '/' ]}>
                    <MainRoute/>
                </MemoryRouter>
            </Provider>
        );
        expect(wrapper.find(HomePageState)).toHaveLength(1);
    });

    it('url should render LoginLayout component (login case)', () => {
        const wrapper = mount(
            <Provider store={store}>
                <MemoryRouter initialEntries={[ '/login' ]}>
                    <MainRoute/>
                </MemoryRouter>
            </Provider>
        );
        expect(wrapper.find(LoginLayout)).toHaveLength(1);
    });

    it('url should render LoginLayout component (logout case)', () => {
        const wrapper = mount(
            <Provider store={store}>
                <MemoryRouter initialEntries={[ '/logout' ]}>
                    <MainRoute/>
                </MemoryRouter>
            </Provider>
        );
        expect(wrapper.find(LoginLayout)).toHaveLength(1);
    });

    it('url should render RegisterLayout component', () => {
        const wrapper = mount(
            <Provider store={store}>
                <MemoryRouter initialEntries={[ '/register' ]}>
                    <MainRoute/>
                </MemoryRouter>
            </Provider>
        );
        expect(wrapper.find(RegisterLayout)).toHaveLength(1);
    });

    it('url should render AnalysisLayoutState component', () => {
        const wrapper = mount(
            <Provider store={store}>
                <MemoryRouter initialEntries={[ '/session' ]}>
                    <MainRoute/>
                </MemoryRouter>
            </Provider>
        );
        expect(wrapper.find(AnalysisLayoutState)).toHaveLength(1);
    });
});
