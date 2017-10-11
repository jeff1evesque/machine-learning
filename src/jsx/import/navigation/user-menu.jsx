/**
 * user-menu.jsx: menu for logged-in, and anonymous users.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import SvgHome from '../svg/svg-home.jsx';
import { Link } from 'react-router-dom'
import { LinkContainer } from 'react-router-bootstrap';
import { Navbar, Nav, NavItem, NavDropdown, MenuItem } from 'react-bootstrap';

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
            <div>
                <Navbar inverse collapseOnSelect>
                    <Navbar.Header>
                        <Navbar.Brand>
                            <Link to='/'><SvgHome /></Link>
                        </Navbar.Brand>
                        <Navbar.Toggle />
                    </Navbar.Header>
                    <Navbar.Collapse>
                        <Nav pullRight>
                            <NavDropdown title={user} id='basic-nav-dropdown'>
                                <LinkContainer to='/session'>
                                    <NavItem>Dashboard</NavItem>
                                </LinkContainer>
                                <MenuItem divider />
                                <LinkContainer to='/logout'>
                                    <NavItem>Sign out</NavItem>
                                </LinkContainer>
                            </NavDropdown>
                        </Nav>
                    </Navbar.Collapse>
                </Navbar>
            </div>
        );
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default UserMenu;
