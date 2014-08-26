## flask_form.py
#  This file simply echos the post values from 'form.html'

#!/usr/bin/python

from flask import Flask, request, redirect, url_for
app = Flask(__name__)

# debug options
app.debug = True
app.config['TRAP_HTTP_EXCEPTIONS'] = True

# handles 'get', and 'post'
@app.route('/machine-learning/tests/python/flask_form.py', methods=['GET', 'POST'])
def parse_request():
  if request.method == 'POST':
    temp = request.form['svm_session']
    return temp
  else:
    return redirect(url_for('/machine-learning/tests/python/form.html'));

if __name__ == '__main__':
    app.run()
