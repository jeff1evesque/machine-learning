/**
 * user-menu.jsx: menu for logged-in, and anonymous users.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import { Navbar, Nav, NavItem, NavDropdown, MenuItem } from 'react-bootstrap';
import LinkContainer from 'react-router-bootstrap';

var UserMenu = React.createClass({
    render: function() {
        var user = 'anonymous';
        if (
            this.props &&
            this.props.user &&
            !!this.props.user.name &&
            this.props.user.name != 'anonymous'
        ) {
            var user = this.props.user.name;
        }

        return(
            <Navbar inverse collapseOnSelect>
                <Navbar.Header>
                    <Navbar.Brand>
                        <LinkContainer to='/'>
                            <MenuItem>MLearning</MenuItem>
                        </LinkContainer>
                    </Navbar.Brand>
                    <Navbar.Toggle />
                </Navbar.Header>
                <Navbar.Collapse>
                    <Nav>
                        <NavDropdown eventKey={1} title='My Account' id='basic-nav-dropdown'>
                            <div>Signed in as {user}</div>
                            <MenuItem divider />
                            <LinkContainer eventKey={1.1} href='/session'>
                                <MenuItem>Dashboard</MenuItem>
                            </LinkContainer>
                            <MenuItem divider />
                            <LinkContainer eventKey={1.2} href='/logout'>
                                <MenuItem>Sign out</MenuItem>
                            </LinkContainer>
                        </NavDropdown>
                    </Nav>
                </Navbar.Collapse>
            </Navbar>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default UserMenu
