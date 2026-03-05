# UHTF Makefile

.PHONY: install test lint format clean build publish

# 安装开发依赖
install:
	pip install -e ".[dev]"

# 运行测试
test:
	pytest tests/ -v --cov=src/python/uhtf --cov-report=html

# 代码检查
lint:
	flake8 src/python/uhtf tests/
	mypy src/python/uhtf

# 代码格式化
format:
	black src/python/uhtf tests/

# 清理
clean:
	rm -rf build/ dist/ *.egg-info
	rm -rf .pytest_cache .coverage htmlcov/
	rm -rf reports/

# 构建
build:
	python -m build

# 发布到 PyPI
publish:
	python -m twine upload dist/*

# 运行示例
example:
	python examples/basic_usage.py

# 帮助
help:
	@echo "Available commands:"
	@echo "  make install   - Install development dependencies"
	@echo "  make test      - Run tests with coverage"
	@echo "  make lint      - Run linting"
	@echo "  make format    - Format code"
	@echo "  make clean     - Clean build artifacts"
	@echo "  make build     - Build package"
	@echo "  make publish   - Publish to PyPI"
	@echo "  make example   - Run example script"
