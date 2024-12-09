from dataclasses import dataclass


@dataclass
class InputArgs:
    # 1ページ目のフォーム入力
    corporate_number: str = ""
    org_name_position: str = "前"
    organization_type: str = ""
    company_name_kana: str = ""
    company_name: str = ""
    office_type: str = "本店"
    branch_office_name_kana: str = ""
    branch_office_name: str = ""
    zip_code: str = ""
    prefecture: str = ""
    city: str = ""
    street_address: str = ""
    building_name: str = ""
    phone_number: str = ""
    tax_office_prefecture: str = ""
    tax_office_name: str = ""
    # 2ページ目のフォーム入力
    representative_last_name_kana: str = ""
    representative_first_name_kana: str = ""
    representative_last_name: str = ""
    representative_first_name: str = ""
    representative_zip_code: str = ""
    representative_prefecture: str = ""
    representative_city: str = ""
    representative_street_address: str = ""
    representative_building_name: str = ""
    representative_phone_number: str = ""
    # 3ページ目のフォーム入力
    head_office_name_position: str = "前"
    head_office_organization_type: str = ""
    head_office_name_kana: str = ""
    head_office_name: str = ""
    head_office_zip_code: str = ""
    head_office_prefecture: str = ""
    head_office_city: str = ""
    head_office_street_address: str = ""
    head_office_building_name: str = ""
    head_office_phone_number: str = ""
    # 4ページ目のフォーム入力
    password: str = ""
    secret_question: str = ""
    secret_question_answer: str = ""
    establishment_year: str = ""
    establishment_month: str = ""
    establishment_day: str = ""
    show_password: bool = True
    tax_payment_confirmation_number: str = ""
    tax_payment_name_kana: str = ""
    main_mail_address: str = ""
    sub_mail_address1: str = ""
    sub_mail_address2: str = ""
    show_atena: bool = True
    atena: str = ""
    sort_number: str = ""
    reference_matters: str = ""
    is_agent: bool = False
    agent_name: str = ""
    agent_phone_number: str = ""
