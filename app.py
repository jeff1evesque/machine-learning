'''@app

This file is the acting web server.

@host, tells the OS (guest VM) to accept connections from all public IP
    addresses.

Note: both the handler, and logger has levels. If the level of the logger is
      higher than that of the handler, no messages will be handled by the
      corresponding handler.

'''

import sys
import pytest
from factory import create_app

# run unit test
if len(sys.argv) > 1:
    if sys.argv[1] == 'test':
        pytest.main(['--cov', '.', '--cov-report', 'xml:coverage.xml', 'test/live_server'])
    elif sys.argv[1] == 'run':
        args = {
            'prefix': 'test',
            'settings': ''
        }
        app = create_app(args)
        app.run(host='0.0.0.0')
# run application
else:
    app = create_app()
    app.run(host='0.0.0.0')
