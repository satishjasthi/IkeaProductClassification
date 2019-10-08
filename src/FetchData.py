"""
Reference: 
Usage:

About: Script to scrape data from IKEA.com for different product categories

Author: Satish Jasthi
"""
from time import sleep
import urllib.request

from tqdm import tqdm

from utils import data_dir
from utils.selinumSpider import Scraper


class DataScraper:

    def __init__(self):
        self.browser = Scraper().launch_browser()
        self.home_page = 'https://www.ikea.com/in/en/cat'
        self.product_urls = {'beds': f'{self.home_page}/beds-bm003/?page=10',
                             'chairs': f'{self.home_page}/chairs-fu002/?page=20',
                             'wardrobes': f'{self.home_page}/wardrobes-19053/?page=10',
                             'candle_holders': f'{self.home_page}/candle-holders-candles-10760/?page=20'
                             }
        # xpath of image in product page
        self.image_xpath = """//*[@id="content"]/div[4]/div[2]/div/div/
        div[2]/div[1]/div[1]/div/div[*]/div/div/a[1]/div/div/div/img"""
        self.data_dir = data_dir

    def download_product_images(self, product_name: str):
        """
        Method to scrape and download images related to given product_name
        :param product_name: str, name of product category
        :return: None
        """
        product_dir = self.data_dir / f'{product_name}'
        product_dir.mkdir(parents=True, exist_ok=True)

        # load product page in browser
        self.browser.get(self.product_urls[product_name])
        sleep(10)

        # scrolling web page from top to bottom multiple times to ensure images are loaded
        for i in range(5):
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.browser.execute_script("window.scrollTo(document.body.scrollHeight, 0);")

        image_xpaths = self.browser.find_elements_by_xpath(self.image_xpath)
        assert len(image_xpaths) > 1, f'Number of image_xpaths == {len(image_xpaths)}'

        # downloading images
        print(f'Downloading {product_name} images...............')
        for indx, image_xpath in tqdm(enumerate(image_xpaths)):
            img_path = product_dir / f'{product_dir.name}_{indx}.jpeg'
            try:
                urllib.request.urlretrieve(image_xpath.get_attribute('src'), img_path.as_posix())
            except Exception as e:
                print(f'Failed downloading image\nError:{e}')
                print('\n Trying to download after 5 secs')
                sleep(5)
                urllib.request.urlretrieve(image_xpath.get_attribute('src'), img_path.as_posix())

    def scrape_products_data(self):
        """
        Method to scrape all product images
        :return: None
        """
        for product in self.product_urls.keys():
            self.download_product_images(product_name=product)
        self.browser.close()


if __name__ == "__main__":
    o = DataScraper()
    o.scrape_products_data()
