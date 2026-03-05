"""
Unit tests for Plugin Manager
"""

import pytest
from uhtf.plugin_manager import PluginManager, HardwarePlugin


class MockPlugin(HardwarePlugin):
    """Mock plugin for testing"""
    
    def __init__(self, name="Mock", version="1.0.0"):
        super().__init__(name, version)
        self._initialized = False
        
    def initialize(self) -> bool:
        self._initialized = True
        return True
        
    def run_tests(self, test_suite=None):
        return {"platform": self.name, "tests": []}
        
    def cleanup(self):
        self._initialized = False


class TestPluginManager:
    """Test PluginManager class"""
    
    def test_initialization(self):
        """Test manager initialization"""
        manager = PluginManager()
        assert manager is not None
        assert len(manager.plugins) == 0
        
    def test_add_plugin(self):
        """Test adding a plugin"""
        manager = PluginManager()
        plugin = MockPlugin()
        
        manager.add_plugin(plugin)
        
        assert "Mock" in manager.plugins
        assert manager.plugins["Mock"] == plugin
        
    def test_remove_plugin(self):
        """Test removing a plugin"""
        manager = PluginManager()
        plugin = MockPlugin()
        manager.add_plugin(plugin)
        
        result = manager.remove_plugin("Mock")
        
        assert result is True
        assert "Mock" not in manager.plugins
        
    def test_remove_nonexistent_plugin(self):
        """Test removing a plugin that does not exist"""
        manager = PluginManager()
        
        result = manager.remove_plugin("NonExistent")
        
        assert result is False
        
    def test_get_plugin(self):
        """Test getting a plugin"""
        manager = PluginManager()
        plugin = MockPlugin()
        manager.add_plugin(plugin)
        
        result = manager.get_plugin("Mock")
        
        assert result == plugin
        
    def test_get_nonexistent_plugin(self):
        """Test getting a plugin that does not exist"""
        manager = PluginManager()
        
        result = manager.get_plugin("NonExistent")
        
        assert result is None
        
    def test_list_plugins(self):
        """Test listing plugins"""
        manager = PluginManager()
        manager.add_plugin(MockPlugin("Plugin1"))
        manager.add_plugin(MockPlugin("Plugin2"))
        
        result = manager.list_plugins()
        
        assert len(result) == 2
        assert "Plugin1" in result
        assert "Plugin2" in result
        
    def test_clear(self):
        """Test clearing all plugins"""
        manager = PluginManager()
        manager.add_plugin(MockPlugin())
        manager.add_plugin(MockPlugin("Another"))
        
        manager.clear()
        
        assert len(manager.plugins) == 0


class TestHardwarePlugin:
    """Test HardwarePlugin base class"""
    
    def test_initialization(self):
        """Test plugin initialization"""
        plugin = MockPlugin("TestPlugin", "2.0.0")
        
        assert plugin.name == "TestPlugin"
        assert plugin.version == "2.0.0"
        assert plugin.is_initialized() is False
        
    def test_is_initialized(self):
        """Test initialization status"""
        plugin = MockPlugin()
        
        assert plugin.is_initialized() is False
        
        plugin.initialize()
        
        assert plugin.is_initialized() is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
