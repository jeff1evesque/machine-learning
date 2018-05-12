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
    it('should render without throwing an error', () => {
        expect(shallow(<LoginForm />).exists(<form ref='loginForm'></form>)).toBe(true)
    });

    it('should render an email input', () => {
        expect(shallow(<LoginForm />).find('[name="user[login]"]').length).toEqual(1)
    });

    it('should render a password input', () => {
        expect(shallow(<LoginForm />).find('[name="user[password]"]').length).toEqual(1)
    });

    it('should render a submit input', () => {
        expect(shallow(<LoginForm />).find('[type="submit"]').length).toEqual(1)
    });
});
