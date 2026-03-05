[![CI](https://github.com/xfengyin/UHTF/actions/workflows/ci.yml/badge.svg)](https://github.com/xfengyin/UHTF/actions/workflows/ci.yml)
[![Release](https://github.com/xfengyin/UHTF/actions/workflows/release.yml/badge.svg)](https://github.com/xfengyin/UHTF/actions/workflows/release.yml)
[![CodeQL](https://github.com/xfengyin/UHTF/actions/workflows/codeql.yml/badge.svg)](https://github.com/xfengyin/UHTF/actions/workflows/codeql.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Universal Hardware Test Framework (UHTF)

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Go](https://img.shields.io/badge/go-1.19%2B-00ADD8)
![License](https://img.shields.io/badge/license-MIT-green)

**统一硬件测试框架** - 支持多种硬件平台的自动化测试框架

## 🌟 核心特性

- **多平台支持**: Arduino, Raspberry Pi, ESP32, STM32等
- **插件架构**: 轻松扩展新硬件平台
- **自动化测试**: 一键运行完整测试套件
- **报告生成**: HTML/JSON/PDF格式测试报告
- **Python + Go**: 灵活性与性能完美结合

## 🚀 快速开始

### 安装

```bash
pip install uhtf
```

### 基础用法

```python
from uhtf.core import TestFramework
from uhtf.plugins.arduino import ArduinoPlugin

# 初始化框架
framework = TestFramework()

# 添加Arduino插件
framework.add_plugin(ArduinoPlugin(port="/dev/ttyUSB0"))

# 运行测试
results = framework.run_tests()

# 生成报告
framework.generate_report(results, format="html")
```

## 📁 项目结构

```
UHTF/
├── src/python/uhtf/     # Python核心框架
│   ├── core.py          # 主框架
│   ├── plugin_manager.py # 插件管理
│   └── report_generator.py # 报告生成
├── src/go/              # Go性能模块
│   └── main.go          # 高性能串口通信
├── plugins/             # 硬件插件
│   ├── arduino/         # Arduino支持
│   └── raspberry_pi/    # 树莓派支持
├── tests/               # 测试用例
└── examples/            # 使用示例
```

## 🔌 支持的平台

| 平台 | 状态 | 功能 |
|------|------|------|
| Arduino | ✅ | 串口通信、GPIO测试、模拟读取 |
| Raspberry Pi | ✅ | GPIO控制、I2C/SPI通信 |
| ESP32 | 🔄 | 开发中 |
| STM32 | 🔄 | 计划中 |

## 💡 使用示例

### Arduino测试

```python
from uhtf.core import TestFramework
from uhtf.plugins.arduino import ArduinoPlugin

framework = TestFramework()
arduino = ArduinoPlugin(port="/dev/ttyUSB0", baudrate=115200)
framework.add_plugin(arduino)

# 运行基础测试
results = framework.run_tests(test_suite="basic")

# 运行完整测试套件
results = framework.run_tests(test_suite="comprehensive")
```

### Raspberry Pi测试

```python
from uhtf.plugins.raspberry_pi import RaspberryPiPlugin

rpi = RaspberryPiPlugin()
framework.add_plugin(rpi)
results = framework.run_tests()
```

## 📊 测试报告示例

框架自动生成详细的测试报告：

```html
测试报告 - 2026-03-05
================================
平台: Arduino
测试套件: basic

✅ 串口通信测试 - 通过 (0.5s)
✅ GPIO引脚测试 - 通过 (1.2s)  
✅ 模拟读取测试 - 通过 (0.8s)

总计: 3/3 通过
```

## 🤝 贡献

欢迎贡献代码！请查看 [贡献指南](CONTRIBUTING.md)

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE)

## 📧 联系方式

- 作者: xfengyin
- GitHub: https://github.com/xfengyin/UHTF
- Issues: https://github.com/xfengyin/UHTF/issues

---

**为硬件开发者打造的测试框架 ❤️**
