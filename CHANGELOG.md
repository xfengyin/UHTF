# 更新日志

所有重要的更改都将记录在此文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
并且本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [Unreleased]

### 计划添加
- ESP32 硬件插件
- STM32 硬件插件
- Web Dashboard
- 远程测试集群支持

## [0.1.0] - 2026-03-05

### 新增
- 核心测试框架 (TestFramework)
- 插件管理系统 (PluginManager, HardwarePlugin)
- 报告生成器 (HTML/JSON/Text)
- Arduino 硬件插件
  - 串口通信测试
  - GPIO 引脚测试
  - 模拟读取测试
  - I2C/SPI 通信测试
  - PWM 输出测试
- Raspberry Pi 硬件插件
  - GPIO 测试
  - I2C 总线测试
  - PWM 测试
- 单元测试框架
- 使用示例
- 完整文档

### 技术栈
- Python 3.8+
- Go 1.19+ (高性能模块)
- pyserial (串口通信)
- RPi.GPIO (树莓派GPIO)

---

## 版本说明

- **主版本号**: 不兼容的 API 更改
- **次版本号**: 向后兼容的功能新增
- **修订号**: 向后兼容的问题修复
