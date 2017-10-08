/**
 * user-menu.jsx: menu for logged-in, and anonymous users.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import { Navbar, Nav, NavItem, NavDropdown, MenuItem } from 'react-bootstrap';
import { NavLink } from 'react-router-dom';

class UserMenu extends Component {
    render() {
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
                        <NavLink to='/'>MLearning</NavLink>
                    </Navbar.Brand>
                    <Navbar.Toggle />
                </Navbar.Header>
                <Navbar.Collapse>
                    <Nav>
                        <NavDropdown eventKey={1} title='My Account' id='basic-nav-dropdown'>
                            <div>Signed in as {user}</div>
                            <MenuItem divider />
                            <NavLink to='/session'>Dashboard</NavLink>
                            <MenuItem divider />
                            <NavLink to='/logout'>Sign out</NavLink>
                        </NavDropdown>
                    </Nav>
                </Navbar.Collapse>
            </Navbar>
        );
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default UserMenu;
