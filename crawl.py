import threading
import csv
import json
import requests
from time import sleep
from bs4 import BeautifulSoup

KEYWORDS_1 = ["covid", "covid-19", "coronavirus", "pandemic"]
KEYWORDS_2 = ["economics", "economy", "economic", "business", "money",
              "monetary", "fiscal", "tariff", "price", "shortage", "stock",
              "inflation", "cost", "asset", "tax", "policy"]
KEYWORDS_3 = ["impact", "consequences", "benefits", "effect",
              "result", "influence", "stimulus"]
LIMIT_1 = 20
LIMIT_2 = 5
LIMIT_3 = 5
MONTHS = {"2020-05": "January 2020", "2020-10": "February 2020",
          "2020-16": "March/April 2020", "2020-24": "May/June 2020",
          "2020-29": "July 2020", "2020-34": "August 2020",
          "2020-40": "September 2020", "2020-45 ": "October 2020",
          "2020-50": "November/December 2020"}
SELECTED_SITES = ["cnn.com", "economist.com", "nytimes.com", "abcnews.go.com",
                  "online.wsj.com", "time.com", "usatoday.com",
                  "washingtonpost.com", "forbes.com", "guardian.co.uk",
                  "latimes.com", "timesonline.co.uk", "foxnews.com",
                  "telegraph.co.uk", "huffingtonpost.com",
                  "cbsnews.com", "csmonitor.com" "newsweek.com", "politico.com",
                  "yahoo.com/news", "www.thetimes.co.uk",
                  "npr.org", "nypost.com", "abcnews.go.com", "nbcnews.com",
                  "cbsnews.com",
                  "newsweek.com", "mercurynews.com", "metrotimes.com",
                  "news10.com", ]

Crawl_URLs = [
    f"http://index.commoncrawl.org/CC-MAIN-{date}-index?url=https://{site}&matchType=domain&output=json"
    for date in MONTHS.keys() for site in SELECTED_SITES]
MATCHES = []


def sum_occur(wordlist, content):
    result = 0
    for word in wordlist:
        result += content.count(word)
    return result


def crawler(response, current):
    for site_json in response.content.splitlines():
        if len(MATCHES) > 1000:
            return
        site_json = json.loads(site_json)
        site = ''
        while site == '':
            try:
                site = requests.get(site_json['url'])
                break
            except requests.exceptions:
                sleep(3)
                continue
        if site.status_code != 200:
            continue
        soup = BeautifulSoup(site.content, 'html.parser')
        text = soup.get_text()
        if sum_occur(KEYWORDS_1, text) > LIMIT_1 \
                and sum_occur(KEYWORDS_2, text) > LIMIT_2 \
                and sum_occur(KEYWORDS_3, text) > LIMIT_3:
            MATCHES.append((current, str(site.url)))


def multi_crawl():
    threads = []
    for url in Crawl_URLs:
        response = requests.get(url)
        if response.status_code != 200:
            continue
        index = url.split("-")[3]
        current = MONTHS["2020-" + index]
        thread = threading.Thread(target=crawler, args=(response, current),
                                  daemon=True)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    multi_crawl()
    with open("out.csv", "w", newline="") as f:
        out = csv.writer(f, delimiter=" ")
        out.writerows(MATCHES)
