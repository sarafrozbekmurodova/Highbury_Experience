import sys
import os

# Add the src folder to Python path so it can find 'app'
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import App

if __name__ == "__main__":
    app = App()
    app.run()
