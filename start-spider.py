from multiprocessing import Pool
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import fullsite.spiders.fullsite
from fullsite.spiders.fullsite import FullSiteSpider
import os

def start_scraper(url):
    process = CrawlerProcess(get_project_settings())
    process.crawl(FullSiteSpider, url=url, save_dir = os.path.join('/output', language_prefix), model_path=os.path.join('/workdir/languages', language_prefix, 'model.p'))
    process.start()

if __name__ == '__main__':
    language_prefix = os.environ.get('language')
    with open(os.path.join('/workdir/languages', language_prefix, 'seedlist'), 'r') as seedlist:
        urls = seedlist.read().splitlines()
        pool = Pool()
        pool.map(start_scraper, urls)
        pool.close()
        pool.join()
