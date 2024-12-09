project_path=$(cd $(dirname $0)/..; pwd)

# /src/read_from_excel/main.py へのパス
main_py_path=$project_path/src/read_from_excel/main.py

arg='蟹蟹'

# 実行
python3 $main_py_path --corporate_name $arg