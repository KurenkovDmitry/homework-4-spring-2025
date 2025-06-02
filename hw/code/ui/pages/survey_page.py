import time

from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from ui.locators.survey_locators import SurveyLocators


class SurveyPage(BasePage):
    url = 'https://ads.vk.com/hq/leadads/surveys'

    def create_survey(self):
        # Клик по кнопке создания опроса и ожидание модального окна
        self.click(SurveyLocators.CREATE_SURVEY_BUTTON)
        self.wait().until(EC.presence_of_element_located(SurveyLocators.MODAL_CONTENT))

    def set_name(self, name):
        # Ожидание видимости и ввод текста в поле "Название"
        name_input = self.wait().until(EC.visibility_of_element_located(SurveyLocators.NAME_INPUT))
        name_input.clear()  # Очистка поля перед вводом
        name_input.send_keys(name)

    def set_company(self, company):
        # Ожидание видимости и ввод текста в поле "Название компании"
        company_input = self.wait().until(EC.visibility_of_element_located(SurveyLocators.COMPANY_INPUT))
        company_input.clear()
        company_input.send_keys(company)

    def set_title(self, title):
        # Ожидание видимости и ввод текста в поле "Заголовок опроса"
        title_input = self.wait().until(EC.visibility_of_element_located(SurveyLocators.TITLE_INPUT))
        title_input.clear()
        title_input.send_keys(title)

    def set_description(self, description):
        # Ожидание видимости и ввод текста в поле "Описание опроса"
        description_textarea = self.wait().until(EC.visibility_of_element_located(SurveyLocators.DESCRIPTION_TEXTAREA))
        description_textarea.clear()
        description_textarea.send_keys(description)

    def select_style(self, style_id):
        # Выбор стиля
        self.click(SurveyLocators.STYLE_DIV(style_id))

    def upload_logo(self, logo_path):
        self.click(SurveyLocators.SET_GLOBAL_IMAGE)
        self.find(SurveyLocators.FILE_INPUT).send_keys(logo_path)
        self.wait().until(EC.presence_of_element_located(SurveyLocators.ITEM_LIST_ITEM))
        self.focus(SurveyLocators.ITEM_LIST_ITEM)
        self.click(SurveyLocators.ITEM_LIST_ITEM)
        self.wait().until(EC.presence_of_element_located(SurveyLocators.APP_LOGO))

    def submit_form(self):
        # Отправка формы
        self.click(SurveyLocators.SUBMIT_BUTTON)

    def single_choice_question(self, options, sample_answer=False):
        self.input_text(SurveyLocators.YES_INPUT, options[0])
        self.input_text(SurveyLocators.NO_INPUT, options[1])
        if len(options) > 2:
            self.click(SurveyLocators.ADD_ANSWER_BUTTON)
            self.find_elements(SurveyLocators.REMOVE_ANSWER_BUTTON)[2].click()
            self.click(SurveyLocators.ADD_ANSWER_BUTTON)
            self.input_text(SurveyLocators.NEUTRAL_INPUT, options[2])

        if sample_answer:
            self.click(SurveyLocators.TEMPLATE_ANSWER_BUTTON)
            self.wait().until(
                EC.visibility_of_element_located(SurveyLocators.TEMPLATE_ANSWER_MODAL)
            )
            self.click(SurveyLocators.TEMPLATE_OPTION)

    def multiple_choice_question(self, options):
        self.click(SurveyLocators.MULTIPLE_CHOICE_OPTION)
        self.input_text(SurveyLocators.YES_INPUT, options[0])
        self.input_text(SurveyLocators.NO_INPUT, options[1])
        if len(options) > 2:
            self.click(SurveyLocators.ADD_ANSWER_BUTTON)
            self.input_text(SurveyLocators.NEUTRAL_INPUT, options[2])

    def scale_question(self, min_label, max_label, test_range=False):
        self.click(SurveyLocators.SCALE_OPTION)
        self.input_text(SurveyLocators.SCALE_MIN_INPUT, min_label)
        self.input_text(SurveyLocators.SCALE_MAX_INPUT, max_label)

        if test_range:
            self.click(SurveyLocators.SCALE_RANGE)
            self.wait().until(
                EC.visibility_of_element_located(SurveyLocators.MODAL)
            )
            self.click(SurveyLocators.RANGE_OPTION)

    def text_question(self):
        self.click(SurveyLocators.TEXT_OPTION)

    def configure_first_question(self, question_type, text, options=None, min_label=None, max_label=None, sample_answer=False):
        textarea = SurveyLocators.QUESTION_1_TEXTAREA
        self.input_text(textarea, text)
        if question_type == 'single_choice' and options:
            self.single_choice_question(options, sample_answer)
        if question_type == 'multiple_choice' and options:
            self.click(SurveyLocators.TYPE)
            self.wait().until(
                EC.visibility_of_element_located(SurveyLocators.MODAL)
            )
            self.multiple_choice_question(options)
        elif question_type == 'scale' and min_label and max_label:
            self.click(SurveyLocators.TYPE)
            self.wait().until(
                EC.visibility_of_element_located(SurveyLocators.MODAL)
            )
            self.scale_question(min_label, max_label, test_range=True)
        elif question_type == 'text':
            self.click(SurveyLocators.TYPE)
            self.wait().until(
                EC.visibility_of_element_located(SurveyLocators.MODAL)
            )
            self.text_question()

    def delete_second_question(self):
        self.find_elements(SurveyLocators.REMOVE_QUESTION_BUTTON)[1].click()

    def add_second_question(self, question_type, text, options=None, min_label=None, max_label=None, delete=False):
        self.click(SurveyLocators.ADD_QUESTION_BUTTON)
        textarea = SurveyLocators.QUESTION_2_TEXTAREA
        self.input_text(textarea, text)
        if question_type == 'single_choice' and options:
            self.single_choice_question(options)
        if question_type == 'multiple_choice' and options:
            self.find_elements(SurveyLocators.TYPE)[1].click()
            self.wait().until(
                EC.visibility_of_element_located(SurveyLocators.MODAL)
            )
            self.multiple_choice_question(options)
        elif question_type == 'scale' and min_label and max_label:
            self.find_elements(SurveyLocators.TYPE)[1].click()
            self.wait().until(
                EC.visibility_of_element_located(SurveyLocators.MODAL)
            )
            self.scale_question(min_label, max_label)
        elif question_type == 'text':
            self.find_elements(SurveyLocators.TYPE)[1].click()
            self.wait().until(
                EC.visibility_of_element_located(SurveyLocators.MODAL)
            )
            self.text_question()

        if delete:
            self.delete_second_question()

    def add_stop_screen(self):
        self.click(SurveyLocators.ADD_STOP_SCREEN_BUTTON)

    def remove_stop_screen(self):
        self.click(SurveyLocators.REMOVE_STOP_SCREEN_BUTTON)

    def set_trigger_question(self):
        self.click(SurveyLocators.TRIGGER_QUESTION)
        self.click(SurveyLocators.TRIGGER_QUESTION_OPTION)

    def set_trigger_criteria(self, option):
        self.click(SurveyLocators.TRIGGER_CRITERIA)
        if option == 1:
            self.click(SurveyLocators.TRIGGER_OPTION_1)
        elif option == 2:
            self.click(SurveyLocators.TRIGGER_OPTION_2)

    def set_thank_you_title(self, title):
        self.input_text(SurveyLocators.THANK_YOU_TITLE, title)

    def set_thank_you_description(self, description):
        self.input_text(SurveyLocators.THANK_YOU_DESCRIPTION, description)

    def set_ending_title(self, title):
        self.input_text(SurveyLocators.ENDING_TITLE_INPUT, title)

    def set_ending_description(self, description):
        self.input_text(SurveyLocators.ENDING_DESCRIPTION_INPUT, description)

    def add_link(self, link):
        self.click(SurveyLocators.ADD_LINK_BUTTON)
        self.input_text(SurveyLocators.LINK_INPUT, link)

    def save_ending(self):
        self.click(SurveyLocators.SAVE_ENDING_BUTTON)

    def open_edit_modal(self):
        self.focus(SurveyLocators.NAV_EDIT_BUTTON)
        self.click(SurveyLocators.NAV_EDIT_BUTTON)
        self.wait().until(EC.presence_of_element_located(SurveyLocators.MODAL_CONTENT))

    def clear_field(self, locator):
        field = self.find(locator)
        field.send_keys('\b' * 100)

    def get_validation_errors(self):
        container = self.find(SurveyLocators.FORM_CONTAINER)
        return container.find_elements(*SurveyLocators.VALIDATION_ERROR_FIELDS)

    def close_modal(self):
        self.click(SurveyLocators.MODAL_OVERLAY)

    def confirm_close_without_saving(self):
        modal = self.find(SurveyLocators.CLOSE_EDITOR_MODAL_TITLE)
        ok_btn = modal.find_element(*SurveyLocators.MODAL_SUBMIT_BUTTON)
        ok_btn.click()

    def archive_survey(self):
        self.focus(SurveyLocators.ARCHIVE_BUTTON)
        self.click(SurveyLocators.ARCHIVE_BUTTON)
        self.click(SurveyLocators.CONFIRM_ARCHIVE_BUTTON)
        self.wait().until(EC.invisibility_of_element_located(SurveyLocators.CONFIRM_ARCHIVE_BUTTON))

    # Helper methods for verification (optional, depending on test needs)
    def is_logo_uploaded(self):
        return self.find(SurveyLocators.APP_LOGO).is_displayed()

    def is_on_questions_page(self):
        return self.find(SurveyLocators.QUESTION_1_TEXTAREA).is_displayed()

    def is_close_confirmation_present(self):
        try:
            self.find(SurveyLocators.CLOSE_EDITOR_MODAL_TITLE, timeout=3)
            return True
        except TimeoutException:
            return False
