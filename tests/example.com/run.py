# WSGI Server for Development
# Use this during development vs. apache. Can view via [url]:8001
# Run using virtualenv. 'env/bin/python run.py'
from app import app

app.run(host='0.0.0.0', port=8001, debug=True)

