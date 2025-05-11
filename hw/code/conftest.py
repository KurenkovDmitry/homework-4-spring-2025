import pytest

pytest_plugins = [
    "ui.fixtures",
]


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome', help='Browser to run tests')
    parser.addoption('--url', default='https://ads.vk.com/', help='Base URL for tests')
    parser.addoption('--chrome-profile', default=None, help='Path to Chrome profile directory')


@pytest.fixture(scope='session')
def config(request):
    return {
        'browser': request.config.getoption('--browser'),
        'url': request.config.getoption('--url'),
        'chrome_profile': request.config.getoption('--chrome-profile'),
    }
