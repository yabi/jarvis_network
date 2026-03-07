import logging
import subprocess
import sys


def ensure_package(pkg_name):
    try:
        __import__(pkg_name)
    except ImportError:
        print(f"Package '{pkg_name}' missing. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg_name])


def setup_logging(config):
    log_level = "INFO"
    log_file = None

    try:
        log_level = config.get('system', {}).get('log_level', 'INFO').upper()
        log_file = config.get('system', {}).get('log_file', 'jarvis.log')
    except Exception:
        print("Config missing, using default log settings")

    handlers = [logging.StreamHandler(sys.stdout)]
    if log_file:
        handlers.append(logging.FileHandler(log_file))

    logging.basicConfig(
        level=getattr(logging, log_level, logging.INFO),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=handlers
    )
