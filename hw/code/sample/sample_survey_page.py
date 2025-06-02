class SurveySamples:
    def __init__(self):
        pass

    @staticmethod
    def sample_first_page(driver, survey_page, logo_path):
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
        SurveySamples.sample_first_page(driver, survey_page, logo_path)
        survey_page.configure_first_question(
            question_type='single_choice',
            text="Test",
            options=["Да", "Нет", "Нейтрально"]
        )
        survey_page.submit_form()

