from time              import sleep
from parsel            import Selector
from random            import uniform
from src.DriverService import DriverService

class LinkedInService:
    def signIn():
        driver = DriverService.getDriver()
        driver.get('https://www.linkedin.com/')

        username = driver.find_element_by_name("session_key")
        username.send_keys('testlenatestlena@gmail.com')
        sleep(uniform(0.5, 3.0))

        password = driver.find_element_by_name('session_password')
        password.send_keys('vangogh23')
        sleep(uniform(0.5, 3.0))

        sign_in_button = driver.find_element_by_class_name('sign-in-form__submit-button')
        sign_in_button.click()
        sleep(2)

        return driver

    def extractDataFromUrl(driver, url):
        if driver is None:
            driver = DriverService.getDriver()
        driver.get(url)
        sleep(uniform(2.0, 10.0))

        sel = Selector(text = driver.page_source)

        name = sel.xpath('//*[@class = "inline t-24 t-black t-normal break-words"]/text()').extract_first()
        name = ' '.join(name.split()) if name else None

        positionWithCompany = sel.xpath('//h2[@class="mt1 t-18 t-black t-normal break-words"]/text()').extract_first()
        extractedValues = positionWithCompany.split(' at ') if positionWithCompany else None
        position = ''.join(extractedValues[0]) if extractedValues and len(extractedValues) else None
        company = ''.join(extractedValues[1]) if extractedValues and len(extractedValues) == 2 else None

        companyUrls = driver.find_elements_by_xpath('//section[@class="pv-profile-section__card-item-v2 pv-profile-section pv-position-entity ember-view"]//a[@href]')
        companyUrl = ''.join(companyUrls[0].get_attribute('href')) if len(companyUrls) else None

        location = sel.xpath('//*[@class = "t-16 t-black t-normal inline-block"]/text()').extract_first()
        location = ' '.join(location.split()) if location else None

        url = driver.current_url

        return [name, position, company, companyUrl, location, url]

    def extractDataFromCompanyUrl(driver, url):
        if driver is None:
            driver = DriverService.getDriver()
        driver.get(url)
        sleep(2)

        sel = Selector(text = driver.page_source)

        name = sel.xpath('//*[@class = "inline t-24 t-black t-normal break-words"]/text()').extract_first()
        name = ' '.join(name.split()) if name else None

        positionWithCompany = sel.xpath('//h2[@class="mt1 t-18 t-black t-normal break-words"]/text()').extract_first()
        extractedValues = positionWithCompany.split(' at ') if positionWithCompany else None
        position = ' '.join(extractedValues[0]) if extractedValues and len(extractedValues) else None
        company = ' '.join(extractedValues[1]) if extractedValues and len(extractedValues) == 2 else None

        companyUrls = driver.find_elements_by_xpath('//section[@class="pv-profile-section__card-item-v2 pv-profile-section pv-position-entity ember-view"]//a[@href]')
        companyUrl = ' '.join(companyUrls[0].get_attribute('href')) if len(companyUrls) else None

        location = sel.xpath('//*[@class = "t-16 t-black t-normal inline-block"]/text()').extract_first()
        location = ' '.join(location.split()) if location else None

        url = driver.current_url

        return [name, position, company, companyUrl, location, url]
