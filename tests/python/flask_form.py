## flask_form.py
#  This file simply echos the post values from 'form.html'

from flask import Flask

app = Flask(__name__)
# handles 'get', and 'post'
@app.route('/machine-learning/tests/python/flask_form.py', methods=['GET', 'POST'])
def parse_request():
  temp = request.form['svm_session']
  print temp
  return temp
