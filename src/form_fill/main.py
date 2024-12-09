import sys
from datetime import datetime
from pathlib import Path

import yaml

if str(Path(__file__).parent) not in sys.path:
    sys.path.append(str(Path(__file__).parent))
from add_args import setup_args
from Class.input import InputArgs
from driver_setup import setup_driver
from form_fillers import (
    fill_form_fields_1,
    fill_form_fields_2,
    fill_form_fields_3,
    fill_form_fields_4,
)
from input_actions import click_element
from screeen_shot import save_screenshot
from selenium.webdriver.common.by import By

# フォームが存在するURL
URL = "https://kaishi.e-tax.nta.go.jp/SU_APP/lnk/kaishiShinkiHojin"
CONFIG_FILE_PATH = Path(__file__).parent.parent.parent / "config" / "config.yaml"


def main(
    input_args: InputArgs,
) -> None:
    """
    メインの処理を実行します。
    """
    # WebDriverを設定
    driver = setup_driver(persistent=True)

    try:
        # ページを開く
        driver.get(URL)
        # 次へボタンをクリック
        click_element(driver, By.ID, "SU_next")

        # ------------ 1ページ目の処理 ------------
        # フォームの入力
        fill_form_fields_1(driver, input_args)

        # 次へボタンをクリック
        click_element(driver, By.ID, "form-confirm-btn")
        # window alertのOKボタンをクリック
        driver.switch_to.alert.accept()

        # ------------ 2ページ目の処理 ------------
        # フォームの入力
        fill_form_fields_2(driver, input_args)

        # 次へボタンをクリック
        click_element(driver, By.ID, "form-confirm-btn")

        if input_args.office_type == "支店":
            # ------------ 3ページ目の処理 ------------
            # フォームの入力
            fill_form_fields_3(driver, input_args)

            # 次へボタンをクリック
            click_element(driver, By.ID, "form-confirm-btn")

        # ------------ 4ページ目の処理 ------------
        # フォームの入力
        fill_form_fields_4(driver, input_args)

        # 次へボタンをクリック
        click_element(driver, By.ID, "form-confirm-btn")
        # window alertのOKボタンをクリック
        driver.switch_to.alert.accept()

        # スクリーンショットを撮る
        with open(CONFIG_FILE_PATH, "r") as f:
            config = yaml.safe_load(f)
        screenshot_dir = config["settings"]["screenshot_dir"]
        screenshot_name = (
            f"{input_args.company_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        )
        screenshot_path = Path(screenshot_dir) / screenshot_name
        save_screenshot(driver, screenshot_path)

        # ------------ 終了処理 ------------
        input("処理が完了しました。Enterキーを押すとブラウザを終了します。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        input("Enterキーを押すと終了します。")
    finally:
        # ブラウザを閉じる
        driver.quit()


if __name__ == "__main__":
    args = setup_args()

    input_args = InputArgs(
        corporate_number=args.corporate_number,
        org_name_position=args.org_name_position,
        organization_type=args.organization_type,
        company_name_kana=args.company_name_kana,
        company_name=args.company_name,
        office_type=args.office_type,
        branch_office_name_kana=args.branch_office_name_kana,
        branch_office_name=args.branch_office_name,
        zip_code=args.zip_code,
        prefecture=args.prefecture,
        city=args.city,
        street_address=args.street_address,
        building_name=args.building_name,
        phone_number=args.phone_number,
        tax_office_prefecture=args.tax_office_prefecture,
        tax_office_name=args.tax_office_name,
        representative_last_name_kana=args.representative_last_name_kana,
        representative_first_name_kana=args.representative_first_name_kana,
        representative_last_name=args.representative_last_name,
        representative_first_name=args.representative_first_name,
        representative_zip_code=args.representative_zip_code,
        representative_prefecture=args.representative_prefecture,
        representative_city=args.representative_city,
        representative_street_address=args.representative_street_address,
        representative_building_name=args.representative_building_name,
        representative_phone_number=args.representative_phone_number,
        head_office_name_position=args.head_office_name_position,
        head_office_organization_type=args.head_office_organization_type,
        head_office_name_kana=args.head_office_name_kana,
        head_office_name=args.head_office_name,
        head_office_zip_code=args.head_office_zip_code,
        head_office_prefecture=args.head_office_prefecture,
        head_office_city=args.head_office_city,
        head_office_street_address=args.head_office_street_address,
        head_office_building_name=args.head_office_building_name,
        head_office_phone_number=args.head_office_phone_number,
        password=args.password,
        secret_question=args.secret_question,
        secret_question_answer=args.secret_question_answer,
        establishment_year=args.establishment_year,
        establishment_month=args.establishment_month,
        establishment_day=args.establishment_day,
        show_password=args.show_password,
        tax_payment_confirmation_number=args.tax_payment_confirmation_number,
        tax_payment_name_kana=args.tax_payment_name_kana,
        main_mail_address=args.main_mail_address,
        sub_mail_address1=args.sub_mail_address1,
        sub_mail_address2=args.sub_mail_address2,
        show_atena=args.show_atena,
        atena=args.atena,
        sort_number=args.sort_number,
        reference_matters=args.reference_matters,
        is_agent=args.is_agent,
        agent_name=args.agent_name,
        agent_phone_number=args.agent_phone_number,
    )

    main(input_args)
