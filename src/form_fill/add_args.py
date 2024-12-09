import argparse


def add_page1_args(parser: argparse.ArgumentParser) -> None:
    """
    ページ1の引数を追加します。

    Parameters
    ----------
    parser : argparse.ArgumentParser
        引数を追加するArgumentParserオブジェクト
    """
    parser.add_argument(
        "--corporate_number", type=str, nargs="?", default="", help="法人番号"
    )
    parser.add_argument(
        "--org_name_position",
        type=str,
        nargs="?",
        default="前",
        help="組織名称が法人名称の前後どちらに付くかを指定 ('前' または '後')。デフォルトは'前'。",
    )
    parser.add_argument(
        "--organization_type",
        type=str,
        nargs="?",
        default="",
        help="組織の種類",
    )
    parser.add_argument(
        "--company_name_kana",
        type=str,
        nargs="?",
        default="",
        help="法人名称（フリガナ）",
    )
    parser.add_argument(
        "--company_name", type=str, nargs="?", default="", help="法人名称"
    )
    parser.add_argument(
        "--office_type",
        type=str,
        nargs="?",
        default="本店",
        help="本店または支店。デフォルトは 本店。",
    )
    parser.add_argument(
        "--branch_office_name_kana",
        type=str,
        nargs="?",
        default="",
        help="支店等名称（フリガナ）",
    )
    parser.add_argument(
        "--branch_office_name",
        type=str,
        nargs="?",
        default="",
        help="支店等名称",
    )
    parser.add_argument("--zip_code", type=str, nargs="?", default="", help="郵便番号")
    parser.add_argument(
        "--prefecture", type=str, nargs="?", default="", help="都道府県"
    )
    parser.add_argument("--city", type=str, nargs="?", default="", help="市区町村")
    parser.add_argument(
        "--street_address", type=str, nargs="?", default="", help="丁目番地等"
    )
    parser.add_argument(
        "--building_name", type=str, nargs="?", default="", help="建物名・号室"
    )
    parser.add_argument(
        "--phone_number", type=str, nargs="?", default="", help="電話番号"
    )
    parser.add_argument(
        "--tax_office_prefecture",
        type=str,
        nargs="?",
        default="",
        help="提出先税務署の都道府県",
    )
    parser.add_argument(
        "--tax_office_name",
        type=str,
        nargs="?",
        default="",
        help="提出先税務署の名称",
    )


def add_page2_args(parser: argparse.ArgumentParser) -> None:
    """
    ページ2の引数を追加します。

    Parameters
    ----------
    parser : argparse.ArgumentParser
        引数を追加するArgumentParserオブジェクト
    """
    parser.add_argument(
        "--representative_last_name_kana",
        type=str,
        nargs="?",
        default="",
        help="代表者氏名カナ（姓）",
    )
    parser.add_argument(
        "--representative_first_name_kana",
        type=str,
        nargs="?",
        default="",
        help="代表者氏名カナ（名）",
    )
    parser.add_argument(
        "--representative_last_name",
        type=str,
        nargs="?",
        default="",
        help="代表者氏名（姓）",
    )
    parser.add_argument(
        "--representative_first_name",
        type=str,
        nargs="?",
        default="",
        help="代表者氏名（名）",
    )
    parser.add_argument(
        "--representative_zip_code",
        type=str,
        nargs="?",
        default="",
        help="代表者住所の郵便番号",
    )
    parser.add_argument(
        "--representative_prefecture",
        type=str,
        nargs="?",
        default="",
        help="代表者住所の都道府県",
    )
    parser.add_argument(
        "--representative_city",
        type=str,
        nargs="?",
        default="",
        help="代表者住所の市区町村",
    )
    parser.add_argument(
        "--representative_street_address",
        type=str,
        nargs="?",
        default="",
        help="代表者住所の丁目番地等",
    )
    parser.add_argument(
        "--representative_building_name",
        type=str,
        nargs="?",
        default="",
        help="代表者住所の建物名・号室",
    )
    parser.add_argument(
        "--representative_phone_number",
        type=str,
        nargs="?",
        default="",
        help="代表者電話番号",
    )


def add_page3_args(parser: argparse.ArgumentParser) -> None:
    """
    ページ3の引数を追加します。

    Parameters
    ----------
    parser : argparse.ArgumentParser
        引数を追加するArgumentParserオブジェクト
    """
    parser.add_argument(
        "--head_office_name_position",
        type=str,
        nargs="?",
        default="前",
        help="組織名称が本店名称の前後どちらに付くかを指定 ('前' または '後')。デフォルトは'前'。",
    )
    parser.add_argument(
        "--head_office_organization_type",
        type=str,
        nargs="?",
        default="",
        help="本店の組織の種類",
    )
    parser.add_argument(
        "--head_office_name_kana",
        type=str,
        nargs="?",
        default="",
        help="本店名称（フリガナ）",
    )
    parser.add_argument(
        "--head_office_name", type=str, nargs="?", default="", help="本店名称"
    )
    parser.add_argument(
        "--head_office_zip_code",
        type=str,
        nargs="?",
        default="",
        help="本店住所の郵便番号",
    )
    parser.add_argument(
        "--head_office_prefecture",
        type=str,
        nargs="?",
        default="",
        help="本店住所の都道府県",
    )
    parser.add_argument(
        "--head_office_city", type=str, nargs="?", default="", help="本店住所の市区町村"
    )
    parser.add_argument(
        "--head_office_street_address",
        type=str,
        nargs="?",
        default="",
        help="本店住所の丁目番地等",
    )
    parser.add_argument(
        "--head_office_building_name",
        type=str,
        nargs="?",
        default="",
        help="本店住所の建物名・号室",
    )
    parser.add_argument(
        "--head_office_phone_number",
        type=str,
        nargs="?",
        default="",
        help="本店電話番号",
    )


def add_page4_args(parser: argparse.ArgumentParser) -> None:
    """
    ページ4の引数を追加します。

    Parameters
    ----------
    parser : argparse.ArgumentParser
        引数を追加するArgumentParserオブジェクト
    """
    parser.add_argument(
        "--password", type=str, nargs="?", default="", help="パスワード"
    )
    parser.add_argument(
        "--secret_question", type=str, nargs="?", default="", help="秘密の質問"
    )
    parser.add_argument(
        "--secret_question_answer",
        type=str,
        nargs="?",
        default="",
        help="秘密の質問の答え",
    )
    parser.add_argument(
        "--establishment_year",
        type=str,
        nargs="?",
        default="",
        help="設立年",
    )
    parser.add_argument(
        "--establishment_month",
        type=str,
        nargs="?",
        default="",
        help="設立月",
    )
    parser.add_argument(
        "--establishment_day",
        type=str,
        nargs="?",
        default="",
        help="設立日",
    )
    parser.add_argument(
        "--show_password",
        type=bool,
        nargs="?",
        default=True,
        help="パスワードを表示するかどうか",
    )
    parser.add_argument(
        "--tax_payment_confirmation_number",
        type=str,
        nargs="?",
        default="",
        help="納税確定番号",
    )
    parser.add_argument(
        "--tax_payment_name_kana",
        type=str,
        nargs="?",
        default="",
        help="納税者名（フリガナ）",
    )
    parser.add_argument(
        "--main_mail_address",
        type=str,
        nargs="?",
        default="",
        help="メインメールアドレス",
    )
    parser.add_argument(
        "--sub_mail_address1",
        type=str,
        nargs="?",
        default="",
        help="サブメールアドレス1",
    )
    parser.add_argument(
        "--sub_mail_address2",
        type=str,
        nargs="?",
        default="",
        help="サブメールアドレス2",
    )
    parser.add_argument(
        "--show_atena",
        type=bool,
        nargs="?",
        default=True,
        help="宛名を表示するかどうか",
    )
    parser.add_argument("--atena", type=str, nargs="?", default="", help="宛名")
    parser.add_argument("--sort_number", type=str, nargs="?", default="", help="並び順")
    parser.add_argument(
        "--reference_matters", type=str, nargs="?", default="", help="参照事項"
    )
    parser.add_argument(
        "--is_agent",
        type=bool,
        nargs="?",
        default=False,
        help="代理人かどうか",
    )
    parser.add_argument(
        "--agent_name", type=str, nargs="?", default="", help="代理人名"
    )
    parser.add_argument(
        "--agent_phone_number",
        type=str,
        nargs="?",
        default="",
        help="代理人電話番号",
    )


# メインの関数
def setup_args() -> argparse.Namespace:
    """
    引数を追加します。

    Parameters
    ----------
    parser : argparse.ArgumentParser
        引数を追加するArgumentParserオブジェクト
    """
    parser = argparse.ArgumentParser(
        description="e-tax Webフォームに値を入力するツール"
    )
    add_page1_args(parser)
    add_page2_args(parser)
    add_page3_args(parser)
    add_page4_args(parser)
    args = parser.parse_args()
    return args
