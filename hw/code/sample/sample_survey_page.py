class SurveySamples:
    def __init__(self):
        # Пустой конструктор, не выполняет действий, так как все методы статические
        pass

    @staticmethod
    def sample_first_page(driver, survey_page, logo_path):
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
        driver.get(survey_page.url)
        survey_page.is_opened()
        survey_page.create_survey()
        survey_page.set_name("Test")
        survey_page.set_company("Test")
        survey_page.set_title("Test")
        survey_page.set_description("Test")
        survey_page.upload_logo(logo_path)
        survey_page.submit_form()

    @staticmethod
    def sample_first_and_second_page(driver, survey_page, logo_path):
        """
        Заполняет первую страницу и добавляет первый вопрос.

        Действия:
        - Заполняет первую страницу (вызов предыдущего метода)
        - Добавляет вопрос с типом 'одиночный выбор' и тремя вариантами
        - Переходит к экрану завершения
        """
        SurveySamples.sample_first_page(driver, survey_page, logo_path)
        survey_page.configure_first_question(
            question_type='single_choice',
            text="Test",
            options=["Да", "Нет", "Нейтрально"]
        )
        survey_page.submit_form()

    @staticmethod
    def create_survey(driver, survey_page, logo_path):
        """
        Полный сценарий создания опроса: от заполнения первой страницы до настройки финального экрана.

        Действия:
        - Заполняет первую страницу и добавляет вопрос
        - Настраивает экран завершения с тестовыми заголовком и описанием
        - Сохраняет изменения
        """
        SurveySamples.sample_first_and_second_page(driver, survey_page, logo_path)
        survey_page.set_ending_title("Test")
        survey_page.set_ending_description("Test")
        survey_page.save_ending()
