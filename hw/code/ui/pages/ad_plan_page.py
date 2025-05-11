from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AdPlanPage(BasePage):
    url = 'https://ads.vk.com/hq/new_create/ad_plan'
    locators = {
        'ad_name_input': (By.ID, 'ad-name'),
    }

    def set_ad_name(self, name):
        self.input_text(self.locators['ad_name_input'], name)