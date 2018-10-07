import allure
import pytest

class Test01():

    @allure.step('我是测试步骤001')
    def test01(self):
        print("test01被执行")


    ''' Severity：严重级别(BLOCKER,CRITICAL,NORMAL,MINOR,TRIVIAL) '''

    @allure.step('我是测试步骤002')
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test02(self):
        allure.attach('断言开始','学院信息是否更新成功？')
        print("test02被执行")
        allure.attach('断言结束', '更新成功！')
        assert 0

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test03(self):
        print("test03被执行")
        assert True










