"""
pytest configuration
"""

import pytest
import sys
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent.parent / "src" / "python"
sys.path.insert(0, str(src_path))


@pytest.fixture
def mock_plugin():
    """Mock plugin fixture"""
    from uhtf.plugin_manager import HardwarePlugin
    
    class MockPlugin(HardwarePlugin):
        def __init__(self):
            super().__init__("Mock", "1.0.0")
            
        def initialize(self):
            return True
            
        def run_tests(self, test_suite=None):
            return {"platform": "Mock", "tests": []}
            
        def cleanup(self):
            pass
            
    return MockPlugin()


@pytest.fixture
def sample_results():
    """Sample test results"""
    return {
        "summary": {
            "total_tests": 3,
            "passed": 2,
            "failed": 1,
            "errors": 0
        },
        "platforms": {
            "Arduino": {
                "tests": [
                    {"name": "Serial Test", "status": "passed", "duration": 0.5},
                    {"name": "GPIO Test", "status": "passed", "duration": 1.0},
                    {"name": "I2C Test", "status": "failed", "duration": 0.3, "error": "Timeout"}
                ]
            }
        },
        "duration": 2.5
    }
