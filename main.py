import requests, time, logging
from bs4 import BeautifulSoup

class WebCrawler:
    def __init__(self, startURl, maxDepth=3, crawlDelay=1):
        self.startURl = startURl
        self.maxDepth = maxDepth
        self.crawlDelay = crawlDelay
        self.visitedURLs = set()
        self.queue = [(startURl, 0)]

    def fetchAndParse(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html,'html.parser')

            else:
                logging.error(f"Failed to fetch {url}")
        except Exception as e:
            logging.error(f"Error processing {url}: {str(e)}")

    def processURL(self, url, depth):
        if url not in self.visitedURLs and depth <= self.maxDepth:
            self.visitedURLs.add(url)
            self.fetchAndParse(url)
            time.sleep(self.crawlDelay)


    def crawl(self):
        while self.queue:
            url, depth = self.queue.pop(0)
            self.processURL(url, depth)
            if depth < self.maxDepth:
                links = []
                for link in links:
                    if link not in self.visitedURLs:
                        self.queue.append((link, depth + 1))

startURl = "https://www.fivenightsatfreddys.movie/"
web_crawler = WebCrawler(startURl)
web_crawler.crawl()

