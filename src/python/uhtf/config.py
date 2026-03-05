"""
Configuration management for UHTF
"""

import os
import json
import yaml
from pathlib import Path
from typing import Dict, Any, Optional
from dataclasses import dataclass, field


@dataclass
class Config:
    """UHTF Configuration"""
    
    # Output settings
    output_dir: str = "reports"
    report_format: str = "html"
    
    # Logging settings
    log_level: str = "INFO"
    log_file: Optional[str] = None
    
    # Test settings
    default_timeout: float = 30.0
    retry_count: int = 3
    
    # Plugin settings
    plugin_dirs: list = field(default_factory=lambda: ["plugins"])
    
    @classmethod
    def from_file(cls, config_path: str) -> "Config":
        """Load configuration from file"""
        path = Path(config_path)
        
        if not path.exists():
            return cls()
            
        with open(path, 'r') as f:
            if path.suffix in ['.yaml', '.yml']:
                data = yaml.safe_load(f)
            else:
                data = json.load(f)
                
        return cls(**data)
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "output_dir": self.output_dir,
            "report_format": self.report_format,
            "log_level": self.log_level,
            "log_file": self.log_file,
            "default_timeout": self.default_timeout,
            "retry_count": self.retry_count,
            "plugin_dirs": self.plugin_dirs,
        }


def get_default_config_path() -> Path:
    """Get default configuration file path"""
    return Path.home() / ".uhtf" / "config.yaml"


def load_config(config_path: Optional[str] = None) -> Config:
    """Load configuration"""
    if config_path:
        return Config.from_file(config_path)
        
    default_path = get_default_config_path()
    if default_path.exists():
        return Config.from_file(str(default_path))
        
    return Config()
