## @app.py
#   This file loads corresponding logic, and html template file(s), which
#       allows the presentation of (asynchronous) content.
from flask import Flask, render_template

# Initialize: create flask instance
app = Flask(__name__)

# Define Route: assign corresponding template, or logic to given path
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/load-data/', methods=['POST', 'GET'])
def load_data():
  if request.method == 'POST':
    if request.files: files = request.files
    settings = request.form

# Execute: run application directly, instead of import
if __name__ == '__main__':
  app.run(
  debug=True
)
