from selenium.webdriver.common.by import By
# 点击搜索按钮
set_research = By.ID,"com.android.settings:id/search"
# 输入123
set_input = By.ID,"android:id/search_src_text"
# 点击返回
return_btn = By.CLASS_NAME,"android.widget.ImageButton"