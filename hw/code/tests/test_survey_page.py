import pytest
import os


def test_survey_page(driver, survey_page):
    driver.get(survey_page.url)
    survey_page.is_opened()
    survey_page.create_survey()

    logo_path = os.path.join(os.getcwd(), 'assets/img/logo-main.png')

    survey_page.fill_survey_form(
        name="FlexiKanban",
        company="FlexiKanban",
        title="Разделим?",
        description="Не хватало ли Вам возможности автоматически делить и соединять задачи на своих досках?",
        logo_path=logo_path,
        style_id="6"
    )

    questions_data = [
        {
            'type': 'multiple_choice',
            'text': "Хотели бы Вы иметь возможность, делить задачи на доске одной кнопкой",
            'options': ["Да", "Нет", "Нейтрально"]
        },
        {
            'type': 'scale',
            'text': "Оцените, насколько бы вы хотели увидеть этот функционал у нас",
            'min_label': "1 - Нет",
            'max_label': "10 - Да"
        },
        {
            'type': 'text',
            'text': "Напишите свои пожелания для этого функционала"
        },
        {
            'type': 'multiple_choice',
            'text': "Что бы Вы хотели увидеть?",
            'options': ["Функционал соединения задач", "Функционал разделения задач"]
        }
    ]
    survey_page.proceed_to_questions(questions_data)

    survey_page.ending(
        title="Спасибо за Ваши ответы!",
        description="Заявка отправлена, попытаемся учесть все Ваши пожелания, ждите результат на нашем сайте!",
        link="https://github.com/AnyFlex-Solutions"
    )

    survey_page.edit()
    survey_page.delete()
