import allure
import pytest
class Test01():
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step("开始执行测试001方法")
    def test001(self):
        allure.attach("描述：","正在登录操作...")
        print("登录成功！")

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step("开始执行测试002方法")
    def test02(self):
        allure.attach("描述：","正在退出操作...")
        print("退出成功！")


    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test03(self):
        print("test003")