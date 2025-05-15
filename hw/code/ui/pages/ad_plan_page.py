from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdPlanPage(BasePage):
    url = 'https://ads.vk.com/hq/new_create/ad_plan'
    locators = {
        'ad_name_input': (By.ID, 'ad-name'),
    }

    def create_company_by_site(self, site):
        self.click((By.CSS_SELECTOR, 'div[data-id="site_conversions"]'))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/main/div[2]/div[1]/div/div/div/div/div/section[2]/fieldset/form/div[1]/div/div/div/div')))
        self.focus((By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/main/div[2]/div[1]/div/div/div/div/div/section[2]/fieldset/form/div[1]/div/div/div/div'))
        self.click((By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/main/div[2]/div[1]/div/div/div/div/div/section[2]/fieldset/form/div[1]/div/div/div/div'))
        self.input_text((By.CSS_SELECTOR, 'input[id="search-:r12:"]'), site)
        self.click((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/div/form/div[2]/div[2]/div/div'))

    def set_data(self, data):
        self.click((By.CSS_SELECTOR, 'span[data-testid="end-date"]'))
        self.click((By.CSS_SELECTOR, f'div[aria-label={data}]'))

    def input_data_about_site(self, description, budget, data):
        self.input_text((By.CSS_SELECTOR, 'textarea[placeholder="Опишите ваше предложение"]'), description)
        self.click((By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/main/div[2]/div[1]/div/div/div/div/div/section[2]/fieldset/form/div[6]/div/div/div[1]/div[2]'))
        self.click((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/div/form/div[2]/div[2]/div[2]/div/div[2]'))
        self.input_text((By.CSS_SELECTOR, 'textarea[placeholder="Не задан"]'), budget)

        self.click((By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/main/div[2]/div[1]/div/div/div/div/div/section[2]/fieldset/form/div[9]/div/div/div/div/div/div'))
        self.focus((By.XPATH, '//span[contains(text(), "за всё время")]'))
        self.click((By.XPATH, '//span[contains(text(), "за всё время")]'))

        self.set_data(data)

        self.click((By.XPATH, '//*[@id="footer"]/div/div/div/div/button'))

    def test_more_group(self):
        self.click((By.XPATH, f'/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/main/div[2]/div[1]/div/div/div/div/div/button'))
        self.click((By.CSS_SELECTOR, f'button[aria-label="More"]'))
        self.click((By.XPATH, f'/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/div[1]/div[2]'))
        self.click((By.CSS_SELECTOR, f'button[data-testid="button-remove"]'))

    def all_data(self, data):
        self.click((By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/main/div[2]/div[1]/div/div/div/div/div/section[1]/fieldset/div[2]/div[1]/div/div'))
        self.click((By.CSS_SELECTOR, f'div[aria-disabled="false"]'))
        self.click((By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/main/div[2]/div[1]/div/div/div/div/div/section[1]/fieldset/div[2]/div[1]/div/div'))

        self.set_data(data)
        self.click((By.CSS_SELECTOR, f'button[aria-label="Очистить поле"]'))
        self.set_data(data)

        self.click((By.XPATH,
                    '/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/main/div[2]/div[1]/div/div/div/div/div/section[1]/fieldset/div[2]/div[2]/div'))
        self.click((By.XPATH,
                    '/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/button[2]'))
        self.click((By.XPATH,
                    '/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[4]/button'))
        self.click((By.CSS_SELECTOR, f'div[data-id="0"]'))
        self.click((By.XPATH,
                    '/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[5]/button'))

        self.click((By.XPATH,
                    '/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/main/div[2]/div[1]/div/div/div/div/div/section[2]/div[2]/fieldset/div/div/div[2]/button'))
        self.input_text((By.CSS_SELECTOR, f'textarea[placeholder="Например: Россия, Москва, 468"]'), "Россия, Москва \n Россия, Санкт-Петербург")
        self.click((By.XPATH,
                    '/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/div/form/div[2]/button'))
        self.click((By.CSS_SELECTOR, f'button[aria-label="close_button"]'))

        self.click((By.CSS_SELECTOR, f'div[id="react-collapsed-toggle-:r12:"]'))
        self.click((By.XPATH, f'/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/main/div[2]/div[1]/div/div/div/div/div/div/section[1]/div[2]/fieldset/div[2]/div/div[1]/div[2]'))
        self.click((By.CSS_SELECTOR, f'div[data-item-id="16"]'))
        self.click((By.XPATH, f'/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/main/div[2]/div[1]/div/div/div/div/div/div/section[1]/div[2]/fieldset/div[4]/div/div'))
        self.click((By.CSS_SELECTOR, f'option[value="16+"]'))

        self.click((By.CSS_SELECTOR, f'div[id="react-collapsed-toggle-:rt:"]'))
        self.click((By.CSS_SELECTOR, f'div[id="react-collapsed-toggle-:r1e:"]'))
        self.click((By.XPATH, f'/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/main/div[2]/div[1]/div/div/div/div/div/div/section[2]/div[2]/fieldset/div[1]/div[1]/svg'))
        self.click((By.CSS_SELECTOR, f'div[id="react-collapsed-toggle-:r1e:"]'))
        self.click((By.XPATH, f'/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/main/div[2]/div[1]/div/div/div/div/div/div/section[2]/div[2]/fieldset/div[1]/div[2]/div/div/span'))
        self.click((By.CSS_SELECTOR, f'div[data-id="9018"]'))
        self.click((By.XPATH, f'/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/button'))

        self.click((By.CSS_SELECTOR, f'div[id="react-collapsed-toggle-:ru:"]'))
        self.click((By.XPATH, f'/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/main/div[2]/div[1]/div/div/div/div/div/div/section[3]/div[2]/fieldset/div[1]/div/div/span'))
        self.click((By.CSS_SELECTOR, f'div[data-item-id="11356434"]'))
        self.click((By.XPATH, f'/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/button'))

        self.click((By.XPATH, f'/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/main/div[2]/div[1]/div/div/div/div/div/div/section[3]/div[2]/fieldset/div[1]/div/button'))
        self.click((By.XPATH, f'/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/main/div[2]/div[1]/div/div/div/div/div/div/section[3]/div[2]/fieldset/div[1]/div[2]/button'))

        self.test_more_group()

        self.click((By.XPATH, f'/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/footer/div/div[2]/div[2]/div/button'))

    def input_rich_text(self, locator, text):
        elem = self.wait().until(EC.element_to_be_clickable(locator))
        elem.click()
        elem.send_keys(text)
        self.wait().until(lambda drv:
                          drv.find_element(*locator).get_attribute("textContent").strip() == text
                          )

    def ending(self, logo_path, title, short_description, long_description):
        self.click((By.XPATH, '//*[@data-testid="change-image"]'))
        self.find((By.XPATH, '//input[@type="file"]')).send_keys(logo_path)
        self.focus((By.XPATH, '//*[contains(@class, "ItemList_item")]'))
        self.click((By.XPATH, '//*[contains(@class, "ItemList_item")]'))
        self.wait().until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "TitleBlock-module_appLogo")]/img')))

        self.input_rich_text((By.CSS_SELECTOR, 'div[data-testid="заголовок, макс. 40 символов"]'), title)
        self.input_rich_text((By.CSS_SELECTOR, 'div[data-testid="описание, макс. 90 символов"]'), short_description)
        self.input_rich_text((By.CSS_SELECTOR, 'div[data-testid="Длинный текст для использования в лентах соцсетей (2000 знаков)"]'), long_description)
