import page
from base.base import Base


class PageFind(Base):
    #  点击搜索
    def click_research(self):
        self.base_click(page.set_research)
    #  输入123
    def input_text(self,text):
        self.base_input(page.set_input,text)
    #  点击返回
    def return_home(self):
        self.base_click(page.return_btn)
    # 组合方法
    def handle(self,text):
        self.click_research()
        self.input_text(text)
        self.return_home()