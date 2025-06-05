import pytest
from shutil import copyfile
from pathlib import Path
from hw.code.ui.locators.survey_locators import SurveyLocators


class TestSurvey:
    @pytest.fixture
    def survey_opened(self, driver, survey_page):
        driver.get(survey_page.url)
        survey_page.is_opened()
        survey_page.create_survey()

    @staticmethod
    def change(survey_page):
        survey_page.set_name("edit")
        survey_page.close_modal()

    # Фикстура для получения пути к файлу логотипа
    @pytest.fixture
    def logo_path(self, tmp_path):
        src = Path(__file__).parent.parent / 'assets' / 'img' / 'logo-main.png'
        dst = tmp_path / 'logo-main.png'
        copyfile(src, dst)
        return str(dst)

    @pytest.fixture
    def sample_first_page(self, survey_opened, survey_page, logo_path):
        """
        Заполняет первую страницу формы опроса с базовыми тестовыми данными.

        Действия:
        - Открывает страницу с опросами
        - Проверяет, что она загружена
        - Открывает модальное окно создания нового опроса
        - Заполняет обязательные поля формы
        - Загружает логотип
        - Переходит на следующую страницу (вопросы)
        """
        survey_page.set_name("Test")
        survey_page.set_company("Test")
        survey_page.set_title("Test")
        survey_page.set_description("Test")
        survey_page.upload_logo(logo_path)
        survey_page.submit_form()

    @pytest.fixture
    def sample_first_and_second_page(self, sample_first_page, survey_page):
        """
        Заполняет первую страницу и добавляет первый вопрос.

        Действия:
        - Заполняет первую страницу (вызов предыдущего метода)
        - Добавляет вопрос с типом 'одиночный выбор' и тремя вариантами
        - Переходит к экрану завершения
        """
        survey_page.configure_first_question(
            question_type='single_choice',
            text="Test",
            options=["Да", "Нет", "Нейтрально"]
        )
        survey_page.submit_form()

    @pytest.fixture
    def create_survey(self, driver, sample_first_and_second_page, survey_page):
        """
        Полный сценарий создания опроса: от заполнения первой страницы до настройки финального экрана.

        Действия:
        - Заполняет первую страницу и добавляет вопрос
        - Настраивает экран завершения с тестовыми заголовком и описанием
        - Сохраняет изменения
        """
        survey_page.set_ending_title("Test")
        survey_page.set_ending_description("Test")
        survey_page.save_ending()
        yield
        driver.get(survey_page.url)
        survey_page.is_opened()
        survey_page.archive_survey()

    # Тест 1: Проверка открытия модального окна создания опроса
    def test_create_survey_modal_opens(self, survey_opened, survey_page):
        # Утверждение: модальное окно открыто, проверяем видимость поля ввода названия
        assert survey_page.find(SurveyLocators.NAME_INPUT).is_displayed(), "Модальное окно не открылось"

    # Тест 2: Заполнение первой страницы формы опроса
    def test_fill_first_page(self, survey_opened, survey_page):
        name = "FlexiKanban"
        company = "FlexiKanban"
        title = "Разделим?"
        description = "Не хватало ли Вам возможности автоматически делить и соединять задачи на своих досках?"

        # Ввод текста в обязательные поля
        survey_page.set_name(name)
        survey_page.set_company(company)
        survey_page.set_title(title)
        survey_page.set_description(description)
        survey_page.select_style("6")

        assert survey_page.get_field_value(SurveyLocators.NAME_INPUT) == name, "Наименование объявления не сохранено"
        assert survey_page.get_field_value(SurveyLocators.COMPANY_INPUT) == company, "Название компании не сохранено"
        assert survey_page.get_field_value(SurveyLocators.TITLE_INPUT) == title, "Название не сохранено"
        assert survey_page.get_field_value(SurveyLocators.DESCRIPTION_TEXTAREA) == description, "Описание не сохранено"

    # Тест 3: Загрузка логотипа
    def test_upload_logo(self, survey_opened, survey_page, logo_path):
        survey_page.upload_logo(logo_path)

        # Проверка, что логотип был загружен
        assert survey_page.find(SurveyLocators.APP_LOGO).is_displayed(), "Логотип не отображается"

    # Тест 4: Добавление одиночного вопроса
    def test_configure_first_question_single_choice(self, sample_first_page, survey_page):
        options = ["Да", "Нет", "Нейтрально"]
        title = "Хотели бы Вы иметь возможность делить задачи одной кнопкой?"

        survey_page.configure_first_question(
            question_type='single_choice',
            text=title,
            options=options,
            sample_answer=True
        )

        assert survey_page.find(SurveyLocators.QUESTION_1_TEXTAREA).get_attribute('value') == title, "Текст вопроса неверный"
        assert survey_page.find(SurveyLocators.YES_INPUT).get_attribute('value') == options[0] and survey_page.find(SurveyLocators.NO_INPUT).get_attribute('value') == options[1] and survey_page.find(SurveyLocators.NEUTRAL_INPUT).get_attribute('value') == options[2], "Полученные ответы не совпадают с введенными"

    # Тест 5: Добавление множественного выбора
    def test_configure_first_question_multiple_choice(self, sample_first_page, survey_page):
        options = ["Да", "Нет", "Нейтрально"]
        title = "Хотели бы Вы иметь возможность делить задачи одной кнопкой?"

        survey_page.configure_first_question(
            question_type='multiple_choice',
            text=title,
            options=options
        )

        assert survey_page.find(SurveyLocators.QUESTION_1_TEXTAREA).get_attribute('value') == title, "Текст вопроса неверный"
        assert survey_page.find(SurveyLocators.YES_INPUT).get_attribute('value') == options[0] and survey_page.find(
            SurveyLocators.NO_INPUT).get_attribute('value') == options[1] and survey_page.find(
            SurveyLocators.NEUTRAL_INPUT).get_attribute('value') == options[2], "Полученные ответы не совпадают с введенными"

    # Тест 6: Добавление шкального вопроса
    def test_configure_first_question_scale_question(self, sample_first_page, survey_page):
        text = "Оцените, насколько бы вы хотели увидеть этот функционал"

        survey_page.configure_first_question(
            question_type='scale',
            text=text,
            min_label=" Нет",
            max_label=" Да"
        )

        assert survey_page.find(SurveyLocators.QUESTION_1_TEXTAREA).get_attribute(
            'value') == text, "Текст вопроса неверный"

    # Тест 7: Добавление текстового вопроса
    def test_configure_first_question_text_question(self, sample_first_page, survey_page):
        text = "Напишите свои пожелания для этого функционала"

        survey_page.configure_first_question(
            question_type='text',
            text=text
        )

        assert survey_page.find(SurveyLocators.QUESTION_1_TEXTAREA).get_attribute(
            'value') == text, "Текст вопроса неверный"

    # Тест 8: Добавление второго вопроса и его удаление
    def test_add_and_remove_second_question(self, sample_first_page, survey_page):
        survey_page.configure_first_question(
            question_type='text',
            text="Напишите свои пожелания для этого функционала"
        )
        survey_page.add_second_question(
            question_type='scale',
            text="Оцените, насколько бы вы хотели увидеть этот функционал",
            min_label=" Нет",
            max_label=" Да",
            delete=True
        )

        assert len(survey_page.find_elements(SurveyLocators.QUESTION_1_TEXTAREA)) == 1, "Второй вопрос не был удален или изначально не добавлен корректно"

    # Тест 9: Дублирование вопроса
    def test_duplicate_question(self, sample_first_page, survey_page):
        survey_page.configure_first_question(
            question_type='single_choice',
            text="Хотели бы Вы иметь возможность делить задачи одной кнопкой?",
            options=["Да", "Нет", "Нейтрально"],
            sample_answer=True
        )
        survey_page.duplicate(0)

        assert len(survey_page.find_elements(SurveyLocators.QUESTION_1_TEXTAREA)) == 1, "Дубликат вопроса не был удален или изначально не добавлен"

    # Тест 10: Добавление и удаление правила (условий показа)
    def test_add_and_remove_rule(self, sample_first_page, survey_page):
        survey_page.configure_first_question(
            question_type='single_choice',
            text="Хотели бы Вы иметь возможность делить задачи одной кнопкой?",
            options=["Да", "Нет", "Нейтрально"],
            sample_answer=True
        )
        survey_page.add_second_question(
            question_type='scale',
            text="Оцените, насколько бы вы хотели увидеть этот функционал",
            min_label=" Нет",
            max_label=" Да"
        )
        survey_page.add_rule()
        survey_page.set_rule_criteria(
            amount=2
        )
        survey_page.remove_rule()

        assert survey_page.find(SurveyLocators.RULE_BUTTON).is_displayed(), "Правило не было удалено"

    # Тест 11: Стоп-экран
    def test_add_stop_screen(self, sample_first_page, survey_page):
        title = "Спасибо, Вам за участие!"
        description = "Вы нам очень помогли, оставив своё мнение по поводу этого вопроса!"

        survey_page.configure_first_question(
            question_type='single_choice',
            text="Хотели бы Вы иметь возможность делить задачи одной кнопкой?",
            options=["Да", "Нет", "Нейтрально"],
            sample_answer=True
        )
        survey_page.add_stop_screen()
        survey_page.remove_stop_screen()
        survey_page.add_stop_screen()
        survey_page.set_trigger_criteria(
            amount=2
        )
        survey_page.set_thank_you_title(
            title=title
        )
        survey_page.set_thank_you_description(
            description=description
        )

        assert survey_page.exists(SurveyLocators.THANK_YOU_TITLE), "Стоп-экран не добавлен"
        assert survey_page.get_field_value(SurveyLocators.THANK_YOU_TITLE) == title, "Заголовок благодарности не установлен"
        assert survey_page.get_field_value(SurveyLocators.THANK_YOU_DESCRIPTION) == description, "Описание благодарности не установлено"

    # Тест 12: Экран завершения (эндинг)
    def test_set_ending_screen(self, sample_first_and_second_page, survey_page):
        title = "Спасибо за Ваши ответы!"
        description = "Заявка отправлена, ждите результат!"
        site = "https://github.com/AnyFlex-Solutions"

        survey_page.set_ending_title(title)
        survey_page.set_ending_description(description)
        survey_page.add_link(site)

        assert survey_page.get_field_value(SurveyLocators.ENDING_TITLE_INPUT) == title, "Заголовок завершения не установлен"
        assert survey_page.get_field_value(SurveyLocators.ENDING_DESCRIPTION_INPUT) == description, "Описание завершения не установлен"
        assert survey_page.find(SurveyLocators.LINK_INPUT).get_attribute('value') == site, "Ссылка не установлена"

    # Тест 13: Проверка отмены сохранения при редактировании
    def test_edit_survey_without_saving(self, create_survey, survey_page):
        survey_page.open_edit_modal()
        TestSurvey.change(survey_page)
        survey_page.confirm_close_without_saving()

        survey_page.open_edit_modal()
        assert survey_page.get_field_value(SurveyLocators.NAME_INPUT) == 'Test', "The value has changed"

    # Тест 14: Проверка сохранения при редактировании
    def test_edit_survey_with_saving(self, create_survey, survey_page):
        survey_page.open_edit_modal()
        TestSurvey.change(survey_page)
        survey_page.confirm_close_with_saving()

        survey_page.open_edit_modal()
        assert survey_page.get_field_value(SurveyLocators.NAME_INPUT) == 'edit', "The value hasn`t changed"

    # Тест 15: Восстановление опроса из архива
    def test_restore_survey(self, create_survey, survey_page):
        survey_page.archive_survey()
        survey_page.select_archive_category()
        survey_page.restore_survey('Test')
        survey_page.select_active_category()

        try:
            survey_page.find(SurveyLocators.LIST_ELEMENT("Test"), timeout=3)
            found = True
        except:
            found = False

        assert found, "Опрос не был восстановлен в активные"

    # Тест 16: Поиск по названию опроса
    def test_search_survey(self, create_survey, survey_page):
        survey_page.search_survey('Test')

        try:
            survey_page.find(SurveyLocators.LIST_ELEMENT("Test"), timeout=3)
            found = True
        except:
            found = False

        assert found, "Опрос не отобразился"

        survey_page.search_survey('2')

        try:
            survey_page.find(SurveyLocators.LIST_ELEMENT("Test"), timeout=3)
            found = False
        except:
            found = True

        assert found, "Опрос отобразился, хотя не долен"

        survey_page.search_survey_clear()

    # Тест 17: Проверка ошибок валидации (пустые поля)
    def test_edit_survey_validation_errors_empty_field(self, survey_opened, survey_page):
        survey_page.submit_form()

        error = 'Нужно заполнить'
        amount = 5

        tests = SurveyLocators.VALIDATION_ERROR_FIELDS(error)
        # Находим контейнер формы
        container = survey_page.find(SurveyLocators.FORM_CONTAINER)

        # Ожидаем, пока в контейнере не появится минимум amount элемента с ошибкой
        survey_page.wait().until(
            lambda driver: len(container.find_elements(*tests)) >= amount
        )

        assert len(container.find_elements(*tests)) >= amount, "Ожидалось минимум 5 полей с ошибкой валидации"

    # Тест 18: Проверка ошибок валидации (слишком длинное значение)
    def test_edit_survey_validation_errors_big_value(self, survey_opened, survey_page):
        survey_page.submit_form()
        survey_page.set_company('testtesttesttesttesttesttesttest')

        error = 'Сократите текст'
        amount = 1

        tests = SurveyLocators.VALIDATION_ERROR_FIELDS(error)
        # Находим контейнер формы
        container = survey_page.find(SurveyLocators.FORM_CONTAINER)

        # Ожидаем, пока в контейнере не появится минимум amount элемента с ошибкой
        survey_page.wait().until(
            lambda driver: len(container.find_elements(*tests)) >= amount
        )

        assert len(container.find_elements(*tests)) >= amount, "Ожидалось минимум 5 полей с ошибкой валидации"

    # Тест 19: Проверка ошибок валидации (пустой вопрос)
    def test_edit_survey_validation_errors_empty_question(self, sample_first_page, survey_page):
        survey_page.submit_form()
        survey_page.add_stop_screen()

        error1 = 'Вопрос должен быть не пустым и содержать минимум 2 ответа'
        amount1 = 1

        error2 = 'Нужно заполнить все поля'
        amount2 = 1

        tests1 = SurveyLocators.VALIDATION_ERROR_FIELDS_SPAN(error1)
        tests2 = SurveyLocators.VALIDATION_ERROR_FIELDS_SPAN(error2)

        # Находим контейнер формы
        container = survey_page.find(SurveyLocators.FORM_CONTAINER_2)

        # Явное ожидание обеих ошибок по количеству
        survey_page.wait().until(
            lambda driver: len(container.find_elements(*tests1)) >= amount1
        ), f"Ожидалось минимум {amount1} ошибка(ок) с текстом: '{error1}'"

        survey_page.wait().until(
            lambda driver: len(container.find_elements(*tests2)) >= amount2
        ), f"Ожидалось минимум {amount2} ошибка(ок) с текстом: '{error2}'"

        assert len(container.find_elements(*tests1)) >= amount1, f"Ошибка: не найдено '{error1}'"
        assert len(container.find_elements(*tests2)) >= amount2, f"Ошибка: не найдено '{error2}'"
