from Class.input import InputArgs
from input_actions import (
    click_element,
    wait_and_fill_input_field,
    wait_and_select_dropdown,
)
from selenium import webdriver
from selenium.webdriver.common.by import By


def select_organization_position(
    driver: webdriver.Chrome, org_name_position: str = "前", timeout: int = 10
) -> None:
    """
    組織名称が法人名称の前後どちらに付くか選択します。
    デフォルトは'前'。
    """
    print(f"組織名称の位置を選択します: {org_name_position}")
    if org_name_position == "前":
        click_element(driver, By.ID, "gSoshikimeiZen", timeout)
    elif org_name_position == "後":
        click_element(driver, By.ID, "gSoshikimeiGo", timeout)
    else:
        raise ValueError("org_name_positionは'前'または'後'で指定してください。")


def select_organization_name(
    driver: webdriver.Chrome, organization_type: str, timeout: int = 10
) -> None:
    """
    組織名称をリストから選択します。
    """
    print(f"組織名称を選択します: {organization_type}")
    wait_and_select_dropdown(driver, By.ID, "gSoshikimei", organization_type, timeout)


def fill_corporate_name(
    driver: webdriver.Chrome, company_name_kana: str, timeout: int = 10
) -> None:
    """
    法人名称（フリガナ）を入力します。
    """
    print(f"法人名称（フリガナ）を入力します: {company_name_kana}")
    wait_and_fill_input_field(
        driver, By.ID, "gHojinmeiKana", company_name_kana, timeout
    )


def fill_corporate_name_kanji(
    driver: webdriver.Chrome, company_name: str, timeout: int = 10
) -> None:
    """
    法人名称を入力します。
    """
    print(f"法人名称を入力します: {company_name}")
    wait_and_fill_input_field(driver, By.ID, "gHojinmei", company_name, timeout)


def select_main_or_branch_office(
    driver: webdriver.Chrome, office_type: str = "本店", timeout: int = 10
) -> None:
    """
    本店または支店を選択します。デフォルトは'本店'。
    """
    print(f"本店または支店を選択します: {office_type}")
    if office_type == "本店":
        click_element(driver, By.ID, "gHonten", timeout)
    elif office_type == "支店":
        click_element(driver, By.ID, "gSiten", timeout)
    else:
        raise ValueError("office_typeは'本店'または'支店'で指定してください。")


def fill_corporate_number(
    driver: webdriver.Chrome, corporate_number: str, timeout: int = 10
) -> None:
    """
    法人番号を入力します。
    """
    print(f"法人番号を入力します: {corporate_number}")
    wait_and_fill_input_field(driver, By.ID, "gHjnNum", corporate_number, timeout)


def fill_branch_office_name_kana(
    driver: webdriver.Chrome, branch_office_name_kana: str, timeout: int = 10
) -> None:
    """
    支店等名称（フリガナ）を入力します。
    """
    print(f"支店等名称（フリガナ）を入力します: {branch_office_name_kana}")
    wait_and_fill_input_field(
        driver, By.ID, "gShitenmeiKana", branch_office_name_kana, timeout
    )


def fill_branch_office_name(
    driver: webdriver.Chrome, branch_office_name: str, timeout: int = 10
) -> None:
    """
    支店等名称を入力します。
    """
    print(f"支店等名称を入力します: {branch_office_name}")
    wait_and_fill_input_field(driver, By.ID, "gShitenmei", branch_office_name, timeout)


# 納税地情報
def fill_zip_code(driver: webdriver.Chrome, zip_code: str, timeout: int = 10) -> None:
    """
    郵便番号を入力します。
    """
    print(f"郵便番号を入力します: {zip_code}")
    wait_and_fill_input_field(driver, By.ID, "gNChiZip3", zip_code[:3], timeout)
    wait_and_fill_input_field(driver, By.ID, "gNChiZip4", zip_code[3:], timeout)


def select_prefecture(
    driver: webdriver.Chrome, prefecture: str, timeout: int = 10
) -> None:
    """
    都道府県を選択します。
    """
    print(f"都道府県を選択します: {prefecture}")
    wait_and_select_dropdown(driver, By.ID, "gNChiTodohuken", prefecture, timeout)


def fill_city(driver: webdriver.Chrome, city: str, timeout: int = 10) -> None:
    """
    市区町村を入力します。
    """
    print(f"市区町村を入力します: {city}")
    wait_and_fill_input_field(driver, By.ID, "gNChiAdd1", city, timeout)


def fill_street_address(
    driver: webdriver.Chrome, street_address: str, timeout: int = 10
) -> None:
    """
    丁目番地等を入力します。
    """
    print(f"丁目番地等を入力します: {street_address}")
    wait_and_fill_input_field(driver, By.ID, "gNChiAdd2", street_address, timeout)


def fill_building_name(
    driver: webdriver.Chrome, building_name: str, timeout: int = 10
) -> None:
    """
    建物名・号室を入力します。
    """
    print(f"建物名・号室を入力します: {building_name}")
    wait_and_fill_input_field(driver, By.ID, "gNChiAdd3", building_name, timeout)


def fill_phone_number(
    driver: webdriver.Chrome, phone_number: str, timeout: int = 10
) -> None:
    """
    電話番号を入力します。
    """
    print(f"電話番号を入力します: {phone_number}")
    wait_and_fill_input_field(driver, By.ID, "gNChiTel1", phone_number[:3], timeout)
    wait_and_fill_input_field(driver, By.ID, "gNChiTel2", phone_number[3:7], timeout)
    wait_and_fill_input_field(driver, By.ID, "gNChiTel3", phone_number[7:], timeout)


# 提出先税務署
def select_tax_office_prefecture(
    driver: webdriver.Chrome, prefecture: str, timeout: int = 10
) -> None:
    """
    提出先の税務署の都道府県を選択します。
    """
    print(f"提出先の税務署の都道府県を選択します: {prefecture}")
    wait_and_select_dropdown(driver, By.ID, "gTTodohuken", prefecture, timeout)


def select_tax_office_name(
    driver: webdriver.Chrome, tax_office_name: str, timeout: int = 10
) -> None:
    """
    提出先の税務署の名称を入力します。
    """
    print(f"提出先の税務署の名称を選択します: {tax_office_name}")
    wait_and_select_dropdown(driver, By.ID, "gTZeimushomei", tax_office_name, timeout)


# 1ページ目のフォーム入力
def fill_form_fields_1(
    driver: webdriver.Chrome,
    input_args: InputArgs,
) -> None:
    """
    1ページ目のフォームのすべてのフィールドを入力します。
    """

    # 法人番号の入力
    fill_corporate_number(driver, input_args.corporate_number)

    # 組織名称の位置を選択
    select_organization_position(driver, input_args.org_name_position)

    # 組織名称の選択
    select_organization_name(driver, input_args.organization_type)

    # 法人名称（フリガナ）の入力
    fill_corporate_name(driver, input_args.company_name_kana)

    # 法人名称の入力
    fill_corporate_name_kanji(driver, input_args.company_name)

    # 本店または支店の選択
    select_main_or_branch_office(driver, input_args.office_type)

    if input_args.office_type == "支店":
        # 支店等名称（フリガナ）の入力
        fill_branch_office_name_kana(driver, input_args.branch_office_name_kana)
        # 支店等名称の入力
        fill_branch_office_name(driver, input_args.branch_office_name)

    # 郵便番号の入力
    fill_zip_code(driver, input_args.zip_code)

    # 都道府県の選択
    select_prefecture(driver, input_args.prefecture)

    # 市区町村の入力
    fill_city(driver, input_args.city)

    # 丁目番地等の入力
    fill_street_address(driver, input_args.street_address)

    # 建物名・号室の入力
    fill_building_name(driver, input_args.building_name)

    # 電話番号の入力
    fill_phone_number(driver, input_args.phone_number)

    # 提出先税務署の都道府県の選択
    select_tax_office_prefecture(driver, input_args.tax_office_prefecture)

    # 提出先税務署の名称の選択
    select_tax_office_name(driver, input_args.tax_office_name)


def fill_representative_last_name_kana(
    driver: webdriver.Chrome, representative_last_name_kana: str, timeout: int = 10
) -> None:
    """
    代表者のフリガナ（姓）を入力します。
    """
    print(f"代表者のフリガナ（姓）を入力します: {representative_last_name_kana}")
    wait_and_fill_input_field(
        driver, By.ID, "gDSeiKana", representative_last_name_kana, timeout
    )


def fill_representative_first_name_kana(
    driver: webdriver.Chrome, representative_first_name_kana: str, timeout: int = 10
) -> None:
    """
    代表者のフリガナ（名）を入力します。
    """
    print(f"代表者のフリガナ（名）を入力します: {representative_first_name_kana}")
    wait_and_fill_input_field(
        driver, By.ID, "gDmeiKana", representative_first_name_kana, timeout
    )


def fill_representative_last_name(
    driver: webdriver.Chrome, representative_last_name: str, timeout: int = 10
) -> None:
    """
    代表者の氏名（姓）を入力します。
    """
    print(f"代表者の氏名（姓）を入力します: {representative_last_name}")
    wait_and_fill_input_field(driver, By.ID, "gDSei", representative_last_name, timeout)


def fill_representative_first_name(
    driver: webdriver.Chrome, representative_first_name: str, timeout: int = 10
) -> None:
    """
    代表者の氏名（名）を入力します。
    """
    print(f"代表者の氏名（名）を入力します: {representative_first_name}")
    wait_and_fill_input_field(
        driver, By.ID, "gDmei", representative_first_name, timeout
    )


def fill_representative_zip_code(
    driver: webdriver.Chrome, representative_zip_code: str, timeout: int = 10
) -> None:
    """
    代表者住所の郵便番号を入力します。
    """
    print(f"代表者住所の郵便番号を入力します: {representative_zip_code}")
    wait_and_fill_input_field(
        driver, By.ID, "gDZip3", representative_zip_code[:3], timeout
    )
    wait_and_fill_input_field(
        driver, By.ID, "gDZip4", representative_zip_code[3:], timeout
    )


def select_representative_prefecture(
    driver: webdriver.Chrome, representative_prefecture: str, timeout: int = 10
) -> None:
    """
    代表者住所の都道府県を選択します。
    """
    print(f"代表者住所の都道府県を選択します: {representative_prefecture}")
    wait_and_select_dropdown(
        driver, By.ID, "gDTodohuken", representative_prefecture, timeout
    )


def fill_representative_city(
    driver: webdriver.Chrome, representative_city: str, timeout: int = 10
) -> None:
    """
    代表者住所の市区町村を入力します。
    """
    print(f"代表者住所の市区町村を入力します: {representative_city}")
    wait_and_fill_input_field(driver, By.ID, "gDAdd1", representative_city, timeout)


def fill_representative_street_address(
    driver: webdriver.Chrome, representative_street_address: str, timeout: int = 10
) -> None:
    """
    代表者住所の丁目番地等を入力します。
    """
    print(f"代表者住所の丁目番地等を入力します: {representative_street_address}")
    wait_and_fill_input_field(
        driver, By.ID, "gDAdd2", representative_street_address, timeout
    )


def fill_representative_building_name(
    driver: webdriver.Chrome, representative_building_name: str, timeout: int = 10
) -> None:
    """
    代表者住所の建物名・号室を入力します。
    """
    print(f"代表者住所の建物名・号室を入力します: {representative_building_name}")
    wait_and_fill_input_field(
        driver, By.ID, "gDAdd3", representative_building_name, timeout
    )


def fill_representative_phone_number(
    driver: webdriver.Chrome, representative_phone_number: str, timeout: int = 10
) -> None:
    """
    代表者の電話番号を入力します。
    """
    print(f"代表者の電話番号を入力します: {representative_phone_number}")
    wait_and_fill_input_field(
        driver, By.ID, "gDTel1", representative_phone_number[:3], timeout
    )
    wait_and_fill_input_field(
        driver, By.ID, "gDTel2", representative_phone_number[3:7], timeout
    )
    wait_and_fill_input_field(
        driver, By.ID, "gDTel3", representative_phone_number[7:], timeout
    )


def fill_form_fields_2(
    driver: webdriver.Chrome,
    input_args: InputArgs,
) -> None:
    """
    2ページ目のフォームのすべてのフィールドを入力します。
    """
    # 代表者のフリガナ（姓）の入力
    fill_representative_last_name_kana(driver, input_args.representative_last_name_kana)

    # 代表者のフリガナ（名）の入力
    fill_representative_first_name_kana(
        driver, input_args.representative_first_name_kana
    )

    # 代表者の氏名（姓）の入力
    fill_representative_last_name(driver, input_args.representative_last_name)

    # 代表者の氏名（名）の入力
    fill_representative_first_name(driver, input_args.representative_first_name)

    # 代表者住所の郵便番号の入力
    fill_representative_zip_code(driver, input_args.representative_zip_code)

    # 代表者住所の都道府県の選択
    select_representative_prefecture(driver, input_args.representative_prefecture)

    # 代表者住所の市区町村の入力
    fill_representative_city(driver, input_args.representative_city)

    # 代表者住所の丁目番地等の入力
    fill_representative_street_address(driver, input_args.representative_street_address)

    # 代表者住所の建物名・号室の入力
    fill_representative_building_name(driver, input_args.representative_building_name)

    # 代表者の電話番号の入力
    fill_representative_phone_number(driver, input_args.representative_phone_number)


def select_head_office_position(
    driver: webdriver.Chrome, head_office_name_position: str = "前", timeout: int = 10
) -> None:
    """
    本店名称が法人名称の前後どちらに付くか選択します。
    デフォルトは'前'。
    """
    print(f"本店名称の位置を選択します: {head_office_name_position}")
    if head_office_name_position == "前":
        click_element(driver, By.ID, "gHSoshikimeiZen", timeout)
    elif head_office_name_position == "後":
        click_element(driver, By.ID, "gHSoshikimeiGo", timeout)
    else:
        raise ValueError(
            "head_office_name_positionは'前'または'後'で指定してください。"
        )


def select_head_office_organization_type(
    driver: webdriver.Chrome, head_office_organization_type: str, timeout: int = 10
) -> None:
    """
    本店の組織形態を選択します。
    """
    print(f"本店の組織形態を選択します: {head_office_organization_type}")
    wait_and_select_dropdown(
        driver, By.ID, "gHSoshikimei", head_office_organization_type, timeout
    )


def fill_head_office_name_kana(
    driver: webdriver.Chrome, head_office_name_kana: str, timeout: int = 10
) -> None:
    """
    本店名称（フリガナ）を入力します。
    """
    print(f"本店名称（フリガナ）を入力します: {head_office_name_kana}")
    wait_and_fill_input_field(
        driver, By.ID, "gHHojinmeiKana", head_office_name_kana, timeout
    )


def fill_head_office_name(
    driver: webdriver.Chrome, head_office_name: str, timeout: int = 10
) -> None:
    """
    本店名称を入力します。
    """
    print(f"本店名称を入力します: {head_office_name}")
    wait_and_fill_input_field(driver, By.ID, "gHHojinmei", head_office_name, timeout)


def fill_head_office_zip_code(
    driver: webdriver.Chrome, head_office_zip_code: str, timeout: int = 10
) -> None:
    """
    本店の郵便番号を入力します。
    """
    print(f"本店の郵便番号を入力します: {head_office_zip_code}")
    wait_and_fill_input_field(
        driver, By.ID, "gHZip3", head_office_zip_code[:3], timeout
    )
    wait_and_fill_input_field(
        driver, By.ID, "gHZip4", head_office_zip_code[3:], timeout
    )


def select_head_office_prefecture(
    driver: webdriver.Chrome, head_office_prefecture: str, timeout: int = 10
) -> None:
    """
    本店の都道府県を選択します。
    """
    print(f"本店の都道府県を選択します: {head_office_prefecture}")
    wait_and_select_dropdown(
        driver, By.ID, "gHTodohuken", head_office_prefecture, timeout
    )


def fill_head_office_city(
    driver: webdriver.Chrome, head_office_city: str, timeout: int = 10
) -> None:
    """
    本店の市区町村を入力します。
    """
    print(f"本店の市区町村を入力します: {head_office_city}")
    wait_and_fill_input_field(driver, By.ID, "gHAdd1", head_office_city, timeout)


def fill_head_office_street_address(
    driver: webdriver.Chrome, head_office_street_address: str, timeout: int = 10
) -> None:
    """
    本店の丁目番地等を入力します。
    """
    print(f"本店の丁目番地等を入力します: {head_office_street_address}")
    wait_and_fill_input_field(
        driver, By.ID, "gHAdd2", head_office_street_address, timeout
    )


def fill_head_office_building_name(
    driver: webdriver.Chrome, head_office_building_name: str, timeout: int = 10
) -> None:
    """
    本店の建物名・号室を入力します。
    """
    print(f"本店の建物名・号室を入力します: {head_office_building_name}")
    wait_and_fill_input_field(
        driver, By.ID, "gHAdd3", head_office_building_name, timeout
    )


def fill_head_office_phone_number(
    driver: webdriver.Chrome, head_office_phone_number: str, timeout: int = 10
) -> None:
    """
    本店の電話番号を入力します。
    """
    print(f"本店の電話番号を入力します: {head_office_phone_number}")
    wait_and_fill_input_field(
        driver, By.ID, "gHTel1", head_office_phone_number[:3], timeout
    )
    wait_and_fill_input_field(
        driver, By.ID, "gHTel2", head_office_phone_number[3:7], timeout
    )
    wait_and_fill_input_field(
        driver, By.ID, "gHTel3", head_office_phone_number[7:], timeout
    )


def fill_form_fields_3(
    driver: webdriver.Chrome,
    input_args: InputArgs,
) -> None:
    """
    3ページ目のフォームのすべてのフィールドを入力します。
    """
    # 本店名称の位置を選択
    select_head_office_position(driver, input_args.head_office_name_position)

    # 本店の組織形態の選択
    select_head_office_organization_type(
        driver, input_args.head_office_organization_type
    )

    # 本店名称（フリガナ）の入力
    fill_head_office_name_kana(driver, input_args.head_office_name_kana)

    # 本店名称の入力
    fill_head_office_name(driver, input_args.head_office_name)

    # 本店の郵便番号の入力
    fill_head_office_zip_code(driver, input_args.head_office_zip_code)

    # 本店の都道府県の選択
    select_head_office_prefecture(driver, input_args.head_office_prefecture)

    # 本店の市区町村の入力
    fill_head_office_city(driver, input_args.head_office_city)

    # 本店の丁目番地等の入力
    fill_head_office_street_address(driver, input_args.head_office_street_address)

    # 本店の建物名・号室の入力
    fill_head_office_building_name(driver, input_args.head_office_building_name)

    # 本店の電話番号の入力
    fill_head_office_phone_number(driver, input_args.head_office_phone_number)


def fill_password(driver: webdriver.Chrome, password: str, timeout: int = 10) -> None:
    """
    パスワードを入力します。
    """
    print("パスワードを入力します")
    wait_and_fill_input_field(driver, By.ID, "gPwd", password, timeout)
    wait_and_fill_input_field(driver, By.ID, "gPwd2", password, timeout)


def select_secret_question(
    driver: webdriver.Chrome, secret_question: str, timeout: int = 10
) -> None:
    """
    秘密の質問を選択します。
    """
    print(f"秘密の質問を選択します: {secret_question}")
    wait_and_select_dropdown(driver, By.ID, "gRmndQus", secret_question, timeout)


def fill_secret_question_answer(
    driver: webdriver.Chrome, secret_question_answer: str, timeout: int = 10
) -> None:
    """
    秘密の質問の回答を入力します。
    """
    print(f"秘密の質問の回答を入力します: {secret_question_answer}")
    wait_and_fill_input_field(
        driver, By.ID, "gRmndAns", secret_question_answer, timeout
    )


def select_establishment_year(
    driver: webdriver.Chrome, establishment_year: str, timeout: int = 10
) -> None:
    """
    設立年を選択します。
    """
    print(f"設立年を選択します: {establishment_year}")
    wait_and_select_dropdown(driver, By.ID, "gSNen", establishment_year, timeout)


def select_establishment_month(
    driver: webdriver.Chrome, establishment_month: str, timeout: int = 10
) -> None:
    """
    設立月を選択します。
    """
    print(f"設立月を選択します: {establishment_month}")
    wait_and_select_dropdown(driver, By.ID, "gSTuki", establishment_month, timeout)


def select_establishment_day(
    driver: webdriver.Chrome, establishment_day: str, timeout: int = 10
) -> None:
    """
    設立日を選択します。
    """
    print(f"設立日を選択します: {establishment_day}")
    wait_and_select_dropdown(driver, By.ID, "gSBi", establishment_day, timeout)


def select_show_password(
    driver: webdriver.Chrome, show_password: bool = True, timeout: int = 10
) -> None:
    """
    パスワードを表示するかどうかを選択します。
    デフォルトはTrue。
    """
    print(f"パスワードを表示するかどうかを選択します: {show_password}")
    if show_password:
        click_element(driver, By.ID, "gHyoujiSuru", timeout)
    else:
        click_element(driver, By.ID, "gHyoujiShinai", timeout)


def fill_tax_payment_confirmation_number(
    driver: webdriver.Chrome, tax_payment_confirmation_number: str, timeout: int = 10
) -> None:
    """
    納税証明書交付申請の確認番号を入力します。
    """
    print(
        f"納税証明書交付申請の確認番号を入力します: {tax_payment_confirmation_number}"
    )
    wait_and_fill_input_field(
        driver, By.ID, "gNKakuninBango", tax_payment_confirmation_number, timeout
    )


# tax_payment_name_kana: str = ""
#     main_mail_address: str = ""
#     sub_mail_address1: str = ""
#     sub_mail_address2: str = ""
#     show_atena: bool = True
#     atena: str = ""
#     sort_number: str = ""
#     reference_matters: str = ""
#     is_agent: bool = False
#     agent_name: str = ""
#     agent_phone_number: str = ""


def fill_tax_payment_name_kana(
    driver: webdriver.Chrome, tax_payment_name_kana: str, timeout: int = 10
) -> None:
    """
    納税者名（フリガナ）を入力します。
    """
    print(f"納税者名（フリガナ）を入力します: {tax_payment_name_kana}")
    wait_and_fill_input_field(
        driver, By.ID, "gNShimeiKana", tax_payment_name_kana, timeout
    )


def fill_main_mail_address(
    driver: webdriver.Chrome, main_mail_address: str, timeout: int = 10
) -> None:
    """
    メインメールアドレスを入力します。
    """
    print(f"メインメールアドレスを入力します: {main_mail_address}")
    wait_and_fill_input_field(driver, By.ID, "gMailAdd", main_mail_address, timeout)
    wait_and_fill_input_field(driver, By.ID, "gMailAdd2", main_mail_address, timeout)


def fill_sub_mail_address1(
    driver: webdriver.Chrome, sub_mail_address1: str, timeout: int = 10
) -> None:
    """
    サブメールアドレス1を入力します。
    """
    print(f"サブメールアドレス1を入力します: {sub_mail_address1}")
    wait_and_fill_input_field(
        driver, By.ID, "gSubMailAdd1_1", sub_mail_address1, timeout
    )
    wait_and_fill_input_field(
        driver, By.ID, "gSubMailAdd1_2", sub_mail_address1, timeout
    )


def fill_sub_mail_address2(
    driver: webdriver.Chrome, sub_mail_address2: str, timeout: int = 10
) -> None:
    """
    サブメールアドレス2を入力します。
    """
    print(f"サブメールアドレス2を入力します: {sub_mail_address2}")
    wait_and_fill_input_field(
        driver, By.ID, "gSubMailAdd2_1", sub_mail_address2, timeout
    )
    wait_and_fill_input_field(
        driver, By.ID, "gSubMailAdd2_2", sub_mail_address2, timeout
    )


def select_show_atena(
    driver: webdriver.Chrome, show_atena: bool = True, timeout: int = 10
) -> None:
    """
    宛名を表示するかどうかを選択します。
    デフォルトはTrue。
    """
    print(f"宛名を表示するかどうかを選択します: {show_atena}")
    if show_atena:
        click_element(driver, By.ID, "gMailToEnabled", timeout)
    else:
        click_element(driver, By.ID, "gMailToDisabled", timeout)


def fill_atena(driver: webdriver.Chrome, atena: str, timeout: int = 10) -> None:
    """
    宛名を入力します。
    """
    print(f"宛名を入力します: {atena}")
    wait_and_fill_input_field(driver, By.ID, "gMailTo", atena, timeout)


def fill_sort_number(
    driver: webdriver.Chrome, sort_number: str, timeout: int = 10
) -> None:
    """
    並び順を入力します。
    """
    print(f"並び順を入力します: {sort_number}")
    wait_and_fill_input_field(driver, By.ID, "gSeiriBango", sort_number, timeout)


def fill_reference_matters(
    driver: webdriver.Chrome, reference_matters: str, timeout: int = 10
) -> None:
    """
    参考事項を入力します。
    """
    print(f"参考事項を入力します: {reference_matters}")
    wait_and_fill_input_field(driver, By.ID, "gSankoJiko", reference_matters, timeout)


def select_is_agent(
    driver: webdriver.Chrome, is_agent: bool = False, timeout: int = 10
) -> None:
    """
    代理送信される場合はチェックボックスにチェックを入れます。
    デフォルトはFalse。
    """
    print(f"代理送信される場合はチェックボックスにチェックを入れます: {is_agent}")
    if is_agent:
        click_element(driver, By.ID, "gZEnabled", timeout)


def fill_agent_name(
    driver: webdriver.Chrome, agent_name: str, timeout: int = 10
) -> None:
    """
    代理送信者の氏名を入力します。
    """
    print(f"代理送信者の氏名を入力します: {agent_name}")
    wait_and_fill_input_field(driver, By.ID, "gZShimei", agent_name, timeout)


def fill_agent_phone_number(
    driver: webdriver.Chrome, agent_phone_number: str, timeout: int = 10
) -> None:
    """
    代理送信者の電話番号を入力します。
    """
    print(f"代理送信者の電話番号を入力します: {agent_phone_number}")
    wait_and_fill_input_field(
        driver, By.ID, "gZshiTel1", agent_phone_number[:3], timeout
    )
    wait_and_fill_input_field(
        driver, By.ID, "gZshiTel2", agent_phone_number[3:7], timeout
    )
    wait_and_fill_input_field(
        driver, By.ID, "gZshiTel3", agent_phone_number[7:], timeout
    )


def fill_form_fields_4(
    driver: webdriver.Chrome,
    input_args: InputArgs,
) -> None:
    """
    4ページ目のフォームのすべてのフィールドを入力します。
    """
    # パスワードの入力
    fill_password(driver, input_args.password)

    # 秘密の質問の選択
    if input_args.secret_question != "":
        select_secret_question(driver, input_args.secret_question)
        fill_secret_question_answer(driver, input_args.secret_question_answer)

    # 設立年の選択
    select_establishment_year(driver, input_args.establishment_year)
    # 設立月の選択
    select_establishment_month(driver, input_args.establishment_month)
    # 設立日の選択
    select_establishment_day(driver, input_args.establishment_day)
    # パスワードを表示するかどうかの選択
    select_show_password(driver, input_args.show_password)
    # 納税証明書交付申請の確認番号の入力
    fill_tax_payment_confirmation_number(
        driver, input_args.tax_payment_confirmation_number
    )
    # 納税者名（フリガナ）の入力
    fill_tax_payment_name_kana(driver, input_args.tax_payment_name_kana)
    # メインメールアドレスの入力
    fill_main_mail_address(driver, input_args.main_mail_address)
    if input_args.main_mail_address != "":
        # サブメールアドレス1の入力
        fill_sub_mail_address1(driver, input_args.sub_mail_address1)
        # サブメールアドレス2の入力
        fill_sub_mail_address2(driver, input_args.sub_mail_address2)
    # 宛名の入力
    if input_args.show_atena:
        select_show_atena(driver, input_args.show_atena)
        fill_atena(driver, input_args.atena)
    # 整理番号の入力
    fill_sort_number(driver, input_args.sort_number)
    # 参考事項の入力
    fill_reference_matters(driver, input_args.reference_matters)

    # 代理送信される場合の選択
    if input_args.is_agent:
        select_is_agent(driver, input_args.is_agent)
        # 代理送信者の氏名の入力
        fill_agent_name(driver, input_args.agent_name)
        # 代理送信者の電話番号の入力
        fill_agent_phone_number(driver, input_args.agent_phone_number)
