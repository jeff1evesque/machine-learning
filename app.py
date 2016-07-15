'''@app

This file is the acting web server.

@debug, enables debugging, and tracebacks
@host, tells the OS (guest VM) to accept connections from all public IP
    addresses.

Note: both the handler, and logger has levels. If the level of the logger is
      higher than that of the handler, no messages will be handled by the
      corresponding handler.

'''

import sys
from manager import Manager
from factory import create_app

# app factory
app = create_app()

# implement app factory
if len(sys.argv) >= 2:
    # unit test
    if sys.argv[1] == 'test':
        manager = Manager(app)
        manager.pytest()
    # other case
    else:
        app.run(host='0.0.0.0')
else:
    app.run(host='0.0.0.0')
