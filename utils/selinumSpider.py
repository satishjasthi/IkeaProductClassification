"""
About: script to create an instance of chrome browser for selenium based web scraping

Author: Satish Jasthi
"""

from utils import chrome_driver

from selenium import webdriver


class Scraper(object):

    def __init__(self):
        self.browser = webdriver

    def launch_browser(self):
        options = self.browser.ChromeOptions()
        options.add_argument('headless')
        browser_con = self.browser.Chrome(executable_path=chrome_driver.as_posix())#,chrome_options=options
        return browser_con