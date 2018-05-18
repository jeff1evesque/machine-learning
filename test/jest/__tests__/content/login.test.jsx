/**
 * login.test.jsx: jest + enzyme test.
 *
 */

import React from 'react';
import Enzyme, { shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import LoginForm from '../../../../src/jsx/import/content/login.jsx';

Enzyme.configure({ adapter: new Adapter() });

describe('Login Component', () => {
    const mockDispatchLayout = jest.fn();
    const mockDispatchSpinner = jest.fn();

    it('should render without throwing an error', () => {
        const wrapper = shallow(
            <LoginForm
                dispatchLayout={mockDispatchLayout}
                 dispatchSpinner={mockDispatchSpinner}
            />
        );
        expect(wrapper.exists(<form ref='loginForm' />)).toBe(true);
    });

    it('should render without throwing an error', () => {
        const wrapper = shallow(
            <LoginForm
                dispatchLayout={mockDispatchLayout}
                dispatchSpinner={mockDispatchSpinner}
            />
        );
        expect(wrapper.find('[name="user[login]"]').length).toEqual(1);
    });

    it('should render without throwing an error', () => {
        const wrapper = shallow(
            <LoginForm
                dispatchLayout={mockDispatchLayout}
                dispatchSpinner={mockDispatchSpinner}
            />
        );
        expect(wrapper.find('[name="user[password]"]').length).toEqual(1);
    });

    it('should render without throwing an error', () => {
        const wrapper = shallow(
            <LoginForm
                dispatchLayout={mockDispatchLayout}
                dispatchSpinner={mockDispatchSpinner}
            />
        );
        expect(wrapper.find('[type="submit"]').length).toEqual(1);
    });
});
