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
if len(sys.argv) > 1 && sys.argv[1] == 'test':
    pytest.main(['-x', 'test'])
# run application
else:
    app = create_app()
    app.run(host='0.0.0.0')
