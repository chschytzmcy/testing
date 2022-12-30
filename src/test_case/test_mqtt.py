import pytest
import allure
import logging
from util.assert_util import assert_keyword
from util.request_util import api_request
from util.global_var import *
from util.excel_util import excel_util

check_mqtt_test_data = excel_util.get_sheet_data("MQTT")

@allure.feature("MQTT 模块")
@pytest.mark.dependency(name="TestMQTTModule")
class TestMQTTModule:
    @allure.story("检测 MQTT RPC 通道功能")
    @allure.title('Check MQTT RPC')  # 指定测试用例标题，默认是函数名
    @allure.description('检测云端到设备的MQTT RPC 通道是否正常')  # 添加测试用例描述
    @allure.severity(allure.severity_level.BLOCKER)  # 阻塞级别
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('case_data', check_mqtt_test_data)
    def test_check_mqtt(self, case_data):
        with allure.step("读取请求数据，调用接口"):
            logging.info("接口用例数据：%s" % case_data)
            response = api_request(case_data[API_IP], case_data[API_URI], case_data[REQUEST_METHOD],
                                   case_data[API_REQUEST_DATA], case_data[RESPONSE_EXTRACT_VAR],
                                   case_data[REQUEST_HEADER], case_data[REQUEST_COOKIE])
        with allure.step("获取响应数据，进行断言"):
            assert_keyword(response, case_data[RESPONSE_ASSERT_KEYWORD])

    @allure.story("检测 MQTT RPC 通道功能1111")
    @allure.title('Check MQTT RPC1111')  # 指定测试用例标题，默认是函数名
    @allure.description('检测云端到设备的MQTT RPC 通道是否正常11111')  # 添加测试用例描述
    @allure.severity(allure.severity_level.BLOCKER)  # 阻塞级别
    @pytest.mark.run(order=1)
    def test_check_mqtt1(self):
        x = "this"
        assert "h" in x

'''
if __name__ == "__main__":
    test_dir = os.path.dirname(__file__)
    pytest.main(['-s', '-q', test_dir, '--alluredir', '../test_result/', "--clean-alluredir"])
    os.system('allure generate ../test_result/ -o ../test_report/ --clean')
    os.system('allure open -h 127.0.0.1 -p 8881 ../test_report/')
'''

if __name__ == '__main__':
    pytest.main(['-s', '-v', "test_case/test_mqtt.py", "--alluredir", RESULT_TEST_DIR, "--clean-alluredir"])
    os.system("allure generate %s -o %s --clean" % (RESULT_TEST_DIR, REPORT_TEST_DIR))
    os.system("allure open -h 0.0.0.0 -p 8881 %s" % REPORT_TEST_DIR)