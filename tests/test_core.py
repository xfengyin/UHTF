"""
Unit tests for UHTF Core
"""

import pytest
from uhtf.core import TestFramework
from uhtf.plugin_manager import HardwarePlugin


class MockPlugin(HardwarePlugin):
    """Mock plugin for testing"""
    
    def __init__(self):
        super().__init__("Mock", "1.0.0")
        
    def initialize(self) -> bool:
        return True
        
    def run_tests(self, test_suite=None):
        return {
            "platform": "Mock",
            "tests": [
                {"name": "Test1", "status": "passed", "duration": 0.1},
                {"name": "Test2", "status": "passed", "duration": 0.2}
            ]
        }
        
    def cleanup(self):
        pass


class TestTestFramework:
    """Test the TestFramework class"""
    
    def test_initialization(self):
        """Test framework initialization"""
        framework = TestFramework()
        assert framework is not None
        assert framework.plugin_manager is not None
        
    def test_add_plugin(self):
        """Test adding a plugin"""
        framework = TestFramework()
        plugin = MockPlugin()
        
        framework.add_plugin(plugin)
        
        assert "Mock" in framework.list_plugins()
        
    def test_remove_plugin(self):
        """Test removing a plugin"""
        framework = TestFramework()
        plugin = MockPlugin()
        
        framework.add_plugin(plugin)
        result = framework.remove_plugin("Mock")
        
        assert result is True
        assert "Mock" not in framework.list_plugins()
        
    def test_run_tests(self):
        """Test running tests"""
        framework = TestFramework()
        plugin = MockPlugin()
        framework.add_plugin(plugin)
        
        results = framework.run_tests()
        
        assert "platforms" in results
        assert "Mock" in results["platforms"]
        assert results["summary"]["passed"] == 2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
