import os,sys

from tools.get_driver import Driver

sys.path.append(os.getcwd())

import pytest

from page.page import PageFind

def get_data():
    return [123]
class TestSet(object):
    # 初始化
    def setup(self):
        self.driver = Driver.get_driver()
        self.find = PageFind(self.driver)
    # 结束
    def teardown(self):
        self.find.driver.quit()
    # 测试用例
    @pytest.mark.parametrize("text",get_data())
    def test01(self,text):
        self.find.handle(text)
if __name__ == '__main__':
    pytest.main("-s test_setting.py")