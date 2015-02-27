## @views.py
#   This file loads corresponding logic for defined route addresses.
#       allows the presentation of (asynchronous) content.
import app

# Define Route: assign corresponding template, or logic to given path
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/load-data/', methods=['POST', 'GET'])
def load_data():
  if request.method == 'POST':
    if request.files: files = request.files
    settings = request.form
