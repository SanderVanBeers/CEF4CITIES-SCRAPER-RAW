from multiprocessing import Pool
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import fullsite.spiders.fullsite
from fullsite.spiders.fullsite import FullSiteSpider

def start_scraper(url):
    process = CrawlerProcess(get_project_settings())
    process.crawl(FullSiteSpider, url=url, save_dir = '/output')
    process.start()

if __name__ == '__main__':
    with open('seedlist', 'r') as seedlist:
        urls = seedlist.read().splitlines() 
        pool = Pool()
        pool.map(start_scraper, urls)
        pool.close()
        pool.join()
