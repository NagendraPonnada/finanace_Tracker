import os
import sys

# Run from the project root so relative data paths work
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from finance_tracker.main import FinanceTracker

if __name__ == "__main__":
    FinanceTracker().run()
