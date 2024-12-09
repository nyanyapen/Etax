import sys
from pathlib import Path

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).parent.parent))

import argparse

import pandas as pd
import yaml

from form_fill.Class.input import InputArgs

CONFIG_FILE_PATH = Path(__file__).parent.parent.parent / "config" / "config.yaml"


def main(corporate_name) -> InputArgs:
    """
    顧客名を受け取り、Excelファイルからデータを取得してInputArgsクラスに変換します。
    """
    # Excelファイルをデータフレームとして読み込む
    with open(CONFIG_FILE_PATH) as file:
        config = yaml.safe_load(file)
    excel_file_path = config["settings"]["excel_file"]
    sheet_name = config["settings"]["sheet_name"]

    # 文字列として読み込む Nan は空文字に変換
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name, dtype="str")
    df = df.fillna("")
    # print(df)

    # フィルタリング
    df = df[df["法人名"] == corporate_name]

    if df.empty:
        raise ValueError(f"法人名: {corporate_name} が見つかりません")
    if df.shape[0] > 1:
        raise ValueError(f"法人名: {corporate_name} が複数見つかりました")

    # dfの行数が1であることを確認
    assert df.shape[0] == 1

    input_args = process_row(df.iloc[0])
    return input_args


def process_row(row) -> InputArgs:
    """
    Excelファイルの行データをInputArgsクラスに変換します。
    """
    print(row)
    input_args = InputArgs(
        org_name_position=row["組織名称(前 or 後)"],
        organization_type=row["組織名称"],
        company_name_kana=row["法人名(カナ)"],
        company_name=row["法人名"],
        office_type=row["本店 or 支店"],
        branch_office_name_kana=row["支店名称(カナ）"],
        branch_office_name=row["支店名称"],
        zip_code=row["納税地(郵便番号)"],
        prefecture=row["納税地(都道府県)"],
        city=row["納税地(市区町村)"],
        street_address=row["納税地(丁目番地等)"],
        building_name=row["納税地(建物名・号室)"],
        phone_number=row["納税地(電話番号)"],
        tax_office_prefecture=row["提出先税務署(都道府県)"],
        tax_office_name=row["提出先税務署(税務署名)"],
        representative_last_name_kana=row["代表者(姓)(カナ)"],
        representative_first_name_kana=row["代表者(名)(カナ)"],
        representative_last_name=row["代表者(姓)"],
        representative_first_name=row["代表者(名)"],
        representative_zip_code=row["代表者住所(郵便番号)"],
        representative_prefecture=row["代表者住所(都道府県)"],
        representative_city=row["代表者住所(市区町村)"],
        representative_street_address=row["代表者住所(丁目番地等)"],
        representative_building_name=row["代表者住所(建物名・号室)"],
        representative_phone_number=row["代表者住所(電話番号)"],
        head_office_name_position=row["本店組織名称(前 or 後)"],
        head_office_organization_type=row["本店組織名称"],
        head_office_name_kana=row["本店名(カナ)"],
        head_office_name=row["本店名"],
        head_office_zip_code=row["本店住所(郵便番号)"],
        head_office_prefecture=row["本店住所(都道府県)"],
        head_office_city=row["本店住所(市区町村)"],
        head_office_street_address=row["本店住所(丁目番地等)"],
        head_office_building_name=row["本店住所(建物名・号室)"],
        head_office_phone_number=row["本店住所(電話番号)"],
        tax_payment_confirmation_number=row["納税用確認番号"],
        tax_payment_name_kana=row["納税用カナ氏名・名称"],
    )
    return input_args


# メイン関数の呼び出し
if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="法人名を受け取り、Excelファイルからデータを取得"
    )
    parser.add_argument("--corporate_name", type=str, help="法人名")
    args = parser.parse_args()

    main(corporate_name=args.corporate_name)
