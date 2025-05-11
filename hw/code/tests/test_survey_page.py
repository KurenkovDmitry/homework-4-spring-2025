import pytest
import os


def test_survey_page(driver, survey_page):
    driver.get(survey_page.url)
    survey_page.is_opened()
    survey_page.create_survey()

    logo_path = os.path.join(os.getcwd(), 'logo-main.png')

    survey_page.fill_survey_form(
        name="FlexiKanban",
        company="FlexiKanban",
        title="Разделим😎?",
        description="Не хватало ли Вам возможности автоматически делить и соединять задачи на своих досках?",
        logo_path=logo_path,
        style_id="6"
    )

    survey_page.proceed_to_questions()
