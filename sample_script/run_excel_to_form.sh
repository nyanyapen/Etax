project_path=$(cd $(dirname $0)/..; pwd)

# /src/excel_to_form/main.py へのパス
main_py_path=$project_path/src/excel_to_form/main.py

arg='蟹蟹'

# 実行
python3 $main_py_path $arg