import subprocess, sys, os

def install(package):
    try:
        import package
    except:
        print(f"Could not install package {package}")

Installs = ["json", "keyboard", "pyperclip"]
for package in Installs:
    install(package)