from selenium.webdriver.common.by import By


class AdPlanLocators:
    # URL
    def __init__(self):
        pass

    URL = 'https://ads.vk.com/hq/new_create/ad_plan'

    # Входы и кнопки
    AD_NAME_INPUT = (By.ID, 'ad-name')
    SITE_CONVERSIONS_TAB = (By.CSS_SELECTOR, 'div[data-id="site_conversions"]')
    SITE_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Вставьте ссылку или выберите из списка"')

    END_DATE_TRIGGER = (By.CSS_SELECTOR, 'span[data-testid="end-date"]')
    DATE_OPTION = lambda date_label: (By.CSS_SELECTOR, f'div[aria-label="{date_label}"]')

    DESCRIPTION_TEXTAREA = (By.CSS_SELECTOR, 'textarea[placeholder="Опишите ваше предложение"]')
    BUDGET_TEXTAREA = (By.CSS_SELECTOR, 'textarea[placeholder="Не задан"]')
    BUDGET_FIELD = (By.CSS_SELECTOR, 'input[data-testid="budget"]')
    BUDGET_POPUP_FIRST = (By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]')

    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[class='vkuiButton vkuiButton--size-l vkuiButton--mode-primary vkuiButton--appearance-accent vkuiButton--align-center vkuiButton--sizeY-regular vkuiButton--stretched vkuiTappable vkuiInternalTappable vkuiTappable--sizeX-none vkuiTappable--hasHover vkuiTappable--hasActive vkuiButton--hover vkuiButton--active vkui-focus-visible'] span[class='vkuiButton__content']")

    # Больше группы
    MORE_GROUP_BUTTON = (By.XPATH, f'/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/main/div[2]/div[1]/div/div/div/div/div/button')
    MORE_BUTTON = (By.CSS_SELECTOR, f'button[aria-label="More"]')
    GROUP_POPUP_ITEM = (By.XPATH, f'/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/div[1]/div[2]')
    REMOVE_BUTTON = (By.CSS_SELECTOR, f'button[data-testid="button-remove"]')

    # Все данные раздела
    ALL_DATA_TRIGGER = (By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/main/div[2]/div[1]/div/div/div/div/div/section[1]/fieldset/div[2]/div[1]/div/div')
    ENABLED_OPTION = (By.CSS_SELECTOR, 'div[aria-disabled="false"]')
    CLEAR_FIELD = (By.CSS_SELECTOR, 'button[aria-label="Очистить поле"]')

    DATA_SUBSECTION_TRIGGER = (By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/main/div[2]/div[1]/div/div/div/div/div/section[1]/fieldset/div[2]/div[2]/div')
    POPUP_NEXT = (By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/button[2]')
    POPUP_SELECT_LAST = (By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[4]/button')
    FIRST_OPTION = (By.CSS_SELECTOR, 'div[data-id="0"]')
    POPUP_SELECT_FIFTH = (By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[5]/button')

    # Ввод местоположения
    LOCATION_ADD_BUTTON = (By.CSS_SELECTOR, 'section:nth-of-type(2) button')
    LOCATION_TEXTAREA = (By.CSS_SELECTOR, 'textarea[placeholder="Например: Россия, Москва, 468"]')
    LOCATION_SUBMIT = (By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/div/form/div[2]/button')
    CLOSE_LOCATION = (By.CSS_SELECTOR, 'button[aria-label="close_button"]')

    # Складные тумблеры
    @staticmethod
    def toggle(id_str): return (By.CSS_SELECTOR, f'div[id="{id_str}"]')

    AGE_SELECTOR = (By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/main/div[2]/div[1]/div/div/div/div/div/div/section[1]/div[2]/fieldset/div[2]/div/div[1]/div[2]')
    AGE_OPTION = (By.CSS_SELECTOR, 'div[data-item-id="16"]')
    AGE_DROPDOWN = (By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/main/div[2]/div[1]/div/div/div/div/div/div/section[1]/div[2]/fieldset/div[4]/div/div')
    AGE_POPUP_OPTION = (By.CSS_SELECTOR, 'option[value="16+"]')

    # Переключатели разделов
    SECTION2_TOGGLE = (By.CSS_SELECTOR, 'div[id="react-collapsed-toggle-:r1e:"]')
    SECTION2_ICON = (By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/main/div[2]/div[1]/div/div/div/div/div/div/section[2]/div[2]/fieldset/div[1]/div[1]/svg')
    SECTION2_CLICK_SPAN = (By.CSS_SELECTOR, 'div[data-id="9018"]')
    SECTION2_POPUP_BUTTON = (By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/button')

    # Секция 3
    SECTION3_TOGGLE = (By.CSS_SELECTOR, 'div[id="react-collapsed-toggle-:ru:"]')
    SECTION3_ITEM = (By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/main/div[2]/div[1]/div/div/div/div/div/div/section[3]/div[2]/fieldset/div[1]/div/div/span')
    SECTION3_OPTION = (By.CSS_SELECTOR, 'div[data-item-id="11356434"]')
    SECTION3_POPUP_BUTTON = (By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/button')

    # Footer submit
    FOOTER_SUBMIT = (By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/footer/div/div[2]/div[2]/div/button')

    # endind
    CHANGE_IMAGE_BUTTON = (By.XPATH, '//*[@data-testid="change-image"]')
    FILE_INPUT = (By.XPATH, '//input[@type="file"]')
    ITEM_LIST_ITEM = (By.XPATH, '//*[contains(@class, "ItemList_item")]')
    APP_LOGO_IMAGE = (By.XPATH, '//div[contains(@class, "TitleBlock-module_appLogo")]/img')
    TITLE_FIELD = (By.CSS_SELECTOR, 'div[data-testid="заголовок, макс. 40 символов"]')
    SHORT_DESC_FIELD = (By.CSS_SELECTOR, 'div[data-testid="описание, макс. 90 символов"]')
    LONG_DESC_FIELD = (
    By.CSS_SELECTOR, 'div[data-testid="Длинный текст для использования в лентах соцсетей (2000 знаков)"]')
    EXAMPLE_UPLOAD_INPUT = (By.XPATH, '//*[contains(@class, "vkuiVisuallyHidden")]')
    BUTTON_8 = (By.XPATH,
                '/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/main/div[2]/div[1]/div/div/div[3]/div[3]/div[3]/div/button[8]')
    BUTTON_22 = (By.XPATH,
                 '/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/main/div[2]/div[1]/div/div/div[3]/div[3]/div[3]/div/button[22]')
    WAIT_BUTTON = (By.XPATH,
                   '/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/main/div[2]/div[1]/div/div/div[1]/div/div/fieldset/div/div/div[9]/div[1]/div/div[1]/div/div/div[1]/div[3]/button')
    MULTI_OPTIONS_BUTTON = (By.CSS_SELECTOR, '//*[contains(@class, "MultiOptionsButton_button__QDFWw")]')
    POPUP_DIV1 = (By.XPATH, '/html/body/div[1]/div/div[2]/div[5]/div/div/div[1]')
    ATTACHMENTS_MODE_SELECT_BUTTON = (By.CSS_SELECTOR, '//*[contains(@class, "AttachmentsModeSelect_button__PX9z7")]')
    POPUP_DIV2 = (By.XPATH, '/html/body/div[1]/div/div[2]/div[5]/div/div/div[2]')
    UPLOAD_MEDIA_BUTTON = (By.CSS_SELECTOR, '//*[contains(@class, "DraggableList_uploadMediaButton__oi")]')
    PRIMARY_SUBMIT = (By.CSS_SELECTOR, '//*[contains(@class, "vkuiButton--mode-primar")]')
    ACTIONS_BUTTON = (By.CSS_SELECTOR, 'button[data-testid="actions"]')
    DELETE_OPTION = (By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[5]/div[1]/label[5]/div[2]/div[1]/span[1]')
