"""
WSGI application entry point for production deployment
Use with Gunicorn or other WSGI servers

Example:
    gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app
"""

import os
import logging
from app import app
from config import get_config

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Load configuration
config = get_config()
app.config.from_object(config)

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
