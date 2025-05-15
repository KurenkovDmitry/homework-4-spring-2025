from hw.code.ui.locators.catalog_locators import CatalogAndCommerceLocators
from hw.code.ui.pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CommerceCenterPage(BasePage):
    url = 'https://ads.vk.com/hq/ecomm/catalogs'

    def find_create_catalog_button(self):
        return self.find(CatalogAndCommerceLocators.CREATE_CATALOG_BUTTON, timeout=10)

    def find_tutorial_moodal(self):
        return self.find(CatalogAndCommerceLocators.CLOSE_TUTORIAL_BUTTON)
    
    def click_close_tutorial_modal(self):
        self.find(CatalogAndCommerceLocators.CLOSE_TUTORIAL_BUTTON, timeout=10)
        self.click(CatalogAndCommerceLocators.CLOSE_TUTORIAL_BUTTON)

    def click_create_catalog_button(self):
        self.find(CatalogAndCommerceLocators.CREATE_CATALOG_BUTTON, timeout=10)
        self.click(CatalogAndCommerceLocators.CREATE_CATALOG_BUTTON)

    def find_new_catalog_header(self):
        return self.exists(CatalogAndCommerceLocators.NEW_CATALOG_HEADER, timeout=10)
    
    def fill_field_catalog_name(self, name):
        self.find(CatalogAndCommerceLocators.CATALOG_NAME_INPUT).send_keys(name)
        self.clear_field(CatalogAndCommerceLocators.CATALOG_NAME_INPUT)
        self.input_text(CatalogAndCommerceLocators.CATALOG_NAME_INPUT, name)

    def find_required_field_name_alert(self):
        return self.exists(CatalogAndCommerceLocators.REQUIRED_FIELD_NAME_ALERT)
    
    def click_manual_option(self):
        self.find(CatalogAndCommerceLocators.MANUAL_OPTION, timeout=10)
        self.click(CatalogAndCommerceLocators.MANUAL_OPTION)

    def find_feed_input(self):
        return self.exists(CatalogAndCommerceLocators.FEED_INPUT, timeout=10)
    
    def upload_feed_file(self, file_path):
        self.find(CatalogAndCommerceLocators.FEED_INPUT).send_keys(file_path)
    
    def click_submit_create_button(self):
        self.find(CatalogAndCommerceLocators.SUBMIT_BUTTON, timeout=10)
        self.click(CatalogAndCommerceLocators.SUBMIT_BUTTON)

    def find_required_field_feed_alert(self):
        return self.exists(CatalogAndCommerceLocators.FIELD_ERROR_ALERT, timeout=10)
    
    def click_cancel_create_button(self):
        self.find(CatalogAndCommerceLocators.CANCEL_BUTTON, timeout=10)
        self.click(CatalogAndCommerceLocators.CANCEL_BUTTON)
        self.wait(5).until(EC.invisibility_of_element_located(CatalogAndCommerceLocators.NEW_CATALOG_HEADER))

    # товары добавляются очень долго, поэтому поставлен большой таймаут
    def find_table_headers(self):
        return self.exists(CatalogAndCommerceLocators.TABLE_HEADERS, timeout=1000)
    
    def delete_catalog_if_exists(self):
        self.open_and_wait()
        if self.exists(CatalogAndCommerceLocators.TABLE_HEADERS):
            self.delete_catalog()
        else:
            self.open_and_wait()

    def delete_catalog(self):
        self.open_and_wait()
        while True:
            catalog_items = self.find_elements(CatalogAndCommerceLocators.CATALOG_ITEMS)
            if not catalog_items:
                break
            for item in catalog_items:
                item.click()
                self.click_settings_button()
                self.click_delete_catalog_button()
                WebDriverWait(self.driver, 5).until(
                    EC.invisibility_of_element_located(CatalogAndCommerceLocators.SETTINGS_HEADER)
                )
                break

    def find_catalog_items(self):
        return self.exists(CatalogAndCommerceLocators.CATALOG_ITEMS, timeout=10)

    def click_settings_button(self):
        self.find(CatalogAndCommerceLocators.SETTINGS_BUTTON, timeout=10)
        self.click(CatalogAndCommerceLocators.SETTINGS_BUTTON) 

    def click_delete_catalog_button(self):
        self.find(CatalogAndCommerceLocators.DELETE_CATALOG_BUTTON, timeout=10)
        self.click(CatalogAndCommerceLocators.DELETE_CATALOG_BUTTON)
        self.find(CatalogAndCommerceLocators.REMOVE_BUTTON, timeout=10)
        self.click(CatalogAndCommerceLocators.REMOVE_BUTTON)

    # иногда бывает задержка в создании каталога
    def search_catalog(self, name):
        self.find(CatalogAndCommerceLocators.SEARCH_INPUT, timeout=20)
        self.input_text(CatalogAndCommerceLocators.SEARCH_INPUT, name)

    def create_catalog(self,file_path, name="Каталог"):
        self.open_and_wait()
        self.click_create_catalog_button()
        self.find_new_catalog_header()
        self.click_manual_option()
        self.upload_feed_file(file_path)
        self.fill_field_catalog_name(name)
        self.click_submit_create_button()
        # ждем, пока уберется окно создания
        self.wait(5).until(EC.invisibility_of_element_located(CatalogAndCommerceLocators.NEW_CATALOG_HEADER))
        self.open_and_wait()
        self.find_table_headers()

    def wait_active_catalog(self):
        return self.exists(CatalogAndCommerceLocators.STATUS_ACTIVE, timeout=1000)

    def find_nothing_found_header(self):
        return self.exists(CatalogAndCommerceLocators.NOTHING_FOUND_HEADER, timeout=10)
    
    def click_catalog_item(self):
        self.wait(10).until(EC.presence_of_element_located(CatalogAndCommerceLocators.CATALOG_ITEMS))
        catalog_items = self.find_elements(CatalogAndCommerceLocators.CATALOG_ITEMS)
        for item in catalog_items:
                item.click()
                break
    
    def find_items_table(self):
        self.find(CatalogAndCommerceLocators.ITEMS_TABLE, timeout=1000)
        return self.exists(CatalogAndCommerceLocators.ITEMS_TABLE, timeout=10)
    
    def search_goods(self, name):
        self.find(CatalogAndCommerceLocators.SEARCH_INPUT, timeout=10)
        self.input_text(CatalogAndCommerceLocators.SEARCH_INPUT, name)

    def click_add_goods_button(self):
        self.find(CatalogAndCommerceLocators.ADD_GOODS_BUTTON, timeout=10)
        self.click(CatalogAndCommerceLocators.ADD_GOODS_BUTTON)

    def find_settings_panel_header(self):
        return self.exists(CatalogAndCommerceLocators.SETTINGS_PANEL_HEADER, timeout=10)
    
    def click_cancel_add_goods_button(self):
        self.find(CatalogAndCommerceLocators.CANCEL_ADD_GOODS_BUTTON, timeout=10)
        self.click(CatalogAndCommerceLocators.CANCEL_ADD_GOODS_BUTTON)
        self.wait(5).until(EC.invisibility_of_element_located(CatalogAndCommerceLocators.SETTINGS_PANEL_HEADER))

    def click_continue_add_goods_button(self):
        self.find(CatalogAndCommerceLocators.CONTINUE_ADD_GOODS_BUTTON, timeout=10)
        self.click(CatalogAndCommerceLocators.CONTINUE_ADD_GOODS_BUTTON)
        self.wait(5).until(EC.invisibility_of_element_located(CatalogAndCommerceLocators.SETTINGS_PANEL_HEADER))

    def click_current_catalog_button(self):
        self.find(CatalogAndCommerceLocators.CURRENT_CATALOG_BUTTON, timeout=10)
        self.click(CatalogAndCommerceLocators.CURRENT_CATALOG_BUTTON)

    def click_catalog_item_by_name(self, name):
        catalog_item_locator = (By.XPATH, CatalogAndCommerceLocators.CATALOG_ITEM_BY_NAME[1].format(name=name))
        self.find(catalog_item_locator, timeout=10)
        self.click(catalog_item_locator)

    def get_catalog_name(self):
        catalog_name_element = self.find(CatalogAndCommerceLocators.CATALOG_NAME, timeout=10)
        return catalog_name_element.text
    
    def click_groups_tab(self):
        self.find(CatalogAndCommerceLocators.GROUPS_TAB, timeout=10)
        self.click(CatalogAndCommerceLocators.GROUPS_TAB)

    def find_create_group_button(self):
        return self.exists(CatalogAndCommerceLocators.CREATE_GROUP_BUTTON, timeout=10)

    def click_create_group_button(self):
        self.find(CatalogAndCommerceLocators.CREATE_GROUP_BUTTON, timeout=10)
        self.click(CatalogAndCommerceLocators.CREATE_GROUP_BUTTON)

    def find_use_filters_button(self):
        return self.exists(CatalogAndCommerceLocators.USE_FILTERS_BUTTON, timeout=10)
    
    def find_choose_goods_manually_button(self):
        return self.exists(CatalogAndCommerceLocators.CHOOSE_GOODS_MANUALLY_BUTTON, timeout=10)
    
    def click_use_filters_button(self):
        self.find(CatalogAndCommerceLocators.USE_FILTERS_BUTTON, timeout=10)
        self.click(CatalogAndCommerceLocators.USE_FILTERS_BUTTON)
        self.find(CatalogAndCommerceLocators.NEW_GROUP_HEADER, timeout=10)

    def click_choose_goods_manually_button(self):
        self.find(CatalogAndCommerceLocators.CHOOSE_GOODS_MANUALLY_BUTTON, timeout=10)
        self.click(CatalogAndCommerceLocators.CHOOSE_GOODS_MANUALLY_BUTTON)

    def find_new_group_header(self):
        return self.exists(CatalogAndCommerceLocators.NEW_GROUP_HEADER, timeout=10)
    
    def click_add_filter_button(self):
        self.find(CatalogAndCommerceLocators.ADD_FILTER_BUTTON, timeout=10)
        self.click(CatalogAndCommerceLocators.ADD_FILTER_BUTTON)

    def count_filter_condition(self):
        return self.exists(CatalogAndCommerceLocators.FILTER_CONDITION, timeout=10)
    
    def find_field_group_name(self):
        return self.exists(CatalogAndCommerceLocators.GROUP_NAME_INPUT, timeout=10)
    
    def get_group_name(self):
        group_name_element = self.find(CatalogAndCommerceLocators.GROUP_NAME_INPUT, timeout=10)
        return group_name_element.get_attribute("value")

    def click_save_button(self):
        self.find(CatalogAndCommerceLocators.SAVE_BUTTON, timeout=10)
        self.click(CatalogAndCommerceLocators.SAVE_BUTTON)

    def click_cancel_button(self):
        self.find(CatalogAndCommerceLocators.CANCEL_BUTTON, timeout=10)
        self.click(CatalogAndCommerceLocators.CANCEL_BUTTON)
        self.wait(5).until(EC.invisibility_of_element_located(CatalogAndCommerceLocators.NEW_GROUP_HEADER))

    def find_group_item_by_name(self, name):
        group_item_locator = (By.XPATH, CatalogAndCommerceLocators.GROUP_ITEM_BY_NAME[1].format(name=name))
        return self.exists(group_item_locator, timeout=10)
    
    def click_more_button(self):
        self.find(CatalogAndCommerceLocators.MORE_BUTTON, timeout=10)
        self.click(CatalogAndCommerceLocators.MORE_BUTTON)
    
    def click_group_item_by_name(self, name):
        group_item_locator = (By.XPATH, CatalogAndCommerceLocators.GROUP_ITEM_BY_NAME_CONTAINS[1].format(name=name))
        self.find(group_item_locator, timeout=10)
        self.click(group_item_locator)


    def delete_group(self, name):
        if not self.exists((By.XPATH, CatalogAndCommerceLocators.GROUP_ITEM_BY_NAME_CONTAINS[1].format(name=name)), timeout=10):
            return
        self.click_group_item_by_name(name)
        self.click_more_button()
        delete_button_locator = (By.XPATH, CatalogAndCommerceLocators.DELETE_GROUP_BUTTON[1].format(name=name))
        self.find(delete_button_locator, timeout=10)
        self.click(delete_button_locator)
        self.find(CatalogAndCommerceLocators.CONFIRM_DELETE_BUTTON, timeout=10)
        self.click(CatalogAndCommerceLocators.CONFIRM_DELETE_BUTTON)

    def find_search_goods_input(self):
        return self.exists(CatalogAndCommerceLocators.SEARCH_GOODS_INPUT, timeout=10)

    def search_goods_manually(self, name):
        search_input = self.wait(10).until(EC.element_to_be_clickable(CatalogAndCommerceLocators.SEARCH_GOODS_INPUT))
        search_input.clear()
        search_input.send_keys(name)

    
    def find_nothing_found_message_goods(self):
        return self.exists(CatalogAndCommerceLocators.NOTHING_FOUND_MESSAGE, timeout=10)
    
    def add_goods(self):
        self.click_add_manually_goods_button()
        self.fill_add_field()
        self.click_submit_manually_add_goods_button()

    def click_add_manually_goods_button(self):
        self.find(CatalogAndCommerceLocators.ADD_LIST_BUTTON, timeout=10)
        self.click(CatalogAndCommerceLocators.ADD_LIST_BUTTON)

    def fill_add_field(self):
        self.find(CatalogAndCommerceLocators.TEXTAREA_FIELD, timeout=10)
        self.input_text(CatalogAndCommerceLocators.TEXTAREA_FIELD, "0")

    def click_submit_manually_add_goods_button(self):
        self.find(CatalogAndCommerceLocators.ADD_TO_GROUP_BUTTON, timeout=10)
        self.click(CatalogAndCommerceLocators.ADD_TO_GROUP_BUTTON)

    def click_selected_goods_tab(self):
        self.find(CatalogAndCommerceLocators.SELECTED_GOODS_TAB, timeout=10)
        self.click(CatalogAndCommerceLocators.SELECTED_GOODS_TAB)

    def fill_field_group_name(self, name):
        self.find(CatalogAndCommerceLocators.GROUP_NAME_INPUT, timeout=10).send_keys(name)
        self.clear_field(CatalogAndCommerceLocators.GROUP_NAME_INPUT)
        self.input_text(CatalogAndCommerceLocators.GROUP_NAME_INPUT, name)

    def search_group(self, name):
        self.find(CatalogAndCommerceLocators.SEARCH_INPUT_IN_GROUPS, timeout=10)
        self.input_text(CatalogAndCommerceLocators.SEARCH_INPUT_IN_GROUPS, name)
        return self.exists(CatalogAndCommerceLocators.GROUP_IN_LIST_GROUP, timeout=10)
    
    def wait_for_group_in_list_group(self):
        self.wait(20).until(EC.invisibility_of_element_located(CatalogAndCommerceLocators.NEW_GROUP_HEADER))
        self.find(CatalogAndCommerceLocators.GROUP_IN_LIST_GROUP, timeout=10)

    def click_edit_group_tab(self):
        self.find(CatalogAndCommerceLocators.EDIT_GROUP_BUTTON, timeout=10)
        self.click(CatalogAndCommerceLocators.EDIT_GROUP_BUTTON)

    def click_created_group_tab(self):
        self.find(CatalogAndCommerceLocators.CREATED_GROUP_BUTTON, timeout=10)
        self.click(CatalogAndCommerceLocators.CREATED_GROUP_BUTTON)

    def find_edit_group_header(self):
        return self.find(CatalogAndCommerceLocators.EDIT_GROUP_HEADER, timeout=10)
    
    def find_edited_group_name(self, name):
        return self.find((By.XPATH, CatalogAndCommerceLocators.EDITED_GROUP_NAME[1].format(name=name)), timeout=10)

    def click_download_history_tab(self):
        self.find(CatalogAndCommerceLocators.DOWNLOAD_HISTORY_TAB, timeout=10)
        self.click(CatalogAndCommerceLocators.DOWNLOAD_HISTORY_TAB)

    def open_modal(self):
        self.click_refresh_btn()
        return self.find_modal_header()

    def click_refresh_btn(self):
        self.find(CatalogAndCommerceLocators.REFRESH_FILE_BUTTON, timeout=10)
        self.click(CatalogAndCommerceLocators.REFRESH_FILE_BUTTON)

    def find_modal_header(self):
        return self.exists(CatalogAndCommerceLocators.CATALOG_DOWNLOAD_HEADER, timeout=10)    


    