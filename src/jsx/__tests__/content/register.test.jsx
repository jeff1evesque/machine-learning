/**
 * register.test.jsx: jest + enzyme test.
 *
 */

import React from 'react';
import Enzyme, { mount, shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import RegisterForm from '../../../../src/jsx/import/content/register.jsx';

Enzyme.configure({ adapter: new Adapter() });

describe('Register Component', () => {
    const mockDispatchLayout = jest.fn();

    it('registerForm should exist', () => {
        const wrapper = mount(
            <RegisterForm
                dispatchLayout={mockDispatchLayout}
            />
        );
        expect(wrapper.contains(<form ref='registerForm'>)).toBeTruthy();
    });

    it('user[login] field should exist', () => {
        const wrapper = shallow(
            <RegisterForm
                dispatchLayout={mockDispatchLayout}
            />
        );
        expect(wrapper.find('[name="user[login]"]').length).toEqual(1);
    });

    it('[name="user[email]"] field should exist', () => {
        const wrapper = shallow(
            <RegisterForm
                dispatchLayout={mockDispatchLayout}
            />
        );
        expect(wrapper.find('[name="user[email]"]').length).toEqual(1);
    });

    it('[name="user[password]"] field should exist', () => {
            <RegisterForm
                dispatchLayout={mockDispatchLayout}
            />
        );
        expect(wrapper.find('[name="user[password]"]').length).toEqual(1);
    });

    it('submit buttom should exist', () => {
        const wrapper = shallow(
            <RegisterForm
                dispatchLayout={mockDispatchLayout}
            />
        );
        expect(wrapper.find('[type="submit"]').length).toEqual(1);
    });
});
