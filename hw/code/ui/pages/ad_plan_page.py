from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui.locators.ad_plan_locators import AdPlanLocators


class AdPlanPage(BasePage):
    url = AdPlanLocators.URL

    def create_company_by_site(self, site):
        self.click(AdPlanLocators.SITE_CONVERSIONS_TAB)
        self.input_text(AdPlanLocators.SITE_INPUT, site)
        self.click(AdPlanLocators.SITE_CONVERSIONS_TAB)

    def set_data(self, date_label):
        self.click(AdPlanLocators.END_DATE_TRIGGER)
        self.click(AdPlanLocators.DATE_OPTION(date_label))

    def input_data_about_site(self, description, budget, date_label):
        self.input_text(AdPlanLocators.DESCRIPTION_TEXTAREA, description)
        self.input_text(AdPlanLocators.BUDGET_TEXTAREA, budget)

        self.click(AdPlanLocators.BUDGET_FIELD)
        self.click(AdPlanLocators.BUDGET_POPUP_FIRST)

        self.set_data(date_label)

        self.click(AdPlanLocators.SUBMIT_BUTTON)

    def test_more_group(self):
        self.click(AdPlanLocators.MORE_GROUP_BUTTON)
        self.click(AdPlanLocators.MORE_BUTTON)
        self.click(AdPlanLocators.GROUP_POPUP_ITEM)
        self.click(AdPlanLocators.REMOVE_BUTTON)

    def all_data(self, date_label, address):
        self.click(AdPlanLocators.ALL_DATA_TRIGGER)
        self.click(AdPlanLocators.ENABLED_OPTION)
        self.click(AdPlanLocators.ALL_DATA_TRIGGER)

        self.set_data(date_label)
        self.click(AdPlanLocators.CLEAR_FIELD)
        self.set_data(date_label)

        self.click(AdPlanLocators.DATA_SUBSECTION_TRIGGER)
        self.click(AdPlanLocators.POPUP_NEXT)
        self.click(AdPlanLocators.POPUP_SELECT_LAST)
        self.click(AdPlanLocators.FIRST_OPTION)
        self.click(AdPlanLocators.POPUP_SELECT_FIFTH)

        # локация
        self.click(AdPlanLocators.LOCATION_ADD_BUTTON)
        self.input_text(AdPlanLocators.LOCATION_TEXTAREA, address)
        self.click(AdPlanLocators.LOCATION_SUBMIT)
        self.click(AdPlanLocators.CLOSE_LOCATION)

        # возраст
        self.click(AdPlanLocators.toggle("react-collapsed-toggle-:r12:"))
        self.click(AdPlanLocators.AGE_SELECTOR)
        self.click(AdPlanLocators.AGE_OPTION)
        self.click(AdPlanLocators.AGE_DROPDOWN)
        self.click(AdPlanLocators.AGE_POPUP_OPTION)

        # секция 2
        self.click(AdPlanLocators.SECTION2_TOGGLE)
        self.click(AdPlanLocators.SECTION2_ICON)
        self.click(AdPlanLocators.SECTION2_TOGGLE)
        self.click(AdPlanLocators.SECTION2_CLICK_SPAN)
        self.click(AdPlanLocators.SECTION2_POPUP_BUTTON)

        # секция 3
        self.click(AdPlanLocators.SECTION3_TOGGLE)
        self.click(AdPlanLocators.SECTION3_ITEM)
        self.click(AdPlanLocators.SECTION3_OPTION)
        self.click(AdPlanLocators.SECTION3_POPUP_BUTTON)

        self.test_more_group()
        self.click(AdPlanLocators.FOOTER_SUBMIT)

    def input_rich_text(self, locator, text):
        elem = self.wait().until(EC.element_to_be_clickable(locator))
        elem.click()
        elem.send_keys(text)
        self.wait().until(lambda drv:
                          drv.find_element(*locator).get_attribute("textContent").strip() == text
                          )

    def ending(self, logo_path, example_path, paths, title, short_description, long_description):
        self.click(EndingLocators.CHANGE_IMAGE_BUTTON)
        self.find(EndingLocators.FILE_INPUT).send_keys(logo_path)
        self.focus(EndingLocators.ITEM_LIST_ITEM)
        self.click(EndingLocators.ITEM_LIST_ITEM)
        self.wait().until(EC.presence_of_element_located(EndingLocators.APP_LOGO_IMAGE))

        self.input_rich_text(EndingLocators.TITLE_FIELD, title)
        self.input_rich_text(EndingLocators.SHORT_DESC_FIELD, short_description)
        self.input_rich_text(EndingLocators.LONG_DESC_FIELD, long_description)

        self.find(EndingLocators.EXAMPLE_UPLOAD_INPUT).send_keys(example_path)

        self.click(EndingLocators.BUTTON_8)
        self.click(EndingLocators.BUTTON_22)

        self.wait().until(EC.element_to_be_clickable(EndingLocators.WAIT_BUTTON))

        self.click(EndingLocators.MULTI_OPTIONS_BUTTON)
        self.click(EndingLocators.POPUP_DIV1)

        self.click(EndingLocators.ATTACHMENTS_MODE_SELECT_BUTTON)
        self.click(EndingLocators.POPUP_DIV2)

        for el in paths:
            self.click(EndingLocators.UPLOAD_MEDIA_BUTTON)
            self.find(EndingLocators.FILE_INPUT).send_keys(el)
            self.focus(EndingLocators.ITEM_LIST_ITEM)
            self.click(EndingLocators.ITEM_LIST_ITEM)

        self.click(EndingLocators.PRIMARY_SUBMIT)

    def delete(self, url):
        self.new_url(url)
        self.focus(EndingLocators.ACTIONS_BUTTON)
        self.click(EndingLocators.DELETE_OPTION)
