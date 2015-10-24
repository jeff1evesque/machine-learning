'''@app

This file is the acting web server.

@debug, enables debugging, and tracebacks
@host, tells the OS (guest VM) to accept connections from all public IP
    addresses.

'''

from interface import app
app.run(debug=True, host='0.0.0.0')
