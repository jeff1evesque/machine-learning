/**
 * user-menu.jsx: menu for logged-in, and anonymous users.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import SvgHome from '../svg/svg-home.jsx';
import SvgUserIcon from '../svg/svg-user.jsx';
import { Link, withRouter } from 'react-router-dom'
import setLogoutState from '../redux/action/logout.jsx';
import { LinkContainer } from 'react-router-bootstrap';
import { Navbar, Nav, NavItem, NavDropdown, MenuItem } from 'react-bootstrap';
import ajaxCaller from '../general/ajax-caller.js';
import { BreakpointRender } from 'rearm/lib/Breakpoint';
import breakpoints from '../general/breakpoints.js';

class UserMenu extends Component {
    constructor(props) {
      // @super is required when constructor defined
      // @props argument is fed into super, only if 'this.props' used in constructor
      // @this.props, works throughout class, regardless of above 'props' argument
      //     - requires callback to be binded to 'this'
      //
        super(props);
        this.state = {
            ajax_done_error: null,
            ajax_fail_error: null
        };

      // bind allows 'this' object reference
        this.handleClick = this.handleClick.bind(this);
        this.render = this.render.bind(this);
    }

    handleClick(event) {
        if (
            this.props &&
            this.props.user &&
            !!this.props.user.name &&
            this.props.user.name != 'anonymous'
        ) {
          // prevent page reload
            event.preventDefault();

          // local variables
            var ajaxArguments = {
                'endpoint': '/logout'
            };

          // asynchronous callback: ajax 'done' promise
            ajaxCaller(function (asynchObject) {
            // Append to DOM
                if (asynchObject && asynchObject.error) {
                    this.setState({ajax_done_error: asynchObject.error});
                }
                else if (asynchObject) {
                    if (asynchObject.status == '0') {
                        var action = setLogoutState();
                        this.props.dispatchLogout(action);
                        sessionStorage.removeItem('username');
                    }

                    if (
                        this.props &&
                        this.props.location &&
                        this.props.location.pathname &&
                        this.props.location.pathname != '/' &&
                        asynchObject.status == '0'
                    ) {
                        this.props.history.push('/');
                    }
                }
            }.bind(this),
          // asynchronous callback: ajax 'fail' promise
            function (asynchStatus, asynchError) {
                if (asynchStatus) {
                    this.setState({ajax_fail_status: asynchStatus});
                    console.log('Error Status: ' + asynchStatus);
                }
                if (asynchError) {
                    this.setState({ajax_fail_error: asynchError});
                    console.log('Error Thrown: ' + asynchError);
                }
            }.bind(this),
          // pass ajax arguments
            ajaxArguments);
        }
    }
    getCurrentUser() {
        if (
            this.props &&
            this.props.user &&
            !!this.props.user.name &&
            this.props.user.name != 'anonymous'
        ) {
            var user = this.props.user.name;
        }
        else {
            var user = 'anonymous';
        }

        return user;
    }
    showDesktopUserDropdown() {
        const user = this.getCurrentUser();
        return (
            <NavDropdown
                title={<SvgUserIcon />}
                className='svg-dropdown'
                id='basic-nav-dropdown'
            >
                <li className='navbar-text'>Welcome {user}!</li>
                <MenuItem divider />
                <LinkContainer to='/session'>
                    <NavItem>Dashboard</NavItem>
                </LinkContainer>
                <MenuItem divider />
                <LinkContainer to='/logout' onClick={this.handleClick}>
                    <NavItem>Sign out</NavItem>
                </LinkContainer>
            </NavDropdown>
        )
    }
    showMobileUserDropdown() {
        const user = this.getCurrentUser();
        const title = <span>
            <span className='user-icon'><SvgUserIcon /></span>
            <span className='user-name'>{user}</span>
        </span>
        return (
            <NavDropdown
                title={title}
                className='svg-dropdown'
                id='basic-nav-dropdown'
            >
                <LinkContainer to='/session'>
                    <NavItem>Dashboard</NavItem>
                </LinkContainer>
                <MenuItem divider />
                <LinkContainer to='/logout' onClick={this.handleClick}>
                    <NavItem>Sign out</NavItem>
                </LinkContainer>
            </NavDropdown>
        )
    }
    render() {
        const userDesktopDropdown = this.showDesktopUserDropdown();
        const userMobileDropdown = this.showMobileUserDropdown();

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
                            <BreakpointRender breakpoints={breakpoints} type='viewport'>
                                {bp => (
                                    bp.isGt('small')
                                        ? userDesktopDropdown
                                        : userMobileDropdown
                                )}
                            </BreakpointRender>
                        </Nav>
                        <Nav pullRight>
                            <NavDropdown title='Session' id='basic-nav-dropdown'>
                                <LinkContainer to='/session/data-new'>
                                    <NavItem>Add new data</NavItem>
                                </LinkContainer>
                                <LinkContainer to='/session/data-append'>
                                    <NavItem>Append data</NavItem>
                                </LinkContainer>
                                <LinkContainer to='/session/model-generate'>
                                    <NavItem>Add new data</NavItem>
                                </LinkContainer>
                                <LinkContainer to='/session/model-predict'>
                                    <NavItem>Make prediction</NavItem>
                                </LinkContainer>
                                <MenuItem divider />
                                <LinkContainer to='/session/results'>
                                    <NavItem>Review Results</NavItem>
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
export default withRouter(UserMenu);
