from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


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
        #self.click((By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > div.ModalRoot_componentWrapper__uzHTL > form > div.ModalSidebarPage_contentWithoutHeader__cVnVe > div.ModalSidebarPage_contentWithFooter__BOnBg > div.ModalSidebarPage_content__2mBu8 > section > div > div:nth-child(3) > div'))
        #file_input.send_keys(logo_path)
        self.input_text((By.CSS_SELECTOR, 'input[placeholder="Введите название компании"]'), company)
        #self.input_text((By.CSS_SELECTOR, 'input[placeholder="Введите заголовок"]'), title)
        self.input_text((By.CSS_SELECTOR, 'textarea[placeholder="Введите описание опроса"]'), description)
        self.click((By.CSS_SELECTOR, f'div[data-id="{style_id}"]'))

    def proceed_to_questions(self):
        self.click((By.XPATH, '//button[contains(text(), "Далее")]'))
