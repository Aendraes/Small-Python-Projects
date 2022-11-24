import subprocess, sys, os

def install(package):
    try:
        import package
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

Installs = ["Json", "Keyboard", "pyperclip"]
for package in Installs:
    install(package)