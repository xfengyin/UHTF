"""
Universal Hardware Test Framework - Core Module
"""

import logging
import time
from typing import Dict, List, Any, Optional
from .plugin_manager import PluginManager, HardwarePlugin
from .report_generator import ReportGenerator


class TestFramework:
    """
    主测试框架类
    
    负责协调插件管理、测试执行和报告生成
    """
    
    def __init__(self, config: Optional[Dict] = None):
        """
        初始化测试框架
        
        Args:
            config: 配置字典（可选）
        """
        self.logger = logging.getLogger(__name__)
        self.config = config or {}
        self.plugin_manager = PluginManager()
        self.report_generator = ReportGenerator()
        self.test_history = []
        
    def add_plugin(self, plugin: HardwarePlugin) -> None:
        """
        添加硬件插件
        
        Args:
            plugin: 硬件插件实例
        """
        self.plugin_manager.add_plugin(plugin)
        self.logger.info(f"已添加插件: {plugin.name} v{plugin.version}")
        
    def remove_plugin(self, plugin_name: str) -> bool:
        """
        移除插件
        
        Args:
            plugin_name: 插件名称
            
        Returns:
            是否成功移除
        """
        return self.plugin_manager.remove_plugin(plugin_name)
        
    def list_plugins(self) -> List[str]:
        """
        列出所有已注册的插件
        
        Returns:
            插件名称列表
        """
        return self.plugin_manager.list_plugins()
        
    def run_tests(self, 
                  platform: Optional[str] = None,
                  test_suite: Optional[str] = None) -> Dict[str, Any]:
        """
        运行测试
        
        Args:
            platform: 指定平台名称（可选，默认测试所有平台）
            test_suite: 测试套件名称（可选）
            
        Returns:
            测试结果字典
        """
        self.logger.info("=" * 50)
        self.logger.info("开始执行测试")
        self.logger.info("=" * 50)
        
        start_time = time.time()
        results = {
            "start_time": start_time,
            "platforms": {},
            "summary": {
                "total_tests": 0,
                "passed": 0,
                "failed": 0,
                "errors": 0
            }
        }
        
        # 获取要测试的插件
        if platform:
            plugins_to_test = {platform: self.plugin_manager.get_plugin(platform)}
        else:
            plugins_to_test = self.plugin_manager.plugins
            
        # 执行每个插件的测试
        for plugin_name, plugin in plugins_to_test.items():
            if plugin is None:
                self.logger.warning(f"插件 {plugin_name} 不存在")
                continue
                
            self.logger.info(f"\n>>> 测试平台: {plugin_name}")
            
            try:
                # 初始化插件
                if not plugin.initialize():
                    results["platforms"][plugin_name] = {
                        "status": "error",
                        "message": "初始化失败"
                    }
                    results["summary"]["errors"] += 1
                    continue
                    
                # 运行测试
                plugin_results = plugin.run_tests(test_suite)
                
                # 统计结果
                test_count = len(plugin_results.get("tests", []))
                passed = sum(1 for t in plugin_results.get("tests", []) 
                           if t.get("status") == "passed")
                failed = test_count - passed
                
                results["platforms"][plugin_name] = plugin_results
                results["summary"]["total_tests"] += test_count
                results["summary"]["passed"] += passed
                results["summary"]["failed"] += failed
                
                # 清理资源
                plugin.cleanup()
                
                self.logger.info(f"完成: {passed}/{test_count} 通过")
                
            except Exception as e:
                self.logger.error(f"测试异常: {e}")
                results["platforms"][plugin_name] = {
                    "status": "error",
                    "error": str(e)
                }
                results["summary"]["errors"] += 1
                
        # 计算总耗时
        end_time = time.time()
        results["end_time"] = end_time
        results["duration"] = end_time - start_time
        
        # 保存历史
        self.test_history.append(results)
        
        # 打印摘要
        self._print_summary(results)
        
        return results
        
    def generate_report(self, 
                       results: Optional[Dict] = None,
                       format: str = "html",
                       output_file: Optional[str] = None) -> str:
        """
        生成测试报告
        
        Args:
            results: 测试结果（可选，默认使用最近一次结果）
            format: 报告格式 (html/json/text)
            output_file: 输出文件路径（可选）
            
        Returns:
            报告文件路径
        """
        if results is None:
            if not self.test_history:
                self.logger.warning("没有测试结果")
                return ""
            results = self.test_history[-1]
            
        return self.report_generator.generate(results, format, output_file)
        
    def _print_summary(self, results: Dict) -> None:
        """打印测试摘要"""
        summary = results["summary"]
        duration = results["duration"]
        
        self.logger.info("\n" + "=" * 50)
        self.logger.info("测试摘要")
        self.logger.info("=" * 50)
        self.logger.info(f"总测试数: {summary['total_tests']}")
        self.logger.info(f"通过: {summary['passed']} ✅")
        self.logger.info(f"失败: {summary['failed']} ❌")
        self.logger.info(f"错误: {summary['errors']} ⚠️")
        self.logger.info(f"耗时: {duration:.2f}秒")
        self.logger.info("=" * 50)
