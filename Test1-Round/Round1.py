import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import  ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys,ActionChains
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
class Cerner():

    def cerner(self):
        driver.get("https://www.cerner.com")
        driver.maximize_window()
        print(driver.title)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #// used to scroll till the bottom of the webpage.
        # driver.find_element(By.TAG_NAME, value="html").send_keys(Keys.END)
        # time.sleep(4)
        # text = driver.find_element(By.XPATH, "//a[text()='More from Perspectives']")
        # ActionChains(driver).move_to_element(text).perform()
        # time.sleep(2)
        region = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='regionSelector']")))
        ActionChains(driver).move_to_element(region)
        time.sleep(3)
        region.click()
        list1 = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//a[text()='India']")))
        list1.click()
        # driver.get_screenshot_as_file("C:/Users/Amith/Pictures/Screenshots.image.png")
        driver.save_screenshot("image.png")
        # driver.switch_to.alert.dismiss()

        # driver.close()


ref = Cerner()
ref.cerner()



