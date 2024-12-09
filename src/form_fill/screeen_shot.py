import base64
import time
from pathlib import Path

from selenium import webdriver


def save_screenshot(
    driver: webdriver.Chrome, file_path: Path, is_full_size: bool = True
) -> None:
    # ページの読み込みを待つ
    time.sleep(1)

    # スクリーンショット設定
    screenshot_config = {
        # Trueの場合スクロールで隠れている箇所も含める、Falseの場合表示されている箇所のみ
        "captureBeyondViewport": is_full_size,
    }

    # スクリーンショット取得
    base64_image = driver.execute_cdp_cmd("Page.captureScreenshot", screenshot_config)

    # ファイル書き出し
    with open(file_path, "wb") as fh:
        fh.write(base64.b64decode(base64_image["data"]))

    print(f"スクリーンショットを保存しました: {file_path}")
