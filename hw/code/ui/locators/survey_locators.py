from selenium.webdriver.common.by import By


class SurveyLocators:
    # Локаторы для create_survey
    def __init__(self):
        pass

    # --- Локаторы для создания опроса ---
    CREATE_SURVEY_BUTTON = (By.CSS_SELECTOR, '[test-id="create-survey-button"]')
    MODAL_CONTENT = (By.CLASS_NAME, 'vkui__portal-root')
    MODAL = (By.CLASS_NAME, "PopoverContent_root__C8WZq")

    # --- Локаторы для формы опроса ---
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

    # --- Первый вопрос ---
    QUESTION_1_TEXTAREA = (By.XPATH, '//textarea[@placeholder="Текст вопроса"]')
    YES_INPUT = (By.XPATH, '(//input[@placeholder="Введите ответ"])[1]')
    NO_INPUT = (By.XPATH, '(//input[@placeholder="Введите ответ"])[2]')
    ADD_ANSWER_BUTTON = (By.XPATH, '//button[.//span[text()="Добавить вариант"]]')
    REMOVE_ANSWER_BUTTON = (By.CSS_SELECTOR, 'button.Answer_removeBtn__owvhi')
    NEUTRAL_INPUT = (By.XPATH, '(//input[@placeholder="Введите ответ"])[3]')
    TEMPLATE_ANSWER_BUTTON = (By.XPATH, '//button[.//span[text()="Ответ из шаблона"]]')
    TEMPLATE_ANSWER_MODAL = (By.CLASS_NAME, "Tooltip_tooltipContainer__2gjYa")
    TEMPLATE_OPTION = (By.XPATH, '//span[contains(text(), "Другое (свой ответ)")]')

    # --- Второй вопрос / переключение типа вопроса --
    ADD_QUESTION_BUTTON = (By.XPATH, '//button[.//span[text()="Добавить вопрос"]]')
    TYPE = (By.XPATH, '//div[contains(@class, "HintSelector_hintSelectorButton__pfubH")]')
    SCALE_OPTION = (By.XPATH, '//span[contains(text(), "Шкала")]')
    SCALE_RANGE = (By.XPATH, '//div[text()="0 — 10"]')
    RANGE_OPTION = (By.XPATH, '//span[contains(text(), "1 — 10")]')
    QUESTION_2_TEXTAREA = (By.XPATH, '(//textarea[@placeholder="Текст вопроса"])[2]')
    SCALE_MIN_INPUT = (By.XPATH, '//input[contains(@value, "0 - Скорее нет")]')
    SCALE_MAX_INPUT = (By.XPATH, '//input[contains(@value, "10 - Скорее да")]')

    # --- Условия показа ---
    RULE_BUTTON = (By.XPATH, '//button[contains(@class, "Question_conditionButton__pjBTk")]')
    RULE_CRITERIA = (By.CSS_SELECTOR, 'div.ChipsSelect_wrapper__m9y64')
    RULE_OPTION = (By.XPATH, '//div[contains(@class, "vkuiParagraph")]')

    TEXT_OPTION = (By.XPATH, '//span[contains(text(), "Ответ в свободной форме")]')

    MULTIPLE_CHOICE_OPTION = (By.XPATH, '//span[contains(text(), "Несколько из списка")]')
    DUPLICATE_QUESTION_BUTTON = (By.CSS_SELECTOR, 'button.Question_duplicateQuestionButton__R6XyA')
    REMOVE_QUESTION_BUTTON = (By.CSS_SELECTOR, 'button.Question_removeQuestionButton__lJ5wm')

    # --- Стоп-экран ---
    ADD_STOP_SCREEN_BUTTON = (By.XPATH, '//button[.//span[text()="Добавить стоп-экран"]]')
    REMOVE_STOP_SCREEN_BUTTON = (By.XPATH, '//button[contains(@class, "StopScreen_removeButton__oX7R+")]')
    TRIGGER_CRITERIA = (By.CSS_SELECTOR, 'div.ChipsSelect_wrapper__m9y64')
    TRIGGER_OPTION = (By.XPATH, '//div[contains(@class, "vkuiParagraph")]')
    THANK_YOU_TITLE = (By.XPATH, '//input[@placeholder="Введите заголовок"]')
    THANK_YOU_DESCRIPTION = (By.XPATH, '//input[@placeholder="Введите описание опроса"]')

    # --- Завершающий экран ---
    ENDING_TITLE_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Введите заголовок"]')
    ENDING_DESCRIPTION_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Введите описание: например, поблагодарите за прохождение опроса"]')
    ADD_LINK_BUTTON = (By.XPATH, '//div[contains(@class, "vkuiCellButton")]')
    LINK_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Введите ссылку"]')
    SAVE_ENDING_BUTTON = (By.XPATH, '//button[.//span[text()="Запустить опрос"]]')

    # --- Архивация ---
    ARCHIVE_BUTTON = (By.XPATH, '//button[contains(@class, "Nav_item")]//span[contains(text(), "Архивировать")]')
    CONFIRM_ARCHIVE_BUTTON = (By.XPATH, '//button[contains(@class, "appearance-negative")]//span[contains(text(), "Архивировать")]')

    # --- Редактирование ---
    NAV_EDIT_BUTTON = (By.XPATH, '//button[contains(@class, "Nav_item")]//span[contains(text(), "Редактировать")]')
    FORM_CONTAINER = (By.XPATH, '//*[contains(@class, "Preview_wrapper__Gq-Id")]')
    FORM_CONTAINER_2 = (By.XPATH, '//*[contains(@class, "Questions_wrapper__a8XCz")]')
    VALIDATION_ERROR_FIELDS = lambda error: (By.XPATH, f'//div[text()="{error}"]')
    VALIDATION_ERROR_FIELDS_SPAN = lambda error: (By.XPATH, f'//span[text()="{error}"]')
    MODAL_OVERLAY = (By.CSS_SELECTOR, 'button[aria-label="Close"]')
    CLOSE_EDITOR_MODAL_TITLE_AFTER_EDIT = (By.XPATH, '//span[contains(@class,"ModalConfirm_title__nR3Fc")]')
    MODAL_SUBMIT_BUTTON = (By.XPATH, '//button[.//span[text()="Сохранить опрос"]]')
    MODAL_CANCEL_BUTTON = (By.XPATH, '//button[.//span[text()="Выйти без сохранения"]]')

    # --- Фильтрация, восстановление, поиск ---
    SELECT_CATEGORY_DROPDOWN = (By.XPATH, '//div[contains(@class, "vkuiCustomSelectInput")]')
    ARCHIVE_CATEGORY_OPTION = (By.XPATH, '//div[text()="В архиве"]')
    ACTIVE_CATEGORY_OPTION = (By.XPATH, '//div[text()="Активные"]')
    RESTORE_ELEMENT_BUTTON = (By.XPATH, f'//button[contains(@class, "Nav_item")]//span[contains(text(), "Восстановить")]')
    RESTORE_ELEMENT_AGREE_BUTTON = (By.XPATH, '//button[contains(@class, "appearance-positive")]//span[contains(text(), "Восстановить")]')
    SEARCH_INPUT = (By.XPATH, '//input[@placeholder="Поиск"]')
    LIST_ELEMENT = lambda n: (By.XPATH, f'//div[span[@data-testid="lead_form_name__{n}"]]')
