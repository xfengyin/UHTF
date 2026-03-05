"""
Command Line Interface for UHTF
"""

import click
import logging
from pathlib import Path
from typing import Optional

from .core import TestFramework
from .config import load_config


@click.group()
@click.option('--config', '-c', type=click.Path(), help='Configuration file path')
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose output')
@click.pass_context
def cli(ctx: click.Context, config: Optional[str], verbose: bool):
    """Universal Hardware Test Framework - 统一硬件测试框架"""
    
    # Setup logging
    log_level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Load configuration
    ctx.ensure_object(dict)
    ctx.obj['config'] = load_config(config)
    

@cli.command()
@click.option('--platform', '-p', help='Platform to test')
@click.option('--suite', '-s', default='basic', help='Test suite name')
@click.option('--output', '-o', type=click.Path(), help='Output directory')
@click.pass_context
def run(ctx: click.Context, platform: Optional[str], suite: str, output: Optional[str]):
    """Run hardware tests"""
    
    config = ctx.obj['config']
    framework = TestFramework()
    
    click.echo("🚀 Starting tests...")
    
    # Import and add plugins
    try:
        from uhtf.plugins.arduino import ArduinoPlugin
        framework.add_plugin(ArduinoPlugin())
    except ImportError:
        pass
        
    try:
        from uhtf.plugins.raspberry_pi import RaspberryPiPlugin
        framework.add_plugin(RaspberryPiPlugin())
    except ImportError:
        pass
    
    # Run tests
    results = framework.run_tests(platform=platform, test_suite=suite)
    
    # Generate report
    output_dir = output or config.output_dir
    report_format = config.report_format
    
    report_path = framework.generate_report(format=report_format)
    
    # Print summary
    summary = results.get('summary', {})
    click.echo(f"\n✅ Passed: {summary.get('passed', 0)}")
    click.echo(f"❌ Failed: {summary.get('failed', 0)}")
    click.echo(f"📄 Report: {report_path}")


@cli.command()
@click.pass_context
def list_plugins(ctx: click.Context):
    """List available plugins"""
    
    click.echo("📦 Available Plugins:")
    click.echo("  - Arduino")
    click.echo("  - Raspberry Pi")
    click.echo("  - ESP32 (coming soon)")
    click.echo("  - STM32 (coming soon)")


@cli.command()
@click.pass_context
def version(ctx: click.Context):
    """Show version"""
    from . import __version__
    click.echo(f"UHTF version {__version__}")


def main():
    """Entry point"""
    cli(obj={})


if __name__ == '__main__':
    main()
