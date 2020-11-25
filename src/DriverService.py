from subprocess import getoutput
from selenium   import webdriver

class DriverService:
    def getDriver():
        chrome_version = getoutput('google-chrome --product-version')[0:2]
        return webdriver.Chrome('./ChromeDriver/linux/'+ chrome_version +'/chromedriver')