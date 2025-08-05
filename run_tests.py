"""
Test runner script for PySPS.

This script configures the Python environment and runs all test cases.
"""

import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Configure environment
if __name__ == "__main__":
    os.chdir(project_root)
    
    # Run tests
    import subprocess
    
    print("🧪 Running PySPS Test Suite")
    print("=" * 50)
    
    try:
        # Run pytest with coverage
        result = subprocess.run([
            sys.executable, "-m", "pytest", 
            "tests/", 
            "-v", 
            "--tb=short",
            "--color=yes"
        ], check=True)
        
        print("\n✅ All tests passed successfully!")
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Tests failed with exit code: {e.returncode}")
        sys.exit(e.returncode)
    except FileNotFoundError:
        print("❌ pytest not found. Please install it with: pip install pytest")
        sys.exit(1)
