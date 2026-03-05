"""
Universal Hardware Test Framework (UHTF)

统一硬件测试框架 - 支持多种硬件平台的自动化测试
"""

__version__ = "0.1.0"
__author__ = "xfengyin"
__email__ = "xfengyin@users.noreply.github.com"

from .core import TestFramework
from .plugin_manager import PluginManager, HardwarePlugin
from .report_generator import ReportGenerator

__all__ = [
    "TestFramework",
    "PluginManager", 
    "HardwarePlugin",
    "ReportGenerator",
]
