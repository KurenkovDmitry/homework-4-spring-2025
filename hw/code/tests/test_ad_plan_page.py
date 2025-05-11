import pytest


def test_ad_plan_page(driver, ad_plan_page):
    driver.get(ad_plan_page.url)
    ad_plan_page.is_opened()
    ad_plan_page.set_ad_name('Test Ad')
