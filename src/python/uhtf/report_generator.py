"""
Universal Hardware Test Framework - Report Generator
"""

import json
import os
from datetime import datetime
from typing import Dict, Any, Optional
from pathlib import Path


class ReportGenerator:
    """
    测试报告生成器
    
    支持HTML、JSON和文本格式的报告
    """
    
    def __init__(self, output_dir: str = "reports"):
        """
        初始化报告生成器
        
        Args:
            output_dir: 报告输出目录
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
    def generate(self, 
                 results: Dict[str, Any], 
                 format: str = "html",
                 output_file: Optional[str] = None) -> str:
        """
        生成测试报告
        
        Args:
            results: 测试结果
            format: 报告格式 (html/json/text)
            output_file: 输出文件路径（可选）
            
        Returns:
            报告文件路径
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if format == "html":
            return self._generate_html(results, timestamp, output_file)
        elif format == "json":
            return self._generate_json(results, timestamp, output_file)
        elif format == "text":
            return self._generate_text(results, timestamp, output_file)
        else:
            raise ValueError(f"不支持的格式: {format}")
            
    def _generate_html(self, 
                       results: Dict, 
                       timestamp: str,
                       output_file: Optional[str]) -> str:
        """生成HTML报告"""
        if output_file is None:
            output_file = str(self.output_dir / f"test_report_{timestamp}.html")
            
        summary = results.get("summary", {})
        
        html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UHTF 测试报告</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; 
               margin: 0; padding: 20px; background: #f5f5f5; }}
        .container {{ max-width: 1200px; margin: 0 auto; background: white; 
                     padding: 30px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        h1 {{ color: #333; border-bottom: 3px solid #4CAF50; padding-bottom: 10px; }}
        .stats {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin: 30px 0; }}
        .stat-box {{ padding: 20px; border-radius: 8px; text-align: center; }}
        .stat-box.total {{ background: #e3f2fd; }}
        .stat-box.passed {{ background: #e8f5e9; }}
        .stat-box.failed {{ background: #ffebee; }}
        .stat-box.errors {{ background: #fff3e0; }}
        .stat-number {{ font-size: 36px; font-weight: bold; }}
        .stat-label {{ color: #666; margin-top: 5px; }}
        .platform {{ margin: 30px 0; padding: 20px; border: 1px solid #ddd; border-radius: 8px; }}
        .platform h2 {{ color: #1976d2; margin-top: 0; }}
        .test {{ padding: 15px; margin: 10px 0; border-radius: 4px; border-left: 4px solid; }}
        .test.passed {{ background: #f1f8e9; border-color: #4CAF50; }}
        .test.failed {{ background: #ffebee; border-color: #f44336; }}
        .test-name {{ font-weight: bold; font-size: 16px; }}
        .test-duration {{ color: #666; font-size: 14px; }}
        .duration {{ color: #666; font-size: 18px; text-align: center; margin: 20px 0; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🧪 UHTF 测试报告</h1>
        <p>生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        
        <div class="stats">
            <div class="stat-box total">
                <div class="stat-number">{summary.get('total_tests', 0)}</div>
                <div class="stat-label">总测试数</div>
            </div>
            <div class="stat-box passed">
                <div class="stat-number">{summary.get('passed', 0)}</div>
                <div class="stat-label">通过 ✅</div>
            </div>
            <div class="stat-box failed">
                <div class="stat-number">{summary.get('failed', 0)}</div>
                <div class="stat-label">失败 ❌</div>
            </div>
            <div class="stat-box errors">
                <div class="stat-number">{summary.get('errors', 0)}</div>
                <div class="stat-label">错误 ⚠️</div>
            </div>
        </div>
        
        <div class="duration">
            ⏱️ 总耗时: {results.get('duration', 0):.2f} 秒
        </div>
"""
        
        # 添加每个平台的测试结果
        for platform_name, platform_data in results.get("platforms", {}).items():
            html += f"""
        <div class="platform">
            <h2>📦 平台: {platform_name}</h2>
"""
            
            if isinstance(platform_data, dict) and "tests" in platform_data:
                for test in platform_data.get("tests", []):
                    status = test.get("status", "unknown")
                    name = test.get("name", "Unknown")
                    duration = test.get("duration", 0)
                    error = test.get("error", "")
                    
                    html += f"""
            <div class="test {status}">
                <div class="test-name">{name}</div>
                <div class="test-duration">耗时: {duration:.2f}s</div>
                {f'<div class="test-error">错误: {error}</div>' if error else ''}
            </div>
"""
            else:
                html += f"""
            <p>无测试数据</p>
"""
                
            html += """
        </div>
"""
            
        html += """
    </div>
</body>
</html>
"""
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
            
        return output_file
        
    def _generate_json(self, 
                       results: Dict, 
                       timestamp: str,
                       output_file: Optional[str]) -> str:
        """生成JSON报告"""
        if output_file is None:
            output_file = str(self.output_dir / f"test_report_{timestamp}.json")
            
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False, default=str)
            
        return output_file
        
    def _generate_text(self, 
                       results: Dict, 
                       timestamp: str,
                       output_file: Optional[str]) -> str:
        """生成文本报告"""
        if output_file is None:
            output_file = str(self.output_dir / f"test_report_{timestamp}.txt")
            
        lines = []
        lines.append("=" * 60)
        lines.append("UHTF 测试报告")
        lines.append("=" * 60)
        lines.append(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("")
        
        summary = results.get("summary", {})
        lines.append("测试摘要:")
        lines.append(f"  总测试数: {summary.get('total_tests', 0)}")
        lines.append(f"  通过: {summary.get('passed', 0)}")
        lines.append(f"  失败: {summary.get('failed', 0)}")
        lines.append(f"  错误: {summary.get('errors', 0)}")
        lines.append(f"  耗时: {results.get('duration', 0):.2f}秒")
        lines.append("")
        
        for platform_name, platform_data in results.get("platforms", {}).items():
            lines.append(f"\n平台: {platform_name}")
            lines.append("-" * 40)
            
            if isinstance(platform_data, dict) and "tests" in platform_data:
                for test in platform_data.get("tests", []):
                    status = "✅" if test.get("status") == "passed" else "❌"
                    lines.append(f"  {status} {test.get('name', 'Unknown')} ({test.get('duration', 0):.2f}s)")
                    if test.get("error"):
                        lines.append(f"     错误: {test.get('error')}")
                        
        lines.append("\n" + "=" * 60)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
            
        return output_file
