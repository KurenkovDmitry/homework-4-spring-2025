from ui.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from ui.locators.survey_locators import SurveyLocators


class SurveyPage(BasePage):
    url = 'https://ads.vk.com/hq/leadads/surveys'

    def create_survey(self):
        # Клик по кнопке создания опроса и ожидание модального окна
        self.click(SurveyLocators.CREATE_SURVEY_BUTTON)
        self.wait().until(EC.presence_of_element_located(SurveyLocators.MODAL_CONTENT))

    def fill_survey_form(self, name, company, title, description, logo_path, style_id):
        # Заполнение основной формы опроса
        self.input_text(SurveyLocators.NAME_INPUT, name)
        self.click(SurveyLocators.SET_GLOBAL_IMAGE)
        self.find(SurveyLocators.FILE_INPUT).send_keys(logo_path)
        self.focus(SurveyLocators.ITEM_LIST_ITEM)
        self.click(SurveyLocators.ITEM_LIST_ITEM)
        self.wait().until(EC.presence_of_element_located(SurveyLocators.APP_LOGO))
        self.input_text(SurveyLocators.COMPANY_INPUT, company)
        self.input_text(SurveyLocators.DESCRIPTION_TEXTAREA, description)
        self.click(SurveyLocators.STYLE_DIV(style_id))
        self.input_text(SurveyLocators.TITLE_INPUT, title)

    def proceed_to_questions(self, questions_data):
        # Переход к вопросам
        self.click(SurveyLocators.SUBMIT_BUTTON)

        # Обработка списка вопросов
        for idx, question in enumerate(questions_data, 1):
            if question['type'] == 'multiple_choice':
                self._add_multiple_choice_question(question['text'], question['options'], idx)
            elif question['type'] == 'scale':
                self._add_scale_question(question['text'], question['min_label'], question['max_label'], idx)
            elif question['type'] == 'text':
                self._add_text_question(question['text'], idx)

        # Добавление и настройка стоп-экрана
        self.click(SurveyLocators.ADD_STOP_SCREEN_BUTTON)
        self.click(SurveyLocators.REMOVE_STOP_SCREEN_BUTTON)
        self.click(SurveyLocators.ADD_STOP_SCREEN_BUTTON)
        self.click(SurveyLocators.TRIGGER_QUESTION)
        self.click(SurveyLocators.TRIGGER_QUESTION_OPTION)
        self.click(SurveyLocators.TRIGGER_CRITERIA)
        self.click(SurveyLocators.TRIGGER_OPTION_1)
        self.click(SurveyLocators.TRIGGER_CRITERIA)
        self.click(SurveyLocators.TRIGGER_OPTION_2)
        self.input_text(SurveyLocators.THANK_YOU_TITLE, "Спасибо, Вам за участие!")
        self.input_text(SurveyLocators.THANK_YOU_DESCRIPTION,
                        "Вы нам очень помогли, оставив своё мнение по поводу этого вопроса!")

    def _add_multiple_choice_question(self, text, options, question_idx):
        # Добавление вопроса с множественным выбором
        if question_idx > 1:
            self.click(SurveyLocators.ADD_QUESTION_BUTTON)
        if question_idx > 1:  # Для всех кроме первого вопроса нужно выбрать тип
            self.click(SurveyLocators.MULTIPLE_CHOICE_TYPE)
            self.click(SurveyLocators.MULTIPLE_CHOICE_OPTION)

        textarea = SurveyLocators.QUESTION_1_TEXTAREA if question_idx == 1 else SurveyLocators.QUESTION_4_TEXTAREA
        self.input_text(textarea, text)

        if question_idx == 1:
            self.input_text(SurveyLocators.YES_INPUT, options[0])
            self.input_text(SurveyLocators.NO_INPUT, options[1])
            self.click(SurveyLocators.ADD_ANSWER_BUTTON)
            self.click(SurveyLocators.REMOVE_ANSWER_BUTTON)
            self.click(SurveyLocators.ADD_ANSWER_BUTTON)
            self.input_text(SurveyLocators.NEUTRAL_INPUT, options[2])
            self.click(SurveyLocators.TEMPLATE_ANSWER_BUTTON)
            self.click(SurveyLocators.TEMPLATE_OPTION)
        else:
            self.input_text(SurveyLocators.CHOICE_1_INPUT, options[0])
            self.input_text(SurveyLocators.CHOICE_2_INPUT, options[1])
            self.click(SurveyLocators.DUPLICATE_QUESTION_BUTTON)
            self.click(SurveyLocators.REMOVE_DUPLICATE_BUTTON)

    def _add_scale_question(self, text, min_label, max_label, question_idx):
        # Добавление вопроса со шкалой
        self.click(SurveyLocators.ADD_QUESTION_BUTTON)
        self.click(SurveyLocators.SCALE_TYPE)
        self.click(SurveyLocators.SCALE_OPTION)
        self.click(SurveyLocators.SCALE_RANGE)
        self.click(SurveyLocators.RANGE_OPTION)
        self.input_text(SurveyLocators.QUESTION_2_TEXTAREA, text)
        self.input_text(SurveyLocators.SCALE_MIN_INPUT, min_label)
        self.input_text(SurveyLocators.SCALE_MAX_INPUT, max_label)
        self.click(SurveyLocators.RULE_BUTTON)
        self.click(SurveyLocators.RULE_CRITERIA)
        self.click(SurveyLocators.RULE_OPTION_1)
        self.click(SurveyLocators.RULE_CRITERIA)
        self.click(SurveyLocators.RULE_OPTION_2)

    def _add_text_question(self, text, question_idx):
        # Добавление текстового вопроса
        self.click(SurveyLocators.ADD_QUESTION_BUTTON)
        self.click(SurveyLocators.TEXT_TYPE)
        self.click(SurveyLocators.TEXT_OPTION)
        self.input_text(SurveyLocators.QUESTION_3_TEXTAREA, text)

    def ending(self, title, description, link):
        # Завершающий экран
        self.click(SurveyLocators.SUBMIT_BUTTON)
        self.input_text(SurveyLocators.ENDING_TITLE_INPUT, title)
        self.input_text(SurveyLocators.ENDING_DESCRIPTION_INPUT, description)
        self.click(SurveyLocators.ADD_LINK_BUTTON)
        self.input_text(SurveyLocators.LINK_INPUT, link)
        self.click(SurveyLocators.SAVE_ENDING_BUTTON)

    def delete(self):
        # Удаление опроса
        self.focus(SurveyLocators.ARCHIVE_BUTTON)
        self.click(SurveyLocators.ARCHIVE_BUTTON)
        self.click(SurveyLocators.CONFIRM_ARCHIVE_BUTTON)
        self.wait().until(EC.invisibility_of_element_located(SurveyLocators.CONFIRM_ARCHIVE_BUTTON))
        self.open_and_wait()

    def edit(self):
        # Открываем нужный дропдаун
        self.focus(self.loc.NAV_EDIT_BUTTON)
        self.click(self.loc.NAV_EDIT_BUTTON)

        # Очищаем обязательные поля
        self.input_text(self.loc.COMPANY_INPUT, "")
        self.input_text(self.loc.DESCRIPTION_TEXTAREA, "")

        # Нажимаем кнопку «Вопросы»
        self.click(self.loc.SUBMIT_BUTTON)

        # Находим контейнер формы
        container = self.find(self.loc.FORM_CONTAINER)

        # Ожидаем, пока в контейнере не появится минимум 2 элемента с ошибкой
        self.wait().until(
            lambda driver: len(container.find_elements(*self.loc.VALIDATION_ERROR_FIELDS)) >= 2
        )

        # Проверяем наличие ошибок
        errs = container.find_elements(*self.loc.VALIDATION_ERROR_FIELDS)
        assert len(errs) < 2, "Ожидалось минимум 2 поля с ошибкой валидации"
        for err in errs:
            foot = err.find_element(*self.loc.ERROR_TEXT)
            assert "Нужно заполнить" not in foot.text, "Неправильное сообщение об ошибке"

        # Кликаем вне модального окна — по фону
        self.click(self.loc.MODAL_OVERLAY)

        # Ожидаем окно подтверждения закрытия без сохранения
        try:
            modal = self.find(self.loc.CLOSE_EDITOR_MODAL_TITLE, timeout=3)
        except TimeoutException:
            raise AssertionError(
                "Не появилось подтверждение закрытия без сохранения при некорректных данных"
            )

        # Проверяем кнопки модалки
        ok_btn = modal.find_element(*self.loc.MODAL_SUBMIT_BUTTON)
        cancel_btn = modal.find_element(*self.loc.MODAL_CANCEL_BUTTON)
        assert not (ok.is_displayed() and cancel.is_displayed()), "Кнопки модалки не отображаются"

        # Закрываем модалку, чтобы не мешать дальнейшим тестам
        cancel_btn.click()
