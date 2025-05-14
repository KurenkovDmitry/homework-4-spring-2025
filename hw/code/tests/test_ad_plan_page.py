import pytest
import os


def test_ad_plan_page(driver, ad_plan_page):
    driver.get(ad_plan_page.url)
    ad_plan_page.is_opened()

    logo_path = os.path.join(os.getcwd(), 'assets/img/logo-main.png')
    example_path = os.path.join(os.getcwd(), 'assets/img/img.png')
    exampl_prigl_path = os.path.join(os.getcwd(), 'assets/img/exampl-prigl.png')

    ad_plan_page.create_company_by_site(
        site="https://github.com/AnyFlex-Solutions"
    )
    ad_plan_page.input_data_about_site(
        description="Основной уклон к автоматизации действий пользователей при использовании канбан досок",
        budget="100",
        date_label="суббота, 31 мая 2025 г."
    )
    ad_plan_page.all_data(
        date_label="суббота, 31 мая 2025 г.",
        address="Россия, Москва \n Россия, Санкт-Петербург"
    )
    ad_plan_page.ending(
        logo_path=logo_path,
        example_path=example_path,
        paths=[logo_path, exampl_prigl_path],
        title="FlexiKanban: Управлять проектами просто!",
        short_description="Начни упрощать управление проектами!",
        long_description="FlexiKanban открыт для вас: оптимизируйте проекты, приступайте к работе уже сегодня."
    )
    ad_plan_page.delete(
        url='https://ads.vk.com/hq/dashboard/ad_plans?mode=ads&attribution=conversion&date_from=13.05.2025&date_to=14.05.2025&sort=-created'
    )
