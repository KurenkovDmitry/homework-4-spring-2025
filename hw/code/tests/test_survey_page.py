import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../sample')))

from sample_survey_page import SurveySamples


# Fixture to get the logo path
@pytest.fixture
def logo_path():
    THIS_DIR = os.path.dirname(__file__)
    HW_DIR = os.path.abspath(os.path.join(THIS_DIR, os.pardir))
    return os.path.join(HW_DIR, 'assets/img/logo-main.png')


# Test 1: Check if the create survey modal opens
def test_create_survey_modal_opens(driver, survey_page):
    driver.get(survey_page.url)
    survey_page.is_opened()
    survey_page.create_survey()


# Test 2: Fill the first page of the survey form
def test_fill_first_page(driver, survey_page, logo_path):
    driver.get(survey_page.url)
    survey_page.is_opened()
    survey_page.create_survey()

    # Ввод данных в поля с явным ожиданием
    survey_page.set_name("FlexiKanban")
    survey_page.set_company("FlexiKanban")
    survey_page.set_title("Разделим?")
    survey_page.set_description(
        "Не хватало ли Вам возможности автоматически делить и соединять задачи на своих досках?")
    survey_page.select_style("6")


# Test 3: Upload logo on the first page
def test_upload_logo(driver, survey_page, logo_path):
    driver.get(survey_page.url)
    survey_page.is_opened()
    survey_page.create_survey()
    survey_page.set_name("Test")
    survey_page.set_company("Test")
    survey_page.set_title("Test")
    survey_page.set_description("Test")
    survey_page.upload_logo(logo_path)
    assert survey_page.is_logo_uploaded(), "Logo was not uploaded successfully"


# Test 4: Configure the first question as single choice
def test_configure_first_question_single_choice(driver, survey_page, logo_path):
    SurveySamples.sample_first_page(driver, survey_page, logo_path)
    survey_page.configure_first_question(
        question_type='single_choice',
        text="Хотели бы Вы иметь возможность делить задачи одной кнопкой?",
        options=["Да", "Нет", "Нейтрально"],
        sample_answer=True
    )


# Test 5: Configure the first question as multiple choice
def test_configure_first_question_multiple_choice(driver, survey_page, logo_path):
    SurveySamples.sample_first_page(driver, survey_page, logo_path)
    survey_page.configure_first_question(
        question_type='multiple_choice',
        text="Хотели бы Вы иметь возможность делить задачи одной кнопкой?",
        options=["Да", "Нет", "Нейтрально"]
    )


# Test 6: Configure the first question as scale
def test_configure_first_question_scale_question(driver, survey_page, logo_path):
    SurveySamples.sample_first_page(driver, survey_page, logo_path)
    survey_page.configure_first_question(
        question_type='scale',
        text="Оцените, насколько бы вы хотели увидеть этот функционал",
        min_label=" Нет",
        max_label=" Да"
    )


# Test 7: Configure the first question as text
def test_configure_first_question_text_question(driver, survey_page, logo_path):
    SurveySamples.sample_first_page(driver, survey_page, logo_path)
    survey_page.configure_first_question(
        question_type='text',
        text="Напишите свои пожелания для этого функционала"
    )


# Test 8: Two questions
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


# Test 9: Set up the ending screen
def test_set_ending_screen(driver, survey_page, logo_path):
    SurveySamples.sample_first_and_second_page(driver, survey_page, logo_path)
    survey_page.set_ending_title("Спасибо за Ваши ответы!")
    survey_page.set_ending_description("Заявка отправлена, ждите результат!")
    survey_page.add_link("https://github.com/AnyFlex-Solutions")
    #survey_page.save_ending()
