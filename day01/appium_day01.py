# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "android"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(15)
el1 = driver.find_element_by_xpath("//android.widget.ImageView[@content-desc=\"萝卜投研\"]")
el1.click()
el2 = driver.find_element_by_id("com.datayes.irr:id/ll_tab_4")
el2.click()
el3 = driver.find_element_by_id("com.datayes.irr:id/ll_tab_1")
el3.click()
el4 = driver.find_element_by_id("com.datayes.irr:id/dy_right_button")
el4.click()

driver.quit()