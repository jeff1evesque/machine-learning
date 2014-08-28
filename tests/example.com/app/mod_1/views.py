# Import flask deps
from app import app
from flask import Blueprint, request, render_template, flash, g, session, \
        redirect, url_for


# Set routing and accepted methods
@app.route('/testpage')
def test():
    return render_template('mod_1/test.html')

