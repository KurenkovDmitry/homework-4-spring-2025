import pytest
from shutil import copyfile
from pathlib import Path


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
    def create_survey(self, sample_first_and_second_page, survey_page):
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

    # Тест 1: Проверка открытия модального окна создания опроса
    def test_create_survey_modal_opens(self, survey_opened, survey_page):
        # Утверждение: модальное окно открыто, проверяем видимость поля ввода названия
        assert survey_page.is_modal_opened(), "Модальное окно не открылось"

    # Тест 2: Заполнение первой страницы формы опроса
    def test_fill_first_page(self, survey_opened, survey_page):
        # Ввод текста в обязательные поля
        survey_page.set_name("FlexiKanban")
        survey_page.set_company("FlexiKanban")
        survey_page.set_title("Разделим?")
        survey_page.set_description(
            "Не хватало ли Вам возможности автоматически делить и соединять задачи на своих досках?")
        survey_page.select_style("6")

        assert survey_page.check_name("FlexiKanban"), "Название не сохранено"

    # Тест 3: Загрузка логотипа
    def test_upload_logo(self, survey_opened, survey_page, logo_path):
        survey_page.upload_logo(logo_path)

        # Проверка, что логотип был загружен
        assert survey_page.is_logo_uploaded(), "Логотип не отображается"

    # Тест 4: Добавление одиночного вопроса
    def test_configure_first_question_single_choice(self, sample_first_page, survey_page):
        survey_page.configure_first_question(
            question_type='single_choice',
            text="Хотели бы Вы иметь возможность делить задачи одной кнопкой?",
            options=["Да", "Нет", "Нейтрально"],
            sample_answer=True
        )

        assert survey_page.get_question_text(
            1) == "Хотели бы Вы иметь возможность делить задачи одной кнопкой?", "Текст вопроса неверный"
        assert survey_page.check_answers_v1(ans=['Да', 'Нет', 'Нейтрально']), "Полученные ответы не совпадают с введенными"

    # Тест 5: Добавление множественного выбора
    def test_configure_first_question_multiple_choice(self, sample_first_page, survey_page):
        survey_page.configure_first_question(
            question_type='multiple_choice',
            text="Хотели бы Вы иметь возможность делить задачи одной кнопкой?",
            options=["Да", "Нет", "Нейтрально"]
        )

        assert survey_page.get_question_text(
            1) == "Хотели бы Вы иметь возможность делить задачи одной кнопкой?", "Текст вопроса неверный"
        assert survey_page.check_answers_v1(['Да', 'Нет', 'Нейтрально']), "Полученные ответы не совпадают с введенными"

    # Тест 6: Добавление шкального вопроса
    def test_configure_first_question_scale_question(self, sample_first_page, survey_page):
        survey_page.configure_first_question(
            question_type='scale',
            text="Оцените, насколько бы вы хотели увидеть этот функционал",
            min_label=" Нет",
            max_label=" Да"
        )

        assert survey_page.get_question_text(
            1) == "Оцените, насколько бы вы хотели увидеть этот функционал", "Текст вопроса неверный"

    # Тест 7: Добавление текстового вопроса
    def test_configure_first_question_text_question(self, sample_first_page, survey_page):
        survey_page.configure_first_question(
            question_type='text',
            text="Напишите свои пожелания для этого функционала"
        )

        assert survey_page.get_question_text(
            1) == "Напишите свои пожелания для этого функционала", "Текст вопроса неверный"

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

        assert survey_page.check_amount_questions(1), "Второй вопрос не был удален или изначально не добавлен корректно"

    # Тест 9: Дублирование вопроса
    def test_duplicate_question(self, sample_first_page, survey_page):
        survey_page.configure_first_question(
            question_type='single_choice',
            text="Хотели бы Вы иметь возможность делить задачи одной кнопкой?",
            options=["Да", "Нет", "Нейтрально"],
            sample_answer=True
        )
        survey_page.duplicate(0)

        assert survey_page.check_amount_questions(1), "Дубликат вопроса не был удален или изначально не добавлен"

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

        assert survey_page.check_rule(), "Правило не было удалено"

    # Тест 11: Стоп-экран
    def test_add_stop_screen(self, sample_first_page, survey_page):
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
            title="Спасибо, Вам за участие!"
        )
        survey_page.set_thank_you_description(
            description="Вы нам очень помогли, оставив своё мнение по поводу этого вопроса!"
        )

        assert survey_page.check_stop_screen(), "Стоп-экран не добавлен"
        assert survey_page.check_thank_you_title("Спасибо, Вам за участие!"), "Заголовок благодарности не установлен"

    # Тест 12: Экран завершения (эндинг)
    def test_set_ending_screen(self, sample_first_and_second_page, survey_page):
        survey_page.set_ending_title("Спасибо за Ваши ответы!")
        survey_page.set_ending_description("Заявка отправлена, ждите результат!")
        survey_page.add_link("https://github.com/AnyFlex-Solutions")

        assert survey_page.check_ending_title("Спасибо за Ваши ответы!"), "Заголовок завершения не установлен"
        assert survey_page.check_ending_link("https://github.com/AnyFlex-Solutions"), "Ссылка не установлена"

    # Тест 13: Проверка отмены сохранения при редактировании
    def test_edit_survey_without_saving(self, create_survey, survey_page):
        survey_page.open_edit_modal()
        TestSurvey.change(survey_page)
        survey_page.confirm_close_without_saving()

        survey_page.open_edit_modal()
        assert survey_page.check_name('Test'), "The value has changed"

        survey_page.close_modal()
        survey_page.archive_survey()

    # Тест 14: Проверка сохранения при редактировании
    def test_edit_survey_with_saving(self, create_survey, survey_page):
        survey_page.open_edit_modal()
        TestSurvey.change(survey_page)
        survey_page.confirm_close_with_saving()

        survey_page.open_edit_modal()
        assert survey_page.check_name('edit'), "The value hasn`t changed"
        survey_page.close_modal()

        survey_page.archive_survey()

    # Тест 15: Восстановление опроса из архива
    def test_restore_survey(self, create_survey, survey_page):
        survey_page.archive_survey()
        survey_page.select_archive_category()
        survey_page.restore_survey('Test')
        survey_page.select_active_category()
        survey_page.archive_survey()

        assert survey_page.is_element_in_list('Test'), "Опрос не был восстановлен в активные"

    # Тест 16: Поиск по названию опроса
    def test_search_survey(self, create_survey, survey_page):
        survey_page.search_survey('Test')
        assert survey_page.is_element_in_list('Test')

        survey_page.search_survey('2')
        assert not survey_page.is_element_in_list('Test2')

        survey_page.search_survey_clear()

        survey_page.archive_survey()

    # Тест 17: Проверка ошибок валидации (пустые поля)
    def test_edit_survey_validation_errors_empty_field(self, survey_opened, survey_page):
        survey_page.submit_form()

        assert survey_page.check_errors(5, 'Нужно заполнить'), "Ожидалось минимум 5 полей с ошибкой валидации"

    # Тест 18: Проверка ошибок валидации (слишком длинное значение)
    def test_edit_survey_validation_errors_big_value(self, survey_opened, survey_page):
        survey_page.submit_form()
        survey_page.set_company('testtesttesttesttesttesttesttest')

        assert survey_page.check_errors(1, 'Сократите текст'), "Ожидалось минимум 5 полей с ошибкой валидации"

    # Тест 19: Проверка ошибок валидации (пустой вопрос)
    def test_edit_survey_validation_errors_empty_question(self, sample_first_page, survey_page):
        survey_page.submit_form()
        survey_page.add_stop_screen()

        assert survey_page.check_errors(1, 'Вопрос должен быть не пустым и содержать минимум 2 ответа', v=2), "Ожидалось минимум 1 ошибка о не пустых ответах"
        assert survey_page.check_errors(1, 'Нужно заполнить все поля', v=2), "Ожидалось минимум 1 ошибка о не пустых полях"
