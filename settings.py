# scrapy config
DOWNLOAD_DELAY = 0.2
CONCURRENT_REQUESTS_PER_DOMAIN = 10
AUTOTHROTTLE_ENABLED = True

# custom config
# status codes to be reported in CSV
REPORT_IF = [200, 404, 500, 400, 503]
INCLUDE_CHILDS = False
OUTPUT_FILE= './results/scrapy-results.csv'
OUTPUT_FORMAT='csv'
# pass in a list of domains

DISALLOWED_DOMAINS = ['www.adobe.com']

# override settings
NAME = 'override'
ALLOWED_DOMAINS = ['allowed_domains']
START_URLS = ['https://google.com']

INCLUDE_CHILDREN=False