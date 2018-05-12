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
    it('should render without throwing an error', () => {
        expect(shallow(<RegisterForm />).exists(<form ref='registerForm'></form>)).toBe(true)
    });

    it('should render a username input', () => {
        expect(shallow(<RegisterForm />).find('[name="user[login]"]').length).toEqual(1)
    });

    it('should render an email input', () => {
        expect(shallow(<RegisterForm />).find('[name="user[email]"]').length).toEqual(1)
    });

    it('should render a password input', () => {
        expect(shallow(<RegisterForm />).find('[name="user[password]"]').length).toEqual(1)
    });

    it('should render a submit input', () => {
        expect(shallow(<RegisterForm />).find('[type="submit"]').length).toEqual(1)
    });
});
