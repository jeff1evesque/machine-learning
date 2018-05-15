/**
 * register.test.jsx: jest + enzyme test.
 *
 */

import React from 'react';
import Enzyme, { shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import RegisterForm from '../../../../src/jsx/import/content/register.jsx';

Enzyme.configure({ adapter: new Adapter() });

describe('Register Component', () => {
    const mockDispatchLayout = jest.fn();

    it('should render without throwing an error', () => {
        expect(
            shallow(
                <RegisterForm
                    dispatchLayout={mockDispatchLayout}
                />
            ).exists(<form ref='registerForm' />)
        ).toBe(true);
    });

    it('should render without throwing an error', () => {
        expect(
            shallow(
                <RegisterForm
                    dispatchLayout={mockDispatchLayout}
                />
            ).find('[name="user[login]"]').length
        ).toEqual(1);
    });

    it('should render without throwing an error', () => {
        expect(
            shallow(
                <RegisterForm
                    dispatchLayout={mockDispatchLayout}
                />
            ).find('[name="user[email]"]').length
        ).toEqual(1);
    });

    it('should render without throwing an error', () => {
        expect(
            shallow(
                <RegisterForm
                    dispatchLayout={mockDispatchLayout}
                />
            ).find('[name="user[password]"]').length
        ).toEqual(1);
    });

    it('should render without throwing an error', () => {
        expect(
            shallow(
                <RegisterForm
                    dispatchLayout={mockDispatchLayout}
                />
            ).find('[type="submit"]').length
        ).toEqual(1);
    });
});
