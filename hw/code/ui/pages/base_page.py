from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException


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

    def click_retry(self, locator, retries=3, timeout=2):
        for _ in range(retries):
            try:
                self.click(locator)
                return
            except StaleElementReferenceException:
                WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located(locator)
                )
        raise RuntimeError(f"Не удалось кликнуть по {locator} из-за устаревшего элемента")

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

    def exists(self, locator, timeout=2):
        try:
            return self.wait(timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return None

    def clear_field(self, field_locator: tuple[str, str]):
        field = self.find(field_locator)
        self.driver.execute_script("arguments[0].value = '';", field)
        self.wait().until(lambda driver: field.get_attribute('value') == '')

    def find_elements(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_all_elements_located(locator))
    
    def get_field_value(self, field_locator: tuple[str, str]):
        return self.find(field_locator).get_attribute('value')

    def submit(self, locator, timeout=None):
        self.find(locator, timeout).submit()

    def new_url(self, url):
        self.driver.get(url)

    def scroll_into_view(self, locator, retries=3, timeout=2):
        for _ in range(retries):
            try:
                el = self.find(locator)
                self.driver.execute_script("arguments[0].scrollIntoView(true);", el)
                return
            except StaleElementReferenceException:
                WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located(locator)
                )
        raise RuntimeError(f"Не удалось кликнуть по {locator} из-за устаревшего элемента")
