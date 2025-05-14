import pytest
import os


def test_ad_plan_page(driver, ad_plan_page):
    driver.get(ad_plan_page.url)
    ad_plan_page.is_opened()

    logo_path = os.path.join(os.getcwd(), 'assets/img/logo-main.png')

    ad_plan_page.create_company_by_site(
        site="https://github.com/AnyFlex-Solutions"
    )
    ad_plan_page.input_data_about_site(
        description="Основной уклон к автоматизации действий пользователей при использовании канбан досок",
        budget="100",
        data="суббота, 31 мая 2025 г."
    )
    ad_plan_page.all_data(
        data="суббота, 31 мая 2025 г."
    )
    ad_plan_page.ending(
        logo_path=logo_path,
        title="",
        short_description="",
        long_description=""
    )
