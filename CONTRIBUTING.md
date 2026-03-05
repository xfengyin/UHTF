# 贡献指南

感谢你对 UHTF 项目的关注！本文档将帮助你了解如何参与项目开发。

## 🚀 快速开始

### 1. Fork 并克隆仓库

```bash
git clone https://github.com/<your-username>/UHTF.git
cd UHTF
```

### 2. 创建虚拟环境

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# 或
venv\Scripts\activate  # Windows
```

### 3. 安装开发依赖

```bash
pip install -e ".[dev]"
```

## 📝 代码规范

### Python 代码风格

- 遵循 PEP 8 规范
- 使用 Black 格式化代码
- 使用类型注解

### 提交信息格式

```
<type>(<scope>): <subject>

<body>

<footer>
```

类型（type）:
- feat: 新功能
- fix: 修复bug
- docs: 文档更新
- test: 测试相关
- refactor: 重构
- chore: 构建/工具相关

示例:
```
feat(arduino): add I2C communication support

- Implement I2C bus scanning
- Add I2C read/write methods
- Update documentation

Closes #123
```

## 🧪 运行测试

```bash
# 运行所有测试
pytest

# 运行带覆盖率的测试
pytest --cov=src/python/uhtf --cov-report=html
```

## 📦 添加新硬件插件

1. 在 `plugins/` 目录下创建新目录
2. 继承 `HardwarePlugin` 基类
3. 实现必要的方法
4. 添加测试
5. 更新文档

示例:

```python
from uhtf.plugin_manager import HardwarePlugin

class MyHardwarePlugin(HardwarePlugin):
    def __init__(self):
        super().__init__("MyHardware", "0.1.0")
        
    def initialize(self) -> bool:
        # 初始化硬件连接
        pass
        
    def run_tests(self, test_suite=None):
        # 运行测试
        pass
        
    def cleanup(self):
        # 清理资源
        pass
```

## 📋 Pull Request 流程

1. 创建功能分支: `git checkout -b feature/my-feature`
2. 提交更改: `git commit -m "feat: add my feature"`
3. 推送分支: `git push origin feature/my-feature`
4. 创建 Pull Request
5. 等待代码审查

## 🐛 报告问题

如果你发现了 bug 或有功能建议，请创建 [Issue](https://github.com/xfengyin/UHTF/issues)。

### Issue 模板

**Bug 报告:**
- 描述问题
- 复现步骤
- 期望行为
- 实际行为
- 环境信息（Python版本、操作系统等）

**功能请求:**
- 描述功能
- 使用场景
- 可能的实现方式

## 📧 联系方式

- GitHub Issues: https://github.com/xfengyin/UHTF/issues
- GitHub Discussions: https://github.com/xfengyin/UHTF/discussions

---

再次感谢你的贡献！🙏
