from selenium.webdriver.common.by import By


class SurveyLocators:
    # Локаторы для create_survey
    def __init__(self):
        pass

    CREATE_SURVEY_BUTTON = (By.CSS_SELECTOR, '[test-id="create-survey-button"]')
    MODAL_CONTENT = (By.CLASS_NAME, 'ModalSidebarPage_content__2mBu8')

    # Локаторы для fill_survey_form
    NAME_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Введите название"]')
    SET_GLOBAL_IMAGE = (By.XPATH, '//*[@data-testid="set-global-image"]')
    FILE_INPUT = (By.XPATH, '//input[@type="file"]')
    ITEM_LIST_ITEM = (By.XPATH, '//*[contains(@class, "ItemList_item")]')
    APP_LOGO = (By.XPATH, '//div[contains(@class, "TitleBlock-module_appLogo")]/img')
    COMPANY_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Введите название компании"]')
    DESCRIPTION_TEXTAREA = (By.CSS_SELECTOR, 'textarea[placeholder="Введите описание опроса"]')
    STYLE_DIV = lambda style_id: (By.CSS_SELECTOR, f'div[data-id="{style_id}"]')
    TITLE_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Введите заголовок"]')

    # Локаторы для proceed_to_questions
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[data-testid="submit"]')
    QUESTION_1_TEXTAREA = (By.XPATH,
                           "//div[@id='root']/div/div[3]/div/div[2]/form/div[2]/div/div/section/div/div/div/div[2]/div/span/textarea")
    YES_INPUT = (By.XPATH,
                 "//*[@id='root']/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div/div/div[2]/div[1]/div/div[1]/div[1]/div/span/input")
    NO_INPUT = (By.XPATH,
                "//*[@id='root']/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div/div/div[2]/div[1]/div/div[1]/div[2]/div/span/input")
    ADD_ANSWER_BUTTON = (By.XPATH,
                         "//*[@id='root']/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div/div/div[2]/div[2]/button")
    REMOVE_ANSWER_BUTTON = (By.XPATH,
                            "//*[@id='root']/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div/div/div[2]/div[1]/div/div[1]/div[3]/div/button")
    NEUTRAL_INPUT = (By.XPATH,
                     "//*[@id='root']/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div/div/div[2]/div[1]/div/div[1]/div[3]/div/span/input")
    TEMPLATE_ANSWER_BUTTON = (By.XPATH,
                              "//*[@id='root']/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div/div/div[2]/div[2]/div/button")
    TEMPLATE_OPTION = (By.XPATH, "/html/body/div[2]/div/div/div[1]/div")

    # Второй вопрос (шкала)
    ADD_QUESTION_BUTTON = (
    By.XPATH, "//*[@id='root']/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/button[1]")
    SCALE_TYPE = (By.XPATH,
                  "//*[@id='root']/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div/div[2]/div/div[1]/div[1]/div[2]/div")
    SCALE_OPTION = (By.XPATH, "/html/body/div[2]/div/div/div[4]")
    SCALE_RANGE = (By.XPATH,
                   "//*[@id='root']/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div/div[2]/div/div[1]/div[1]/div[3]/div/div")
    RANGE_OPTION = (By.XPATH, "/html/body/div[2]/div/div/div[2]")
    QUESTION_2_TEXTAREA = (By.XPATH,
                           "//div[@id='root']/div/div[3]/div/div[2]/form/div[2]/div/div/section/div/div/div[2]/div/div[2]/div/span/textarea")
    SCALE_MIN_INPUT = (By.XPATH,
                       "//*[@id='root']/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div/div[2]/div/div[2]/div/div/div/div[2]/span[1]/input")
    SCALE_MAX_INPUT = (By.XPATH,
                       "//*[@id='root']/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div/div[2]/div/div[2]/div/div/div/div[2]/span[2]/input")
    RULE_BUTTON = (By.XPATH,
                   "//*[@id='root']/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div/div[2]/div/div[1]/div[2]/div[1]/button")
    RULE_CRITERIA = (By.XPATH,
                     "//*[@id='root']/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div/div[2]/div/div[2]/div[1]/fieldset/div[2]/div/span")
    RULE_OPTION_1 = (By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div[1]")
    RULE_OPTION_2 = (By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div[2]")

    # Третий вопрос (текст)
    QUESTION_3_TEXTAREA = (By.XPATH,
                           "//div[@id='root']/div/div[3]/div/div[2]/form/div[2]/div/div/section/div/div/div[3]/div/div[2]/div/span/textarea")
    TEXT_TYPE = (By.XPATH,
                 "//*[@id='root']/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div/div[3]/div/div[1]/div[1]/div[2]/div")
    TEXT_OPTION = (By.XPATH, "/html/body/div[2]/div/div/div[3]")

    # Четвертый вопрос (множественный выбор)
    MULTIPLE_CHOICE_TYPE = (By.XPATH,
                            "//*[@id='root']/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div/div[4]/div/div[1]/div[1]/div[2]/div")
    MULTIPLE_CHOICE_OPTION = (By.XPATH, "/html/body/div[2]/div/div/div[2]")
    QUESTION_4_TEXTAREA = (By.XPATH,
                           "//div[@id='root']/div/div[3]/div/div[2]/form/div[2]/div/div/section/div/div/div[4]/div/div[2]/div/span/textarea")
    CHOICE_1_INPUT = (By.XPATH,
                      "//*[@id='root']/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div/div[4]/div/div[2]/div[1]/div/div[1]/div[1]/div/span/input")
    CHOICE_2_INPUT = (By.XPATH,
                      "//*[@id='root']/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div/span/input")
    DUPLICATE_QUESTION_BUTTON = (By.XPATH,
                                 "//*[@id='root']/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div/div[4]/div/div[1]/div[2]/div[2]/button")
    REMOVE_DUPLICATE_BUTTON = (By.XPATH,
                               "//*[@id='root']/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div/div[5]/div/div[1]/div[2]/div[3]/button")

    # Стоп-экран
    ADD_STOP_SCREEN_BUTTON = (
    By.XPATH, "//*[@id='root']/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/button[2]")
    REMOVE_STOP_SCREEN_BUTTON = (By.XPATH,
                                 "//*[@id='root']/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[2]/div/div[1]/div[2]/div/button")
    TRIGGER_QUESTION = (By.XPATH,
                        "//*[@id='root']/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[2]/div/div[2]/div[1]/div/div/div/input")
    TRIGGER_QUESTION_OPTION = (
    By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[1]/div[1]/div/div[1]")
    TRIGGER_CRITERIA = (By.XPATH,
                        "//*[@id='root']/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[2]/div/div[2]/div[2]/div/span")
    TRIGGER_OPTION_1 = (By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div[1]")
    TRIGGER_OPTION_2 = (By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div[2]")
    THANK_YOU_TITLE = (By.XPATH,
                       "//*[@id='root']/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[2]/div/div[3]/div[1]/span/input")
    THANK_YOU_DESCRIPTION = (By.XPATH,
                             "//*[@id='root']/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[2]/div/div[3]/div[2]/span/input")

    # Локаторы для ending
    ENDING_TITLE_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Введите заголовок"]')
    ENDING_DESCRIPTION_INPUT = (
    By.CSS_SELECTOR, 'input[placeholder="Введите описание: например, поблагодарите за прохождение опроса"]')
    ADD_LINK_BUTTON = (By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div[3]/div')
    LINK_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Введите ссылку"]')
    SAVE_ENDING_BUTTON = (By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/button[2]')

    # Локаторы для delete
    ARCHIVE_BUTTON = (By.XPATH, '//button[contains(@class, "Nav_item")]//span[contains(text(), "Архивировать")]')
    CONFIRM_ARCHIVE_BUTTON = (
    By.XPATH, '//button[contains(@class, "appearance-negative")]//span[contains(text(), "Архивировать")]')

    # Локаторы для редактирования
    NAV_EDIT_BUTTON = (By.XPATH, '//button[contains(@class, "Nav_item")]//span[contains(text(), "Редактировать")]')
    FORM_CONTAINER = (By.XPATH, '//*[contains(@class, "Preview_wrapper__Gq-Id")]')
    VALIDATION_ERROR_FIELDS = (By.XPATH, '//*[contains(@class, "vkuiFormItem--status-error")]')
    ERROR_TEXT = (By.XPATH, '//*[contains(@class, "vkuiFormItem__bottom")]')
    MODAL_OVERLAY = (By.CSS_SELECTOR, 'button[aria-label="Close"]')
    CLOSE_EDITOR_MODAL_TITLE = (By.XPATH, '//h2[contains(text(),"Закрыть редактор опроса?")]')
    MODAL_SUBMIT_BUTTON = (By.XPATH, "../..//button[@data-testid='submit']")
    MODAL_CANCEL_BUTTON = (By.XPATH, "../..//button[@data-testid='cancel']")
