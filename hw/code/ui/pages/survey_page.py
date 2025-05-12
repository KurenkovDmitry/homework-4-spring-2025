from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class SurveyPage(BasePage):
    url = 'https://ads.vk.com/hq/leadads/surveys'
    locators = {
        'create_survey_button': (By.CSS_SELECTOR, '[test-id="create-survey-button"]'),
    }

    def create_survey(self):
        self.click(self.locators['create_survey_button'])
        self.wait().until(EC.presence_of_element_located((By.CLASS_NAME, 'ModalSidebarPage_content__2mBu8')))

    def fill_survey_form(self, name, company, title, description, logo_path, style_id):
        self.input_text((By.CSS_SELECTOR, 'input[placeholder="Введите название"]'), name)
        self.click((By.XPATH, '//*[@data-testid="set-global-image"]'))

        self.find((By.XPATH, '//input[@type="file"]')).send_keys(logo_path)
        self.focus((By.XPATH, '//*[contains(@class, "ItemList_item")]'))
        self.click((By.XPATH, '//*[contains(@class, "ItemList_item")]'))
        self.wait().until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "TitleBlock-module_appLogo")]/img')))

        self.input_text((By.CSS_SELECTOR, 'input[placeholder="Введите название компании"]'), company)
        self.input_text((By.CSS_SELECTOR, 'textarea[placeholder="Введите описание опроса"]'), description)
        self.click((By.CSS_SELECTOR, f'div[data-id="{style_id}"]'))
        self.input_text((By.CSS_SELECTOR, 'input[placeholder="Введите заголовок"]'), title)
        self.click((By.CSS_SELECTOR, f'button[data-testid="submit"]'))

    def proceed_to_questions(self):
        self.click((By.XPATH, '//button[contains(text(), "Далее")]'))
