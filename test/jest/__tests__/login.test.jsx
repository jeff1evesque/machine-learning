/**
 * login.test.jsx: jest + enzyme test.
 *
 */

import React from 'react';
import { shallow, mount, render } from 'enzyme';
import LoginForm from '../../../src/jsx/import/content/login.jsx'

describe('Login Component', () => {
   it('should render without throwing an error', () => {
       expect(shallow(<LoginForm />).exists(<form ref='loginForm'></form>)).toBe(true)
   });
});
