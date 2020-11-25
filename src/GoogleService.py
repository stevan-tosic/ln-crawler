from selenium.webdriver.common.keys import Keys
from time                           import sleep
from random                         import uniform
from src.DriverService              import DriverService
from src.CrawlerService             import CrawlerService

class GoogleService:
    def getUrls(driver = None):
        if driver is None:
            driver = DriverService.getDriver()
        crawler = CrawlerService
        query = crawler.getSearchQuery()

        driver.get('https://www.google.com/')
        search_query = driver.find_element_by_name('q')
        search_query.send_keys(query)
        search_query.send_keys(Keys.RETURN)
        sleep(uniform(0.5, 3.0))

        searchFirstPage = driver.current_url

        page = 1
        urls = []
        while page <= 150:
            driver.get(searchFirstPage + '&start=' + str((page - 1) * 10))
            links = driver.find_elements_by_xpath('//*[@id="rso"]/div/div/div[1]/a[@href]')
            if (len(links) == 0):
                print(len(urls))
                break
            urls += [url.get_attribute('href') for url in links]
            page += 1
            sleep(uniform(2.0, 3.0))

        return [driver, urls]

    def getCompanyUrls(driver = None):
        if driver is None:
            driver = DriverService.getDriver()
        crawler = CrawlerService
        query = crawler.getCompanySearchQuery()

        driver.get('https://www.google.com/')
        search_query = driver.find_element_by_name('q')
        search_query.send_keys(query)
        search_query.send_keys(Keys.RETURN)
        sleep(uniform(0.5, 3.0))

        searchFirstPage = driver.current_url

        page = 1
        urls = []
        while page < 10:
            driver.get(searchFirstPage + '&start=' + (page - 1) * 10)
            links = driver.find_elements_by_xpath('//*[@id="rso"]/div/div/div[1]/a[@href]')
            urls += [url.get_attribute('href') for url in links]
            page += 1
            sleep(uniform(0.5, 3.0))

        print(urls)
        return [driver, urls]
