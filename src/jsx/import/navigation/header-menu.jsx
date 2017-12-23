/**
 * header-menu.jsx: menu for logged-in, and anonymous users.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React, { Component } from 'react';
import SvgHome from '../svg/svg-home.jsx';
import SvgBooks from '../svg/svg-books.jsx';
import SvgUser from '../svg/svg-user.jsx';
import SvgPencilNote from '../svg/svg-pencil-note.jsx';
import { Link } from 'react-router-dom'
import HomeLink from './menu-items/home.jsx';
import LoginLinkState from '../redux/container/login-link.jsx';
import RegisterLinkState from '../redux/container/register-link.jsx';
import { LinkContainer } from 'react-router-bootstrap';
import { Navbar, Nav, NavItem, NavDropdown } from 'react-bootstrap';
import { BreakpointRender } from 'rearm/lib/Breakpoint';
import breakpoints from '../general/breakpoints.js';

class HeaderMenu extends Component {
    showDesktopHeader() {
        return (
            <div>
                <HomeLink />
                <LoginLinkState />
                <RegisterLinkState />
            </div>
        )
    }
    showMobileHeader() {
        const session = <span>
            <span><SvgBooks /></span>
            <span className='menu-label'>Session</span>
        </span>
        return (
            <Navbar inverse collapseOnSelect>
                <Navbar.Header>
                    <Navbar.Brand>
                        <Link to='/'><SvgHome /></Link>
                    </Navbar.Brand>
                    <Navbar.Toggle />
                </Navbar.Header>
                <Navbar.Collapse>
                    <Nav pullRight>
                        <NavDropdown title={session} id='basic-nav-dropdown'>
                            <LinkContainer to='/session/data-new'>
                                <NavItem>Add new data</NavItem>
                            </LinkContainer>
                            <LinkContainer to='/session/data-append'>
                                <NavItem>Append data</NavItem>
                            </LinkContainer>
                            <LinkContainer to='/session/model-generate'>
                                <NavItem>Generate model</NavItem>
                            </LinkContainer>
                            <LinkContainer to='/session/model-predict'>
                                <NavItem>Make prediction</NavItem>
                            </LinkContainer>
                            <LinkContainer to='/session/results'>
                                <NavItem>Review results</NavItem>
                            </LinkContainer>
                        </NavDropdown>
                    </Nav>
                    <Nav pullRight>
                        <LinkContainer to='/login'>
                            <NavItem className='nav-item'>
                                <span><SvgUser /></span>
                                <span className='menu-label'>Login</span>
                            </NavItem>
                        </LinkContainer>
                        <LinkContainer to='/register'>
                            <NavItem className='nav-item'>
                                <span><SvgPencilNote /></span>
                                <span className='menu-label'>Register</span>
                            </NavItem>
                        </LinkContainer>
                    </Nav>
                </Navbar.Collapse>
            </Navbar>
        )
    }
    renderContent() {
        const desktopMenu = this.showDesktopHeader();
        const mobileMenu = this.showMobileHeader();

        if (
            !!this.props &&
            !!this.props.layout &&
            !!this.props.layout.type &&
            this.props.layout.type == 'login'
        ) {
            return (
                <nav
                    className='main-navigation menu-login'
                >
                    <div className='col-sm-12'><HomeLink /></div>
                </nav>
            );
        } else if (
            !!this.props &&
            !!this.props.layout &&
            !!this.props.layout.type &&
            this.props.layout.type == 'register'
        ) {
            return (
                <nav
                    className='main-navigation menu-register'
                >
                    <div className='col-sm-2'><HomeLink /></div>
                    <div className='col-sm-10'><LoginLinkState /></div>
                </nav>
            );
        }
        return (
            <nav
                className='main-navigation menu-home'
            >
                <BreakpointRender breakpoints={breakpoints} type='viewport'>
                    {bp => ( bp.isGt('small') ? desktopMenu : mobileMenu )}
                </BreakpointRender>
            </nav>
        );
    }
    // display result
    render() {
        const selectedContent = this.renderContent();
        return (selectedContent);
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default HeaderMenu;
