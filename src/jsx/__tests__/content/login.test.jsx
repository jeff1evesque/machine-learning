/**
 * login.test.jsx: jest + enzyme test.
 *
 */

import React from 'react';
import Enzyme, { mount, shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import LoginForm from '../../../../src/jsx/import/content/login.jsx';

Enzyme.configure({ adapter: new Adapter() });

describe('Login Component', () => {
    const mockDispatchLayout = jest.fn();
    const mockDispatchSpinner = jest.fn();

    it('loginForm should exist', () => {
        const wrapper = mount(
            <LoginForm
                dispatchLayout={mockDispatchLayout}
                dispatchSpinner={mockDispatchSpinner}
            />
        );
        expect(wrapper.contains(<form ref='loginForm'>)).toBeTruthy();
    });

    it('user[login] field should exist', () => {
        const wrapper = shallow(
            <LoginForm
                dispatchLayout={mockDispatchLayout}
                dispatchSpinner={mockDispatchSpinner}
            />
        );
        expect(wrapper.find('[name="user[login]"]').length).toHaveLength(1);
    });

    it('user[password] field should exist', () => {
        const wrapper = shallow(
            <LoginForm
                dispatchLayout={mockDispatchLayout}
                dispatchSpinner={mockDispatchSpinner}
            />
        );
        expect(wrapper.find('[name="user[password]"]').length).toHaveLength(1);
    });

    it('form submit button should exist', () => {
        const wrapper = shallow(
            <LoginForm
                dispatchLayout={mockDispatchLayout}
                dispatchSpinner={mockDispatchSpinner}
            />
        );
        expect(wrapper.find('[type="submit"]').length).toHaveLength(1);
    });
});
