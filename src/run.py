import pytest
import os
from util.global_var import *



if __name__ == '__main__':
    pytest.main(['-s', '-v', "test_case/test_mqtt.py", "--alluredir", RESULT_TEST_DIR, "--clean-alluredir"])
    os.system("allure generate %s -o %s --clean" % (RESULT_TEST_DIR, REPORT_TEST_DIR))
    os.system("allure open -h 0.0.0.0 -p 8881 %s" % REPORT_TEST_DIR)