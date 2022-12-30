import pytest
import logging
#from util.global_var import *

class TestClass:
    def test_one(self):
        logging.info("test case 111111")
        print("6666666666666")
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")

    def test_three(self):
        x = "1111"
        assert hasattr(x, "222")

    def test_forth(self):
        logging.info("test case 111111")
        x = "this"
        assert "h" in x

