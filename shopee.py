from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
import time

# set url
edge_driver_path = r'edgedriver_win64\msedgedriver.exe'
service = Service(executable_path=edge_driver_path)
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(service=service, options=options)

# open url
driver.get("https://www.lelai.com.tw/products/nike-dunk-low-%E7%86%8A%E8%B2%93-1")

#test 
#driver.get("https://www.lelai.com.tw/products/philips-funcube-20-%E5%A4%9A%E5%90%88%E4%B8%80%E7%A3%81%E5%90%B8%E8%A1%8C%E5%8B%95%E9%9B%BB%E6%BA%90type-c-dlp4348c")

# ty click
while True:
    try:
        print("trying clicking...")
        # wait until btn can click
        buy_now_button = WebDriverWait(driver, 4).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn-buy-now') and contains(@ng-click, 'addItemToCart')]"))
        )

        # move to btn and click
        actions = ActionChains(driver)
        actions.move_to_element(buy_now_button).click().perform()
        print("success click")
        
        # success than break
        break  

    except Exception as e:
        print(f"btn can't be clicked \n ERROR: {e}")
        
        # reload
        driver.refresh()  

        # wait reload
        time.sleep(0.5)
        print("reloading ...")

time.sleep(2)

# login
email_input = driver.find_element(By.ID, "field-1")
password_input = driver.find_element(By.ID, "field-2")


# ===============================================================================================================================here
email_input.send_keys("richunri544@gmail.com")
password_input.send_keys("s1nnplevvorcl")
# ===============================================================================================================================here

# click but
submit_button = driver.find_element(By.CSS_SELECTOR, "[data-e2e-id='login-submit_button']")
submit_button.click()

time.sleep(2)

try:
    skip_button = driver.find_element(By.CSS_SELECTOR, ".emotion-css-cache-1fh616s")
    ActionChains(driver).move_to_element(skip_button).click().perform()
    print("已成功点击略過按钮。")
except Exception as e:
    print("找不到略過按钮:", e)


print("Fuction done")