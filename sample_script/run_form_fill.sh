project_path=$(cd $(dirname $0)/..; pwd)

# /src/form_fill/main.py へのパス
main_py_path=$project_path/src/form_fill/main.py

arg=''

# 法人番号
corporate_number=''
arg="$arg --corporate_number $corporate_number"

# org_name_position
org_name_position='前'
arg="$arg --org_name_position $org_name_position"

# organaizeion_type
organization_type='株式会社'
arg="$arg --organization_type $organization_type"

# company_name_kana
company_name_kana='ニャ'
arg="$arg --company_name_kana $company_name_kana"

# company_name
company_name='猫猫'
arg="$arg --company_name $company_name"

# office_type
office_type='支店'
arg="$arg --office_type $office_type"

# branch_office_name_kana
branch_office_name_kana='ナニシテン'
arg="$arg --branch_office_name_kana $branch_office_name_kana"

# branch_office_name
branch_office_name='何支店'
arg="$arg --branch_office_name $branch_office_name"

# zip_code
zip_code='1234567'
arg="$arg --zip_code $zip_code"

# prefecture
prefecture='東京都'
arg="$arg --prefecture $prefecture"

# city
city='千代田区丸の内'
arg="$arg --city $city"

# street_address
street_address='1-1-1'
arg="$arg --street_address $street_address"

# building_name
building_name='東京ビル1F'
arg="$arg --building_name $building_name"

# phone_number
phone_number='09012345678'
arg="$arg --phone_number $phone_number"

# tax_office_prefecture
tax_office_prefecture='東京都'
arg="$arg --tax_office_prefecture $tax_office_prefecture"

# tax_office_name
tax_office_name='品川'
arg="$arg --tax_office_name $tax_office_name"

##### page 2

# 代表者氏名カナ
representative_last_name_kana='ヤマダ'
representative_first_name_kana='アキト'
arg="$arg --representative_last_name_kana $representative_last_name_kana --representative_first_name_kana $representative_first_name_kana"

# 代表者氏名
representative_last_name='山田'
representative_first_name='明人'
arg="$arg --representative_last_name $representative_last_name --representative_first_name $representative_first_name"

# 代表者住所
representative_zip_code='1234567'
representative_prefecture='東京都'
representative_city='千代田区丸の内'
representative_street_address='1-1-1'
representative_building_name='東京ビル1F'
arg="$arg --representative_zip_code $representative_zip_code --representative_prefecture $representative_prefecture --representative_city $representative_city --representative_street_address $representative_street_address --representative_building_name $representative_building_name"

# 代表者電話番号
representative_phone_number='09012345678'
arg="$arg --representative_phone_number $representative_phone_number"

##### page 3

##### page 4
password='password1234'
arg="$arg --password $password"

show_password='True'
arg="$arg --show_password $show_password"

tax_payment_confirmation_number='123456'
arg="$arg --tax_payment_confirmation_number $tax_payment_confirmation_number"

main_mail_address='ayanokoji@kimimaro.com'
arg="$arg --main_mail_address $main_mail_address"

# 最後に main.py を実行
echo "python3 $main_py_path $arg"
echo
python3 $main_py_path $arg
