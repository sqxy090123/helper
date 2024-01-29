import os

def install(package:str):
    os.system(f"pip install {package}")

def uninstall(package:str):
    os.system(f"pip uninstall {package}")

def all(command:str):
    os.system(f"pip {command}")

