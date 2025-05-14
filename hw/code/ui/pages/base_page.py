from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium import webdriver


class PageNotOpenedException(Exception):
    pass


class BasePage:
    url: str = ''

    def __init__(self, driver):
        self.driver = driver

    def is_opened(self, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedException(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def wait(self, timeout=None):
        return WebDriverWait(self.driver, timeout or 5)

    def open_and_wait(self, url: str = None):
        url = url if url is not None else self.url
        self.driver.get(url)
        self.wait().until(EC.url_matches(url))

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=None):
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    def safe_send_keys(self, element, text):
        if any(ord(c) > 0xFFFF for c in text):
            self.driver.execute_script("arguments[0].value = arguments[1];", element, text)
        else:
            element.clear()
            element.send_keys(text)

    def input_text(self, locator, text, timeout=None):
        element = self.find(locator, timeout)
        self.safe_send_keys(element, text)

    def focus(self, locator, timeout=None):
        el = self.find(locator, timeout=timeout)
        webdriver.ActionChains(self.driver).move_to_element(el).perform()

    def submit(self, locator, timeout=None):
        self.find(locator, timeout).submit()

    def new_url(self, url):
        self.driver.get(url)
