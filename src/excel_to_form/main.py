import sys
from pathlib import Path

import yaml

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).parent.parent))

import argparse

from form_fill.main import main as form_fill_main
from read_from_excel.main import main as read_from_excel_main

CONFIG_FILE_PATH = Path(__file__).parent.parent.parent / "config" / "config.yaml"


def main(corporate_name: str) -> None:
    """
    顧客名を受け取り、Excelファイルからデータを取得してフォームに入力します。
    """
    # Excelファイルからデータを取得
    input_args = read_from_excel_main(corporate_name)

    with open(CONFIG_FILE_PATH) as file:
        config = yaml.safe_load(file)

    # passwordを設定
    input_args.password = config["settings"]["password"]
    # emailを設定
    input_args.main_mail_address = config["settings"]["email"]
    # 税理士情報を設定
    input_args.is_agent = True
    input_args.agent_name = config["settings"]["tax_accountant_name"]
    print(input_args.agent_name)
    input_args.agent_phone_number = config["settings"]["tax_accountant_tel"]

    # フォームにデータを入力
    form_fill_main(input_args)

    print("処理が完了しました")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("corporate_name", help="法人名を指定してください")
    args = parser.parse_args()

    main(args.corporate_name)
