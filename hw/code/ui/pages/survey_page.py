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
        # Загружает логотип через файл-инпут и подтверждает выбор изображения
        self.click(SurveyLocators.SET_GLOBAL_IMAGE)
        self.find(SurveyLocators.FILE_INPUT).send_keys(logo_path)
        self.wait().until(EC.presence_of_element_located(SurveyLocators.ITEM_LIST_ITEM))
        self.scroll_into_view(SurveyLocators.ITEM_LIST_ITEM)
        self.click_retry(SurveyLocators.ITEM_LIST_ITEM)
        self.wait().until(EC.presence_of_element_located(SurveyLocators.APP_LOGO))

    def submit_form(self):
        # Отправка формы
        self.click(SurveyLocators.SUBMIT_BUTTON)

    def single_choice_question(self, options, sample_answer=False):
        # Заполняет вариант вопроса с единственным выбором
        # При необходимости добавляет шаблонный ответ
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
        # Заполняет вариант вопроса с множественным выбором
        self.click(SurveyLocators.MULTIPLE_CHOICE_OPTION)
        self.input_text(SurveyLocators.YES_INPUT, options[0])
        self.input_text(SurveyLocators.NO_INPUT, options[1])
        if len(options) > 2:
            self.click(SurveyLocators.ADD_ANSWER_BUTTON)
            self.input_text(SurveyLocators.NEUTRAL_INPUT, options[2])

    def scale_question(self, min_label, max_label, test_range=False):
        # Заполняет шкальный вопрос с метками минимального и максимального значений
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
        # Выбирает тип вопроса "Текст"
        self.click(SurveyLocators.TEXT_OPTION)

    def configure_first_question(self, question_type, text, options=None, min_label=None, max_label=None, sample_answer=False):
        # Конфигурирует первый вопрос, выбирая тип и заполняя содержимое
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
        # Удаляет второй вопрос
        self.find_elements(SurveyLocators.REMOVE_QUESTION_BUTTON)[1].click()

    def add_second_question(self, question_type, text, options=None, min_label=None, max_label=None, delete=False):
        # Добавляет второй вопрос, конфигурирует его и, опционально, удаляет
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

    def duplicate(self, number):
        # Дублирует вопрос по индексу и удаляет его копию
        self.find_elements(SurveyLocators.DUPLICATE_QUESTION_BUTTON)[number].click()
        self.find_elements(SurveyLocators.REMOVE_QUESTION_BUTTON)[number + 1].click()

    def add_rule(self):
        # Добавляет правило показа
        self.click(SurveyLocators.RULE_BUTTON)

    def remove_rule(self):
        # Удаляет правило показа
        self.click(SurveyLocators.RULE_BUTTON)

    def set_rule_criteria(self, amount):
        # Устанавливает критерии для правил показа
        try:
            for i in range(amount):
                self.click(SurveyLocators.RULE_CRITERIA)
                self.find_elements(SurveyLocators.RULE_OPTION)[i].click()
        except Exception as e:
            raise RuntimeError(f"Ошибка при установке rule criteria: {e}")

    def add_stop_screen(self):
        # Добавляет стоп-экран
        self.click(SurveyLocators.ADD_STOP_SCREEN_BUTTON)

    def remove_stop_screen(self):
        # Удаляет стоп-экран
        self.click(SurveyLocators.REMOVE_STOP_SCREEN_BUTTON)

    def set_trigger_criteria(self, amount):
        # Устанавливает критерии для стоп-экрана
        try:
            for i in range(amount):
                self.click(SurveyLocators.TRIGGER_CRITERIA)
                self.find_elements(SurveyLocators.TRIGGER_OPTION)[i].click()
        except Exception as e:
            raise RuntimeError(f"Ошибка при установке trigger criteria: {e}")

    def set_thank_you_title(self, title):
        # Заполняет заголовок экрана благодарности
        self.input_text(SurveyLocators.THANK_YOU_TITLE, title)

    def set_thank_you_description(self, description):
        # Заполняет описание экрана благодарности
        self.input_text(SurveyLocators.THANK_YOU_DESCRIPTION, description)

    def set_ending_title(self, title):
        # Заполняет заголовок завершающего экрана
        self.input_text(SurveyLocators.ENDING_TITLE_INPUT, title)

    def set_ending_description(self, description):
        # Заполняет описание завершающего экрана
        self.input_text(SurveyLocators.ENDING_DESCRIPTION_INPUT, description)

    def add_link(self, link):
        # Добавляет ссылку на завершающем экране
        self.click(SurveyLocators.ADD_LINK_BUTTON)
        self.input_text(SurveyLocators.LINK_INPUT, link)

    def save_ending(self):
        # Сохраняет настройки завершающего экрана
        self.click(SurveyLocators.SAVE_ENDING_BUTTON)

    def open_edit_modal(self):
        # Открывает модальное окно редактирования опроса
        self.focus(SurveyLocators.NAV_EDIT_BUTTON)
        self.click(SurveyLocators.NAV_EDIT_BUTTON)
        self.wait().until(EC.presence_of_element_located(SurveyLocators.MODAL_CONTENT))

    def check_name(self, value):
        # Проверяет, совпадает ли значение поля "Название" с ожидаемым
        return self.get_field_value(SurveyLocators.NAME_INPUT) == value

    def check_answers_v1(self, ans):
        if self.find(SurveyLocators.YES_INPUT).get_attribute('value') != ans[0] or self.find(SurveyLocators.NO_INPUT).get_attribute('value') != ans[1] or self.find(SurveyLocators.NEUTRAL_INPUT).get_attribute('value') != ans[2]:
            return False
        return True

    def check_amount_questions(self, amount):
        question_textareas = self.find_elements(SurveyLocators.QUESTION_1_TEXTAREA)
        return len(question_textareas) == amount

    def check_rule(self):
        return self.find(SurveyLocators.RULE_BUTTON).is_displayed()

    def check_stop_screen(self):
        return self.exists(SurveyLocators.THANK_YOU_TITLE)

    def check_thank_you_title(self, value):
        return self.get_field_value(SurveyLocators.THANK_YOU_TITLE) == value

    def check_ending_title(self, value):
        return self.get_field_value(SurveyLocators.ENDING_TITLE_INPUT) == value

    def check_ending_link(self, value):
        return self.find(SurveyLocators.LINK_INPUT).get_attribute('value') == value

    def close_modal(self):
        # Закрывает модальное окно
        self.click(SurveyLocators.MODAL_OVERLAY)

    def confirm_close_without_saving(self):
        # Подтверждает закрытие модального окна без сохранения
        self.click(SurveyLocators.MODAL_CANCEL_BUTTON)

    def confirm_close_with_saving(self):
        # Подтверждает закрытие модального окна с сохранением
        self.click(SurveyLocators.MODAL_SUBMIT_BUTTON)

    def archive_survey(self):
        # Архивирует опрос и дожидается завершения действия
        self.focus(SurveyLocators.ARCHIVE_BUTTON)
        self.click(SurveyLocators.ARCHIVE_BUTTON)
        self.click(SurveyLocators.CONFIRM_ARCHIVE_BUTTON)
        self.wait().until(EC.invisibility_of_element_located(SurveyLocators.CONFIRM_ARCHIVE_BUTTON))

    def select_archive_category(self):
        # Переключает фильтр списка опросов на "Архив"
        self.click(SurveyLocators.SELECT_CATEGORY_DROPDOWN)
        self.click(SurveyLocators.ARCHIVE_CATEGORY_OPTION)

    def select_active_category(self):
        # Переключает фильтр списка опросов на "Активные"
        self.click(SurveyLocators.SELECT_CATEGORY_DROPDOWN)
        self.click(SurveyLocators.ACTIVE_CATEGORY_OPTION)

    def restore_survey(self, name):
        # Восстанавливает ранее заархивированный опрос
        self.focus(SurveyLocators.RESTORE_ELEMENT_BUTTON)
        self.click(SurveyLocators.RESTORE_ELEMENT_BUTTON)
        self.click(SurveyLocators.RESTORE_ELEMENT_AGREE_BUTTON)
        self.open_and_wait()

    def search_survey(self, name):
        self.click(SurveyLocators.SEARCH_INPUT)
        # Выполняет поиск опроса по имени
        self.input_text(SurveyLocators.SEARCH_INPUT, name)

    def search_survey_clear(self):
        # Очищает строку поиска
        self.find(SurveyLocators.SEARCH_INPUT).send_keys('\b' * 1000)

    def is_logo_uploaded(self):
        # Проверяет, отображается ли загруженный логотип
        return self.find(SurveyLocators.APP_LOGO).is_displayed()

    def is_modal_opened(self):
        # Проверяет, отображается ли модальное окно
        return self.find(SurveyLocators.NAME_INPUT).is_displayed()

    def is_close_confirmation_present(self):
        # Проверяет наличие модального окна подтверждения закрытия редактора
        try:
            self.find(SurveyLocators.CLOSE_EDITOR_MODAL_TITLE_AFTER_EDIT, timeout=3)
            return True
        except Exception as e:
            raise RuntimeError(f"Ошибка при появлении модального окна (edit): {e}")

    def is_element_in_list(self, element_name):
        # Проверяет, отображается ли элемент с указанным названием в списке
        try:
            self.find(SurveyLocators.LIST_ELEMENT(element_name), timeout=3)
            return True
        except Exception as e:
            return False

    def check_errors(self, amount, error, v=1):
        # Проверяет количество отображаемых ошибок валидации на форме
        try:
            if v==1:
                tests = SurveyLocators.VALIDATION_ERROR_FIELDS(error)

                # Находим контейнер формы
                container = self.find(SurveyLocators.FORM_CONTAINER)
            elif v==2:
                tests = SurveyLocators.VALIDATION_ERROR_FIELDS_SPAN(error)

                # Находим контейнер формы
                container = self.find(SurveyLocators.FORM_CONTAINER_2)
            else:
                raise RuntimeError(f"Некорректная версия")

            # Ожидаем, пока в контейнере не появится минимум amount элемента с ошибкой
            self.wait().until(
                lambda driver: len(container.find_elements(*tests)) >= amount
            )

            # Проверяем наличие ошибок
            errs = container.find_elements(*tests)
            return len(errs) >= amount
        except Exception as e:
            return False

    def get_question_text(self, question_number):
        """
        Получает текст вопроса по его номеру.

        Аргументы:
            question_number (int): Номер вопроса, начиная с 1.

        Возвращает:
            str: Текст вопроса.
        """
        question_element = self.find(SurveyLocators.QUESTION_1_TEXTAREA)
        return question_element.get_attribute('value')
