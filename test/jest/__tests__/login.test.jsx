/**
 * login.test.jsx: jest + enzyme test.
 *
 */

import React from 'react';
import { shallow } from 'enzyme';
import LoginForm from '../../../src/jsx/import/content/login.jsx'

describe('Login Component', () => {
    it('should render without throwing an error', () => {
        expect(shallow(<LoginForm />).exists(<form ref='loginForm'></form>)).toBe(true)
    });

    it('renders email input', () => {
        expect(shallow(<LoginForm />).find('[name="user[login]"]').length).toEqual(1)
    });

    it('renders password input', () => {
        expect(shallow(<LoginForm />).find('[name="user[password]"]').length).toEqual(1)
    });

    it('renders submit input', () => {
        expect(shallow(<LoginForm />).find('[type="submit"]').length).toEqual(1)
    });
});
