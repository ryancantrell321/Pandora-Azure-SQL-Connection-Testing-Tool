import subprocess
import sys


def check_dependencies():
    try:
        import required_module
    except ImportError:
        return False
    return True


def install_dependencies(req_path):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", req_path])


def dependencies(req_path):
    if not check_dependencies():
        print("Required dependencies not found. Installing...")
        install_dependencies(req_path)
        print("Dependencies installed successfully.")

