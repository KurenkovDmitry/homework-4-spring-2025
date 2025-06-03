import os
import pytest

class TestCommerceCenter:
    @pytest.fixture(autouse=True)
    def setup_open_catalog(self, catalog_page):
        catalog_page.open_and_wait()

    def test_open_catalog_create_form(self, catalog_page):
        assert catalog_page.find_create_catalog_button()
        catalog_page.close_tutorial_modal()
        catalog_page.click_create_catalog_button()
        catalog_page.find_new_catalog()

    def test_search_catalog(self, catalog_page):
        catalog_page.create_catalog()
        catalog_page.open_and_wait()
        catalog_page.search_catalog("Каталог")
        catalog_page.find_table()

    def test_search_nonexistent_catalog(self, catalog_page):
        catalog_page.create_catalog()
        catalog_page.search_catalog("QAQAQA")
        catalog_page.find_nothing_found_message()

    def test_create_name_catalog(self, catalog_page):
        catalog_page.find_create_catalog_button()

        catalog_page.click_create_catalog_button()
        catalog_page.find_new_catalog()

        catalog_page.fill_field_catalog_name("Каталог")
        assert not catalog_page.find_required_field_name_alert()

    def test_create_catalog_manually_option(self, catalog_page):
        catalog_page.click_create_catalog_button()
        catalog_page.find_new_catalog()
        catalog_page.click_manual_option()
        catalog_page.find_feed_input()

    def test_create_continue_button_with_empty_field(self, catalog_page):
        catalog_page.click_create_catalog_button()
        catalog_page.find_new_catalog()
        catalog_page.click_manual_option()
        catalog_page.click_submit_create_button()
        catalog_page.find_required_field_feed_alert()

    def test_create_continue_button(self, catalog_page):
        catalog_page.click_create_catalog_button()
        catalog_page.find_new_catalog()
        catalog_page.click_manual_option()
        catalog_page.upload_feed_file()
        catalog_page.click_submit_create_button()
        catalog_page.open_and_wait()
        catalog_page.find_table()

    def test_create_cancel_button(self, catalog_page):
        catalog_page.click_create_catalog_button()
        catalog_page.find_new_catalog()
        catalog_page.click_cancel_create_button()
        assert not catalog_page.find_new_catalog()

class TestCatalogGoods():

    def test_goods_search(self, catalog_page):
        catalog_page.click_catalog_item()
        catalog_page.find_items_table()
        catalog_page.search_goods("Худи")
        catalog_page.find_items_table()

    def test_goods_add_button(self, catalog_page):
        catalog_page.click_catalog_item()
        catalog_page.click_add_goods_button()
        catalog_page.find_settings_panel()

    def test_goods_add_cancel_button(self, catalog_page):
        catalog_page.click_catalog_item()
        catalog_page.click_add_goods_button()
        catalog_page.find_settings_panel()
        catalog_page.click_cancel_add_goods_button()
        assert not catalog_page.find_settings_panel()

    def test_goods_choose_goods(self, catalog_page):
        catalog_page.click_catalog_item()
        catalog_page.click_current_catalog_button()
        catalog_page.click_catalog_item_by_name("Каталог")
        current_catalog_name = catalog_page.get_catalog_name()
        assert "Каталог" in current_catalog_name

class TestCatalogGroup():

    def test_group_create_button(self, catalog_page):
        catalog_page.create_catalog()
        catalog_page.click_catalog_item()
        catalog_page.click_groups_tab()
        catalog_page.find_create_group_button()

        catalog_page.click_create_group_button()
        catalog_page.find_use_filters_button()
        catalog_page.find_choose_goods_manually()

    def test_group_use_filters(self, catalog_page):
        catalog_page.create_catalog()
        catalog_page.click_catalog_item()
        catalog_page.click_groups_tab()
        catalog_page.find_create_group_button()

        catalog_page.click_create_group_button()
        catalog_page.find_use_filters_button()
        catalog_page.click_use_filters_button()
        catalog_page.find_new_group_block()

    def test_group_add_filter(self, catalog_page):
        catalog_page.create_catalog()
        catalog_page.click_catalog_item()
        catalog_page.click_groups_tab()
        catalog_page.find_create_group_button()

        catalog_page.click_create_group_button()
        catalog_page.find_use_filters_button()

        catalog_page.click_use_filters_button()
        catalog_page.click_add_filter_button()
        assert catalog_page.count_filter_condition()

    def test_group_save_filter_button(self, catalog_page):
        catalog_page.create_catalog()
        catalog_page.click_catalog_item()
        catalog_page.click_groups_tab()
        catalog_page.find_create_group_button()

        catalog_page.click_create_group_button()
        catalog_page.find_use_filters_button()

        catalog_page.click_use_filters_button()
        catalog_page.find_new_group_block()
        catalog_page.find_field_group_name()

        name = catalog_page.get_group_name()
        catalog_page.click_save_button()
        catalog_page.find_group_item_by_name(name)

    
    def test_group_cancel_filter_button(self, catalog_page):
        catalog_page.create_catalog()
        catalog_page.click_catalog_item()
        catalog_page.click_groups_tab()
        catalog_page.delete_group("Группа")

        catalog_page.find_create_group_button()

        catalog_page.click_create_group_button()
        catalog_page.find_use_filters_button()

        catalog_page.click_use_filters_button()
        catalog_page.click_cancel_button()
        assert not catalog_page.find_new_group_block()
    

    def test_group_manually_add_button(self, catalog_page):
        catalog_page.create_catalog()
        catalog_page.click_catalog_item()
        catalog_page.click_groups_tab()
        catalog_page.delete_group("Группа")
        catalog_page.find_create_group_button()
        catalog_page.click_create_group_button()

        catalog_page.find_choose_goods_manually()

        catalog_page.click_choose_goods_manually_button()
        catalog_page.find_new_group_block()


    def test_group_manually_add_search(self, catalog_page):
        catalog_page.create_catalog()
        catalog_page.click_catalog_item()
        catalog_page.click_groups_tab()
        catalog_page.delete_group("Группа")
        catalog_page.find_create_group_button()
        catalog_page.click_create_group_button()
        catalog_page.find_choose_goods_manually()

        catalog_page.click_choose_goods_manually_button()
        catalog_page.find_new_group_block()
        catalog_page.find_search_goods_input()
        catalog_page.search_goods_manually("Худи")
        catalog_page.find_items_table()


    def test_group_manually_add_search_nonexistent_goods(self, catalog_page):
        catalog_page.create_catalog()
        catalog_page.click_catalog_item()
        catalog_page.click_groups_tab()
        catalog_page.delete_group("Группа")
        catalog_page.find_create_group_button()
        catalog_page.click_create_group_button()
        catalog_page.find_choose_goods_manually()

        catalog_page.click_choose_goods_manually_button()
        catalog_page.search_goods_manually("QAQAQA")
        catalog_page.find_nothing_found_message_goods()

    def test_group_manually_add_add_button(self, catalog_page):
        catalog_page.create_catalog()
        catalog_page.click_catalog_item()
        catalog_page.click_groups_tab()
        catalog_page.delete_group("Группа")
        catalog_page.find_create_group_button()
        catalog_page.click_create_group_button()
        catalog_page.find_choose_goods_manually()

        catalog_page.click_choose_goods_manually_button()
        catalog_page.add_goods()
        catalog_page.click_selected_goods_tab()
        catalog_page.find_items_table()

    def test_group_manually_add_save_button(self, catalog_page):
        catalog_page.create_catalog()
        catalog_page.click_catalog_item()
        catalog_page.click_groups_tab()
        catalog_page.delete_group("Группа")
        catalog_page.find_create_group_button()
        catalog_page.click_create_group_button()
        catalog_page.find_choose_goods_manually()

        catalog_page.click_choose_goods_manually_button()
        catalog_page.add_goods()
        catalog_page.click_save_button()
        catalog_page.wait_for_group_in_list_group()
        catalog_page.find_items_table()

    def test_group_manually_add_cancel_button(self, catalog_page):
        catalog_page.create_catalog()
        catalog_page.click_catalog_item()
        catalog_page.click_groups_tab()
        catalog_page.delete_group("Группа")
        catalog_page.find_create_group_button()
        catalog_page.click_create_group_button()
        catalog_page.find_choose_goods_manually()

        catalog_page.click_choose_goods_manually_button()
        catalog_page.click_cancel_button()
        assert not catalog_page.find_new_group_block()

    def test_group_list_search(self, catalog_page):
        catalog_page.create_catalog()
        catalog_page.click_catalog_item()
        catalog_page.click_groups_tab()

        assert catalog_page.search_group("Все")

    def test_group_edit(self, catalog_page):
        catalog_page.create_catalog()
        catalog_page.click_catalog_item()
        catalog_page.click_groups_tab()

        catalog_page.find_create_group_button()
        catalog_page.click_create_group_button()
        catalog_page.find_choose_goods_manually()

        catalog_page.click_choose_goods_manually_button()
        catalog_page.add_goods()
        catalog_page.click_save_button()
        catalog_page.wait_for_group_in_list_group()

        catalog_page.click_created_group_tab()
        catalog_page.click_edit_group_tab()

        catalog_page.find_edit_group_header()

        catalog_page.fill_field_group_name('Тестовая группа')
        catalog_page.click_save_button()
        catalog_page.find_edited_group_name('Тестовая группа')

class TestCatalogDownload():
    @pytest.fixture(autouse=True)
    def setup_open_catalog(self, catalog_page):
        catalog_page.open_and_wait()

    def test_download_history(self, catalog_page):
        catalog_page.create_catalog()
        catalog_page.click_catalog_item()
        catalog_page.click_download_history_tab()
        assert catalog_page.open_modal()


class TestDeleteCatalog():
    @pytest.fixture(autouse=True)
    def setup_open_catalog(self, catalog_page):
        catalog_page.open_and_wait()

    def test_delete_catalog(self, catalog_page):
        catalog_page.delete_catalog()
        assert not catalog_page.find_catalog_items()
