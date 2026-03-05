"""
UHTF Example: Basic Usage
"""

from uhtf.core import TestFramework
from uhtf.plugins.arduino import ArduinoPlugin
from uhtf.plugins.raspberry_pi import RaspberryPiPlugin


def main():
    # 创建测试框架
    framework = TestFramework()
    
    # 添加Arduino插件（模拟模式，无需真实硬件）
    arduino = ArduinoPlugin(port="/dev/ttyUSB0")
    framework.add_plugin(arduino)
    
    # 添加Raspberry Pi插件（模拟模式）
    rpi = RaspberryPiPlugin()
    framework.add_plugin(rpi)
    
    # 运行测试
    print("开始运行测试...")
    results = framework.run_tests()
    
    # 生成HTML报告
    print("\n生成测试报告...")
    report_path = framework.generate_report(format="html")
    print(f"报告已生成: {report_path}")
    
    # 打印结果摘要
    print(f"\n测试完成！")
    print(f"通过: {results['summary']['passed']}")
    print(f"失败: {results['summary']['failed']}")


if __name__ == "__main__":
    main()
