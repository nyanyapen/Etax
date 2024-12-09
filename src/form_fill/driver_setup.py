from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def setup_driver(persistent: bool = True) -> webdriver.Chrome:
    """
    Chrome WebDriverのインスタンスを設定して返します。

    Parameters
    ----------
    persistent : bool, optional
        スクリプトが終了してもブラウザを開き続けるかどうかを指定します。デフォルトはTrue。
    """

    # Chrome WebDriverのオプションを設定
    chrome_options = webdriver.ChromeOptions()
    if persistent:
        chrome_options.add_experimental_option("detach", True)

    # Chrome WebDriverのサービスを設定
    service = Service(ChromeDriverManager().install())

    # Chrome WebDriverのインスタンスを設定
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.maximize_window()
    return driver
