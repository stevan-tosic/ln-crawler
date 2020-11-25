#! /usr/bin/python3

from src.LinkedInService import LinkedInService
from src.GoogleService   import GoogleService
from src.CsvService      import CsvService
from src.CrawlerService  import CrawlerService

crawler  = CrawlerService
linkedIn = LinkedInService
google   = GoogleService
csv      = CsvService

crawler.checkParams()
document = csv.prepareCompanyCsvContent()
driver   = linkedIn.signIn()
[driver, urls] = google.getCompanyUrls(driver)

for url in urls[:1]:
    data = linkedIn.extractDataFromCompanyUrl(driver, url)

    csv.logCompanyData(data)
    csv.writeCompanyData(document, data)

driver.quit()
