from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def wait_and_fill_input_field(
    driver: webdriver.Chrome,
    by: By,
    value: str,
    input_text: str,
    timeout: int = 5,
) -> None:
    """
    指定された入力フィールドにテキストを入力します。
    """
    # None, 空文字, "nan" の場合は何もしない
    if input_text in [None, ""]:
        return
    if type(input_text) is str and input_text.lower().strip() == "nan":
        return

    input_field = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, value))
    )
    input_field.send_keys(input_text)


def wait_and_select_dropdown(
    driver: webdriver.Chrome,
    by: By,
    value: str,
    option_text: str,
    timeout: int = 5,
) -> None:
    """
    指定されたドロップダウンメニューからオプションを選択します。
    """
    # None, 空文字, "nan" の場合は何もしない
    if option_text in [None, ""]:
        return
    if type(option_text) is str and option_text.lower().strip() == "nan":
        return

    dropdown = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, value))
    )
    try:
        option = dropdown.find_element(By.XPATH, f".//option[text()='{option_text}']")
        option.click()
    except Exception:
        print(f"{value}からオプションを選択できませんでした: {option_text}")
        return

    # フォーカスを外す
    try:
        driver.execute_script("arguments[0].blur();", dropdown)
    except Exception:
        print(f"{value}からフォーカスを外すことができませんでした")


def click_element(
    driver: webdriver.Chrome, by: By, value: str, timeout: int = 5
) -> None:
    """
    指定された要素をクリックします。
    """
    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, value))
    )

    try:
        element.click()
    except ElementClickInterceptedException:
        # クリックできない場合はスクロールしてから再度クリック
        try:
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            driver.execute_script("arguments[0].click();", element)
        except Exception:
            print(f"{value}をクリックできませんでした")
