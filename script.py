#! /usr/bin/python3

from src.LinkedInService import LinkedInService
from src.GoogleService import GoogleService
from src.CsvService import CsvService
from src.CrawlerService import CrawlerService

crawler  = CrawlerService
linkedIn = LinkedInService
google   = GoogleService
csv      = CsvService

crawler.checkParams()
document = csv.prepareCsvContent()
driver   = linkedIn.signIn()
[driver, urls] = google.getUrls(driver)

for url in urls:
    data = linkedIn.extractDataFromUrl(driver, url)

    csv.logData(data)
    csv.writeData(document, data)

driver.quit()
