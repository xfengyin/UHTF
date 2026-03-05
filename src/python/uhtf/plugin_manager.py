"""
Universal Hardware Test Framework - Plugin Manager
"""

import logging
from typing import Dict, Optional, Any
from abc import ABC, abstractmethod


class HardwarePlugin(ABC):
    """
    硬件插件基类
    
    所有硬件插件必须继承此类并实现抽象方法
    """
    
    def __init__(self, name: str, version: str):
        """
        初始化插件
        
        Args:
            name: 插件名称
            version: 插件版本
        """
        self.name = name
        self.version = version
        self.logger = logging.getLogger(f"uhtf.plugins.{name}")
        self._initialized = False
        
    @abstractmethod
    def initialize(self) -> bool:
        """
        初始化硬件连接
        
        Returns:
            是否成功初始化
        """
        pass
        
    @abstractmethod
    def run_tests(self, test_suite: Optional[str] = None) -> Dict[str, Any]:
        """
        运行测试
        
        Args:
            test_suite: 测试套件名称（可选）
            
        Returns:
            测试结果字典，格式：
            {
                "platform": str,
                "tests": [
                    {
                        "name": str,
                        "status": "passed" | "failed",
                        "duration": float,
                        "error": Optional[str]
                    }
                ]
            }
        """
        pass
        
    @abstractmethod
    def cleanup(self) -> None:
        """
        清理资源
        
        在测试完成后调用，用于释放硬件连接等资源
        """
        pass
        
    def is_initialized(self) -> bool:
        """检查是否已初始化"""
        return self._initialized


class PluginManager:
    """
    插件管理器
    
    负责管理所有注册的硬件插件
    """
    
    def __init__(self):
        """初始化插件管理器"""
        self.plugins: Dict[str, HardwarePlugin] = {}
        self.logger = logging.getLogger(__name__)
        
    def add_plugin(self, plugin: HardwarePlugin) -> None:
        """
        添加插件
        
        Args:
            plugin: 硬件插件实例
        """
        if plugin.name in self.plugins:
            self.logger.warning(f"插件 {plugin.name} 已存在，将被覆盖")
        self.plugins[plugin.name] = plugin
        self.logger.info(f"已注册插件: {plugin.name} v{plugin.version}")
        
    def remove_plugin(self, plugin_name: str) -> bool:
        """
        移除插件
        
        Args:
            plugin_name: 插件名称
            
        Returns:
            是否成功移除
        """
        if plugin_name in self.plugins:
            del self.plugins[plugin_name]
            self.logger.info(f"已移除插件: {plugin_name}")
            return True
        self.logger.warning(f"插件 {plugin_name} 不存在")
        return False
        
    def get_plugin(self, plugin_name: str) -> Optional[HardwarePlugin]:
        """
        获取插件
        
        Args:
            plugin_name: 插件名称
            
        Returns:
            插件实例，如果不存在返回None
        """
        return self.plugins.get(plugin_name)
        
    def list_plugins(self) -> list:
        """
        列出所有插件名称
        
        Returns:
            插件名称列表
        """
        return list(self.plugins.keys())
        
    def clear(self) -> None:
        """清除所有插件"""
        self.plugins.clear()
        self.logger.info("已清除所有插件")
