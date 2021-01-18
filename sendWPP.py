import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

Url = "https://web.whatsapp.com/"
UserName = "WHO WLL RECEIVE THE MESSAGE"
MessageText = "MESSAGE"

firefoxProfile = webdriver.FirefoxProfile(
    'YOUR PROFILE PATH')
driver = webdriver.Firefox(firefoxProfile)
driver.get(Url)
time.sleep(20) #Added because of the time until WhatsApp page load.

searchBar = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]")
searchBar.click()
searchBar.send_keys(UserName)
spanTag = driver.find_element_by_xpath("//span[contains(@title, UserName)]")
spanTag.click()

sendBar = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
sendBar.click()
sendBar.send_keys(MessageText)
time.sleep(3)
sendButton = driver.find_element_by_class_name("_35EW6")
sendButton.click()

