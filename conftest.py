import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Класс для установки драйвера, при первой установке будет долго скачивать и устанавливать без логов в консоль
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default=None,
        help="Выберите язык браузера",
    )


@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption("language")
    if not lang:
        raise pytest.UsageError("Не выбран язык браузера")

    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": lang})

    # Только Chrome
    print("\nОткрытие драйвера...")
    service = Service(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)

    yield browser

    print("\nЗакрытие драйвера...")
    browser.quit()
