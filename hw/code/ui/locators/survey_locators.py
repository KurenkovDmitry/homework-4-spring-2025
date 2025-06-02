from selenium.webdriver.common.by import By


class SurveyLocators:
    # Локаторы для create_survey
    def __init__(self):
        pass

    CREATE_SURVEY_BUTTON = (By.CSS_SELECTOR, '[test-id="create-survey-button"]')
    MODAL_CONTENT = (By.CLASS_NAME, 'vkui__portal-root')
    MODAL = (By.CLASS_NAME, "PopoverContent_root__C8WZq")

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

    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[data-testid="submit"]')
    QUESTION_1_TEXTAREA = (By.XPATH, '//textarea[@placeholder="Текст вопроса"]')
    YES_INPUT = (By.XPATH, '(//input[@placeholder="Введите ответ"])[1]')
    NO_INPUT = (By.XPATH, '(//input[@placeholder="Введите ответ"])[2]')
    ADD_ANSWER_BUTTON = (By.XPATH, '//button[.//span[text()="Добавить вариант"]]')
    REMOVE_ANSWER_BUTTON = (By.CSS_SELECTOR, 'button.Answer_removeBtn__owvhi')
    NEUTRAL_INPUT = (By.XPATH, '(//input[@placeholder="Введите ответ"])[3]')
    TEMPLATE_ANSWER_BUTTON = (By.XPATH, '//button[.//span[text()="Ответ из шаблона"]]')
    TEMPLATE_ANSWER_MODAL = (By.CLASS_NAME, "Tooltip_tooltipContainer__2gjYa")
    TEMPLATE_OPTION = (By.XPATH, '//span[contains(text(), "Другое (свой ответ)")]')

    ADD_QUESTION_BUTTON = (By.XPATH, '//button[.//span[text()="Добавить вопрос"]]')
    TYPE = (By.XPATH, '//div[contains(@class, "HintSelector_hintSelectorButton__pfubH")]')
    SCALE_OPTION = (By.XPATH, '//span[contains(text(), "Шкала")]')
    SCALE_RANGE = (By.XPATH, '//div[text()="0 — 10"]')
    RANGE_OPTION = (By.XPATH, '//span[contains(text(), "1 — 10")]')
    QUESTION_2_TEXTAREA = (By.XPATH, '(//textarea[@placeholder="Текст вопроса"])[2]')
    SCALE_MIN_INPUT = (By.XPATH, '//input[contains(@value, "0 - Скорее нет")]')
    SCALE_MAX_INPUT = (By.XPATH, '//input[contains(@value, "10 - Скорее да")]')
    RULE_BUTTON = (By.CSS_SELECTOR, 'button.Question_conditionButton__pjBTk')
    RULE_CRITERIA = (By.CSS_SELECTOR, 'div.ChipsSelect_wrapper__m9y64')
    RULE_OPTION_1 = (By.XPATH, '//div[contains(@class, "vkuiPopover")]//div[1]/div[1]')
    RULE_OPTION_2 = (By.XPATH, '//div[contains(@class, "vkuiPopover")]//div[1]/div[2]')

    QUESTION_3_TEXTAREA = (By.XPATH, '(//textarea[@placeholder="Текст вопроса"])[3]')
    TEXT_OPTION = (By.XPATH, '//span[contains(text(), "Ответ в свободной форме")]')

    MULTIPLE_CHOICE_OPTION = (By.XPATH, '//span[contains(text(), "Несколько из списка")]')
    DUPLICATE_QUESTION_BUTTON = (By.CSS_SELECTOR, 'button.Question_duplicateQuestionButton__R6XyA')
    REMOVE_QUESTION_BUTTON = (By.CSS_SELECTOR, 'button.Question_removeQuestionButton__lJ5wm')

    ADD_STOP_SCREEN_BUTTON = (By.XPATH, '//button[text()="Добавить стоп-экран"]')
    REMOVE_STOP_SCREEN_BUTTON = (By.CSS_SELECTOR, 'button.StopScreen_removeButton__oX7R+')
    TRIGGER_QUESTION = (By.XPATH, '//input[@placeholder="Выбрать вопрос"]')
    TRIGGER_QUESTION_OPTION = (By.XPATH, '//div[contains(@class, "vkuiPopover")]//div[1]')
    TRIGGER_CRITERIA = (By.CSS_SELECTOR, 'div.ChipsSelect_wrapper__m9y64')
    TRIGGER_OPTION_1 = (By.XPATH, '//div[contains(@class, "vkuiPopover")]//div[1]/div[1]')
    TRIGGER_OPTION_2 = (By.XPATH, '//div[contains(@class, "vkuiPopover")]//div[1]/div[2]')
    THANK_YOU_TITLE = (By.XPATH, '//input[@placeholder="Введите заголовок"]')
    THANK_YOU_DESCRIPTION = (By.XPATH, '//input[@placeholder="Введите описание опроса"]')

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
