#https://duiqt.github.io/herta_kuru/
# Kuru kuru~!
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


opt = Options()
# 讓瀏覽器不要自動關閉
opt.add_experimental_option("detach", True)
ser = webdriver.ChromeService()
driver = webdriver.Chrome(service=ser, options=opt)
driver.get("https://duiqt.github.io/herta_kuru/")

# 在等待網頁讀取時，等到這個元素出現才執行下一個動作
kuru = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "counter-button"))
)
# 點擊按鈕
for i in range(10000):
    kuru.click()

# action = ActionChains(driver)
# action.move_to_element(kuru)
# for i in range(10000):
#     action.click(kuru)
#     action.double_click(kuru)
#     action.perform()


