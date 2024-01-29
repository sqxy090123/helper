from helper import Analyst, Color, Translate, Python_pip, Code

import hashlib

__author__ = "NameError_Studio && sqxy090123"
__project_url__ = "https://github.com/sqxy090123/helper"
__issues__ = "https://github.com/sqxy090123/helper/issues"

__all__ = ["sha256", "sha1", "Analyst", "Color", "Translate", "Python_pip", "Code"]

class sha256:
    @staticmethod
    def code(string:str):
        return hashlib.sha256(string.encode()).hexdigest()
    
    @staticmethod
    def decode(sha256_string, mode=False):
        """
        :test_string :暴力穷举法
        :return :返回破解完成的字符串
        """
        decode_hash = bytes.fromhex(sha256_string)
        i = 0
        """:i :暴力穷举法 """
        while True:  # 可根据需求调整循环范围
            i += 1
            test_string = hex(i)[2:]
            hashed_test_string = hashlib.sha256(test_string.encode()).digest()
            if hashed_test_string == decode_hash:
                return test_string
            if mode:
                if i % 10000000 == 0:
                    print(f"total: {i} times.")

class sha1:
    @staticmethod
    def code(string:str):
        return hashlib.sha1(string.encode()).hexdigest()
    
    @staticmethod
    def decode(sha1_string, mode=False):
        """
        :test_string :暴力穷举法
        :return :返回破解完成的字符串
        """
        decode_hash = bytes.fromhex(sha1_string)
        i = 0
        """:i :暴力穷举法 """
        while True:  # 可根据需求调整循环范围
            i += 1
            test_string = hex(i)[2:]
            hashed_test_string = hashlib.sha1(test_string.encode()).digest()
            if hashed_test_string == decode_hash:
                return test_string
            if mode:
                if i % 10000000 == 0:
                    print(f"total: {i} times.")
