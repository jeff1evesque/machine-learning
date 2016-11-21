'''

This file initializes the LoginManager

@session_protection, when session protection is active, each request, it
    generates an identifier for the user’s computer (basically, a secure hash
    of the IP address and user agent). If the session does not have an
    associated identifier, the one generated will be stored. If it has an
    identifier, and it matches the one generated, then the request is OK.

    If the identifiers do not match in basic mode, or when the session is
    permanent, then the session will simply be marked as non-fresh, and
    anything requiring a fresh login will force the user to re-authenticate.
    (Of course, you must be already using fresh logins where appropriate for
    this to have an effect.)

    If the identifiers do not match in strong mode for a non-permanent
    session, then the entire session (as well as the remember token if it
    exists) is deleted.

  - https://flask-login.readthedocs.io/en/0.4.0/#session-protection

@login_view, by default, when a user attempts to access a login_required view
    without being logged in, Flask-Login will flash a message and redirect
    them to the log in view. (If the login view is not set, it will abort
    with a 401 error.)

  - https://flask-login.readthedocs.io/en/0.4.0/#customizing-the-login-process

'''

from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = '/login'
