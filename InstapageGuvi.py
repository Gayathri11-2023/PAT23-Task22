from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class instapageofguvi:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # Get the url to access
    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(10)
    # Quit the driver
    def quit(self):
        self.driver.quit()
    # Get the number of followers from Guvi official web page
    def  getnumberoffollowers(self):
        xpath = '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button'
        return  self.driver.find_element(by=By.XPATH, value=xpath).text

    # Get the number of following from Guvi official web page
    def getnumberoffollowing(self):
        xpath_1 = '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[3]/button'
        return self.driver.find_element(by=By.XPATH, value=xpath_1).text

url = "https://www.instagram.com/guviofficial/"
obj = instapageofguvi(url)
obj.boot()
# To print the number of followers in the web pge
print(obj.getnumberoffollowers())
# To print the number of following in the web page
print(obj.getnumberoffollowing())
