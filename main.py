from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://demoqa.com/checkbox")


boxToggleHome=driver.find_element(by=By.XPATH, value="//button[@title='Toggle']//*[name()='svg']")
checkBoxHome=driver.find_element(by=By.XPATH, value="//label[@for='tree-node-home']//span[@class='rct-checkbox']//*[name()='svg']")

boxToggleHome.click()
checkBoxHome.click()

boxToggleDesktop = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='tree-node']/ol/li/ol/li[1]/span/button")))
boxToggleDesktop.click()

checkBoxNotes = driver.find_element(by=By.ID, value="tree-node-notes")


##checkBoxWorkSpace = driver.find_element(by=By.ID, value="tree-node-workspace")
##checkBoxExcel = driver.find_element(by=By.ID, value="tree-node-excelFile")














