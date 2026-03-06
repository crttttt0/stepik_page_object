import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# Классы для установки драйверов, при первой установке будет долго скачивать и устанавливать без логов в консоль
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default=None,
        help="Выберите язык браузера",
    )

    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Выберите браузер (chrome/firefox)",
    )


@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption("language")
    if not lang:
        raise pytest.UsageError("Не выбран язык браузера")

    browser_name = request.config.getoption("browser_name")

    print("\nОткрытие драйвера...")
    match browser_name:
        case "chrome":
            options = ChromeOptions()
            options.add_experimental_option("prefs", {"intl.accept_languages": lang})

            service = ChromeService(executable_path=ChromeDriverManager().install())
            browser = webdriver.Chrome(service=service, options=options)
        case "firefox":
            options = FirefoxOptions()
            options.set_preference("intl.accept_languages", lang)

            service = FirefoxService(executable_path=GeckoDriverManager().install())
            browser = webdriver.Firefox(service=service, options=options)

    yield browser

    print("\nЗакрытие драйвера...")
    browser.quit()
