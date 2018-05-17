/**
 * analysis.test.jsx: jest + enzyme test.
 *
 */

import React from 'react';
import { MemoryRouter } from 'react-router';
import Enzyme, { mount, shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import { Provider } from 'react-redux';
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
    const mockGetState = jest.fn();
    const mockDispatchLayout = jest.fn();

    it('should render home route', () => {
        const wrapper = mount(
            <Provider store={{getState: mockGetState}}>
                <MemoryRouter initialEntries={[ '/' ]}>
                    <MainRoute dispatchLayout={mockDispatchLayout} />
                </MemoryRouter>
            </Provider>
        );
        expect(wrapper.find(HomePageState)).toHaveLength(1);
    });

    it('should render login route', () => {
        const wrapper = mount(
            <Provider store={{getState: mockGetState}}>
                <MemoryRouter initialEntries={[ '/login' ]}>
                    <MainRoute dispatchLayout={mockDispatchLayout} />
                </MemoryRouter>
            </Provider>
        );
        expect(wrapper.find(LoginLayout)).toHaveLength(1);
    });

    it('should render logout route', () => {
        const wrapper = mount(
            <Provider store={{getState: mockGetState}}>
                <MemoryRouter initialEntries={[ '/logout' ]}>
                    <MainRoute dispatchLayout={mockDispatchLayout} />
                </MemoryRouter>
            </Provider>
        );
        expect(wrapper.find(LoginLayout)).toHaveLength(1);
    });

    it('should render register route', () => {
        const wrapper = mount(
            <Provider store={{getState: mockGetState}}>
                <MemoryRouter initialEntries={[ '/register' ]}>
                    <MainRoute dispatchLayout={mockDispatchLayout} />
                </MemoryRouter>
            </Provider>
        );
        expect(wrapper.find(RegisterLayout)).toHaveLength(1);
    });

    it('should render analysis route', () => {
        const wrapper = mount(
            <Provider store={{getState: mockGetState}}>
                <MemoryRouter initialEntries={[ '/register' ]}>
                    <MainRoute dispatchLayout={mockDispatchLayout} />
                </MemoryRouter>
            </Provider>
        );
        expect(wrapper.find(AnalysisLayoutState)).toHaveLength(1);
    });
});
