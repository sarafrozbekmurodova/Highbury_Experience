"""
Main entry point for the application.

Responsibilities:
- Configure Python path to locate project modules
- Initialize and start the application

This file acts as the bootstrap for the system.
"""

import sys
import os

# Add the src folder to Python path so it can find 'app'
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import App


if __name__ == "__main__":
    """
    Start the application.
    """
    app = App()
    app.run()