"""
Unit tests for Report Generator
"""

import pytest
import tempfile
import os
from pathlib import Path

from uhtf.report_generator import ReportGenerator


class TestReportGenerator:
    """Test ReportGenerator class"""
    
    def test_initialization(self):
        """Test generator initialization"""
        with tempfile.TemporaryDirectory() as tmpdir:
            generator = ReportGenerator(output_dir=tmpdir)
            assert generator is not None
            assert generator.output_dir == Path(tmpdir)
            
    def test_generate_json_report(self):
        """Test JSON report generation"""
        with tempfile.TemporaryDirectory() as tmpdir:
            generator = ReportGenerator(output_dir=tmpdir)
            
            results = {
                "summary": {"total_tests": 2, "passed": 2, "failed": 0, "errors": 0},
                "platforms": {"Mock": {"tests": [{"name": "Test1", "status": "passed"}]}},
                "duration": 1.5
            }
            
            report_path = generator.generate(results, format="json")
            
            assert os.path.exists(report_path)
            assert report_path.endswith(".json")
            
    def test_generate_html_report(self):
        """Test HTML report generation"""
        with tempfile.TemporaryDirectory() as tmpdir:
            generator = ReportGenerator(output_dir=tmpdir)
            
            results = {
                "summary": {"total_tests": 2, "passed": 2, "failed": 0, "errors": 0},
                "platforms": {"Mock": {"tests": [{"name": "Test1", "status": "passed"}]}},
                "duration": 1.5
            }
            
            report_path = generator.generate(results, format="html")
            
            assert os.path.exists(report_path)
            assert report_path.endswith(".html")
            
            # Check HTML content
            with open(report_path, 'r') as f:
                content = f.read()
                assert "UHTF" in content
                assert "测试报告" in content
                
    def test_generate_text_report(self):
        """Test text report generation"""
        with tempfile.TemporaryDirectory() as tmpdir:
            generator = ReportGenerator(output_dir=tmpdir)
            
            results = {
                "summary": {"total_tests": 2, "passed": 2, "failed": 0, "errors": 0},
                "platforms": {"Mock": {"tests": [{"name": "Test1", "status": "passed"}]}},
                "duration": 1.5
            }
            
            report_path = generator.generate(results, format="text")
            
            assert os.path.exists(report_path)
            assert report_path.endswith(".txt")
            
    def test_invalid_format(self):
        """Test invalid format raises error"""
        with tempfile.TemporaryDirectory() as tmpdir:
            generator = ReportGenerator(output_dir=tmpdir)
            
            with pytest.raises(ValueError):
                generator.generate({}, format="invalid")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
