from sys import exit, argv

class CrawlerService:
    def checkParams():
        params = argv[1:]
        if len(params) == 0:
            print('Please pass search params as argument: script.py "param 1", "param 2"...')
            exit()

    def getSearchQuery():
        params = argv[1:]
        query = 'site:linkedin.com/in'
        for param in params:
            query += ' AND "' + param + '"'
        return query

    def getCompanySearchQuery():
        params = argv[1:]
        query = 'site:linkedin.com/company'
        for param in params:
            query += ' AND "' + param + '"'
        return query
