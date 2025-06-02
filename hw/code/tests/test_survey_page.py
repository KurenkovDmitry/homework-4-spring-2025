import pytest
import os
import sys

# Добавляем директорию sample в sys.path, чтобы можно было импортировать модули оттуда
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../sample')))

from sample_survey_page import SurveySamples # Импорт вспомогательных методов для заполнения страниц


# Фикстура для получения пути к файлу логотипа
@pytest.fixture
def logo_path():
    THIS_DIR = os.path.dirname(__file__)
    HW_DIR = os.path.abspath(os.path.join(THIS_DIR, os.pardir))
    return os.path.join(HW_DIR, 'assets/img/logo-main.png')


# Тест 1: Проверка открытия модального окна создания опроса
def test_create_survey_modal_opens(driver, survey_page):
    driver.get(survey_page.url)
    survey_page.is_opened()
    survey_page.create_survey()


# Тест 2: Заполнение первой страницы формы опроса
def test_fill_first_page(driver, survey_page):
    driver.get(survey_page.url)
    survey_page.is_opened()
    survey_page.create_survey()

    # Ввод текста в обязательные поля
    survey_page.set_name("FlexiKanban")
    survey_page.set_company("FlexiKanban")
    survey_page.set_title("Разделим?")
    survey_page.set_description(
        "Не хватало ли Вам возможности автоматически делить и соединять задачи на своих досках?")
    survey_page.select_style("6")


# Тест 3: Загрузка логотипа
def test_upload_logo(driver, survey_page, logo_path):
    driver.get(survey_page.url)
    survey_page.is_opened()
    survey_page.create_survey()
    survey_page.set_name("Test")
    survey_page.set_company("Test")
    survey_page.set_title("Test")
    survey_page.set_description("Test")
    survey_page.upload_logo(logo_path)

    # Проверка, что логотип был загружен
    assert survey_page.is_logo_uploaded(), "Logo was not uploaded successfully"


# Тест 4: Добавление одиночного вопроса
def test_configure_first_question_single_choice(driver, survey_page, logo_path):
    SurveySamples.sample_first_page(driver, survey_page, logo_path)
    survey_page.configure_first_question(
        question_type='single_choice',
        text="Хотели бы Вы иметь возможность делить задачи одной кнопкой?",
        options=["Да", "Нет", "Нейтрально"],
        sample_answer=True
    )


# Тест 5: Добавление множественного выбора
def test_configure_first_question_multiple_choice(driver, survey_page, logo_path):
    SurveySamples.sample_first_page(driver, survey_page, logo_path)
    survey_page.configure_first_question(
        question_type='multiple_choice',
        text="Хотели бы Вы иметь возможность делить задачи одной кнопкой?",
        options=["Да", "Нет", "Нейтрально"]
    )


# Тест 6: Добавление шкального вопроса
def test_configure_first_question_scale_question(driver, survey_page, logo_path):
    SurveySamples.sample_first_page(driver, survey_page, logo_path)
    survey_page.configure_first_question(
        question_type='scale',
        text="Оцените, насколько бы вы хотели увидеть этот функционал",
        min_label=" Нет",
        max_label=" Да"
    )


# Тест 7: Добавление текстового вопроса
def test_configure_first_question_text_question(driver, survey_page, logo_path):
    SurveySamples.sample_first_page(driver, survey_page, logo_path)
    survey_page.configure_first_question(
        question_type='text',
        text="Напишите свои пожелания для этого функционала"
    )


# Тест 8: Добавление второго вопроса и его удаление
def test_two_questions(driver, survey_page, logo_path):
    SurveySamples.sample_first_page(driver, survey_page, logo_path)
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


# Тест 9: Дублирование вопроса
def test_duplicate_question(driver, survey_page, logo_path):
    SurveySamples.sample_first_page(driver, survey_page, logo_path)
    survey_page.configure_first_question(
        question_type='single_choice',
        text="Хотели бы Вы иметь возможность делить задачи одной кнопкой?",
        options=["Да", "Нет", "Нейтрально"],
        sample_answer=True
    )
    survey_page.duplicate(0)


# Тест 10: Добавление и удаление правила (условий показа)
def test_role(driver, survey_page, logo_path):
    SurveySamples.sample_first_page(driver, survey_page, logo_path)
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


# Тест 11: Стоп-экран
def test_stop_screen(driver, survey_page, logo_path):
    SurveySamples.sample_first_page(driver, survey_page, logo_path)
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


# Тест 12: Экран завершения (эндинг)
def test_set_ending_screen(driver, survey_page, logo_path):
    SurveySamples.sample_first_and_second_page(driver, survey_page, logo_path)
    survey_page.set_ending_title("Спасибо за Ваши ответы!")
    survey_page.set_ending_description("Заявка отправлена, ждите результат!")
    survey_page.add_link("https://github.com/AnyFlex-Solutions")


# Тест 13: Проверка сохранения/отмены при редактировании
def test_edit_survey_without_saving(driver, survey_page, logo_path):
    SurveySamples.create_survey(driver, survey_page, logo_path)

    def change():
        survey_page.set_name("edit")
        survey_page.close_modal()

    survey_page.open_edit_modal()
    change()
    assert survey_page.is_close_confirmation_present(), "Close confirmation did not appear"
    survey_page.confirm_close_without_saving()

    survey_page.open_edit_modal()
    assert survey_page.check_name('Test'), "The value has changed"
    change()
    survey_page.confirm_close_with_saving()

    survey_page.open_edit_modal()
    assert survey_page.check_name('edit'), "The value hasn`t changed"
    survey_page.close_modal()

    survey_page.archive_survey()


# Тест 14: Восстановление опроса из архива
def test_restore_survey(driver, survey_page, logo_path):
    SurveySamples.create_survey(driver, survey_page, logo_path)
    survey_page.archive_survey()
    survey_page.select_archive_category()
    survey_page.restore_survey('Test')
    survey_page.select_active_category()
    survey_page.archive_survey()


# Тест 15: Поиск по названию опроса
def test_search_survey(driver, survey_page, logo_path):
    SurveySamples.create_survey(driver, survey_page, logo_path)
    driver.get(survey_page.url)
    survey_page.is_opened()

    survey_page.search_survey('Test')
    assert survey_page.is_element_in_list('Test')

    survey_page.search_survey('2')
    assert not survey_page.is_element_in_list('Test2')

    survey_page.search_survey_clear()

    survey_page.archive_survey()


# Тест 16: Проверка ошибок валидации (пустые поля)
def test_edit_survey_validation_errors_empty_field(driver, survey_page):
    driver.get(survey_page.url)
    survey_page.is_opened()
    survey_page.create_survey()
    survey_page.submit_form()

    assert survey_page.check_errors(5, 'Нужно заполнить'), "Ожидалось минимум 5 полей с ошибкой валидации"


# Тест 17: Проверка ошибок валидации (слишком длинное значение)
def test_edit_survey_validation_errors_big_value(driver, survey_page):
    driver.get(survey_page.url)
    survey_page.is_opened()
    survey_page.create_survey()
    survey_page.submit_form()
    survey_page.set_company('testtesttesttesttesttesttesttest')

    assert survey_page.check_errors(1, 'Сократите текст'), "Ожидалось минимум 5 полей с ошибкой валидации"


# Тест 18: Проверка ошибок валидации (пустой вопрос)
def test_edit_survey_validation_errors_empty_question(driver, survey_page, logo_path):
    SurveySamples.sample_first_page(driver, survey_page, logo_path)
    survey_page.submit_form()
    survey_page.add_stop_screen()

    assert survey_page.check_errors(1, 'Вопрос должен быть не пустым и содержать минимум 2 ответа', v=2), "Ожидалось минимум 1 ошибка о не пустых ответах"
    assert survey_page.check_errors(1, 'Нужно заполнить все поля', v=2), "Ожидалось минимум 1 ошибка о не пустых полях"
