import time
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from ui.pages.survey_page import SurveyPage
from ui.pages.ad_plan_page import AdPlanPage


@pytest.fixture(scope='session')
def driver(config):
    browser = config['browser']
    url = config['url']
    selenoid = config.get('selenoid', False)
    vnc = config.get('vnc', False)
    headless = config.get('headless', False)

    options = Options()

    if headless:
        options.add_argument('--headless=new')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

    if selenoid:
        caps = options.to_capabilities()
        caps['browserName'] = 'chrome'
        caps['browserVersion'] = '118.0'
        caps['selenoid:options'] = {
            'enableVNC': bool(vnc),
        }
        driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=caps,
        )
    else:
        if browser == 'chrome':
            THIS_DIR = os.path.dirname(__file__)
            HW_DIR = os.path.abspath(os.path.join(THIS_DIR, os.pardir))
            chromedriver_path = os.path.join(HW_DIR, 'chromedriver-win64', 'chromedriver.exe')
            print("ChromeDriver path:", chromedriver_path)

            if not os.path.isfile(chromedriver_path):
                raise FileNotFoundError(f"ChromeDriver not found at {chromedriver_path}")
            service = Service(executable_path=chromedriver_path)
            options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

            if not os.path.isfile(options.binary_location):
                raise FileNotFoundError(f"Chrome binary not found at {options.binary_location}")
            driver = webdriver.Chrome(service=service, options=options)
        elif browser == 'firefox':
            driver = webdriver.Firefox(options=options)
        else:
            raise RuntimeError(f'Unsupported browser: "{browser}"')

    driver.maximize_window()
    driver.get('https://ads.vk.com/hq/overview')
    time.sleep(60)  # Пауза на 60 секунд для ручной авторизации
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture
def survey_page(driver):
    return SurveyPage(driver)


@pytest.fixture
def ad_plan_page(driver):
    return AdPlanPage(driver)
