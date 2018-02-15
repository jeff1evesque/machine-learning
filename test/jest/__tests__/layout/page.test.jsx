/**
 * analysis.test.jsx: jest + enzyme test.
 *
 */

import React from 'react';
import { shallow } from 'enzyme';
import PageLayout from '../../../../src/jsx/import/layout/page.jsx';
import HomePageState from '../../../src/jsx/import/redux/container/home-page.jsx';
import UserMenuState from '../../../src/jsx/import/redux/container/user-menu.jsx';
import HeaderMenuState from '../../../src/jsx/import/redux/container/header-menu.jsx';
import AnalysisLayoutState from '../../../src/jsx/import/redux/container/analysis-layout.jsx';
import LoginLayout from '../../../src/jsx/import/layout/login.jsx';
import RegisterLayout from '../../../src/jsx/import/layou/register.jsx';

describe('PageLayout Component', () => {
    it('should render correct routes', () => {
        const wrapper = shallow(<PageLayout />);
        const pathMap = wrapper.find(Route).reduce((pathMap, route) => {
            const routeProps = route.props();
            pathMap[routeProps.path] = routeProps.component;
            return pathMap;
        }, {});

        expect(pathMap['/']).toBe(HomePageState);
        expect(pathMap['/login']).toBe(LoginLayout);
        expect(pathMap['/logout']).toBe(LoginLayout);
        expect(pathMap['/register']).toBe(RegisterLayout);
        expect(pathMap['/session']).toBe(AnalysisLayoutState);
    });
});
