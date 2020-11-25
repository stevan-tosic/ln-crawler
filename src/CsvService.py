import csv
from selenium import webdriver

class CsvService:
    def prepareCsvContent():
        writer = csv.writer(open('output.csv', 'w+', encoding='utf-8-sig', newline=''))
        writer.writerow(['Name', 'Position', 'Company', 'Company URL', 'Location', 'URL'])

        return writer

    def prepareCompanyCsvContent():
        writer = writer(open('CompanyOutput.csv', 'w+', encoding='utf-8-sig', newline=''))
        writer.writerow(['Name', 'Position', 'Company', 'Company URL', 'Location', 'URL'])

        return writer


    def writeData(writer, data):
        [name, position, company, companyUrl, location, url] = data
        writer.writerow([name,
                 position,
                 company,
                 companyUrl,
                 location,
                 url])

    def writeCompanyData(writer, data):
        [name, position, company, companyUrl, location, url] = data
        writer.writerow([name,
                 position,
                 company,
                 companyUrl,
                 location,
                 url])

    def logCompanyData(data):
        [name, position, company, companyUrl, location, url] = data
        print('\n')
        print('Name: ', name)
        print('Position: ', position)
        print('Company: ', company)
        print('Company URL: ', companyUrl)
        print('Location: ', location)
        print('URL: ', url)
        print('\n')

    def logData(data):
        [name, position, company, companyUrl, location, url] = data
        print('\n')
        print('Name: ', name)
        print('Position: ', position)
        print('Company: ', company)
        print('Company URL: ', companyUrl)
        print('Location: ', location)
        print('URL: ', url)
        print('\n')