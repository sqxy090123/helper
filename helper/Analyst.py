import ast
import inspect

class __raiseup(Exception):
    def __init__(self, word):
        raise ImportError(word)


def _e(*args):
    ast_tree, 


def analyst(module_name:str):
    try:
        module = __import__(module_name)
    except ImportError as E:
        __raiseup(str(E))
        return
    
    source_code = inspect.getsource(module)
    ast_tree = ast.parse(source_code)
    # 打印函数定义
    for node in ast_tree.body:
        if isinstance(node, ast.FunctionDef):
            print(f"Function: {node.name}")
    # 打印类定义
    for node in ast_tree.body:
        if isinstance(node, ast.ClassDef):
            print(f"Class: {node.name}")
            