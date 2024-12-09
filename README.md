# この python スクリプトについて
e-tax 開始届出（法人用）　新規 を行うためのスクリプトです。

# 使い方

## 1. 事前準備

### 1.1. python 仮想環境の作成
python の仮想環境を作成し、必要なライブラリをインストールしてください。
以下のコマンドを実行してください。
```bash
# この README.md があるディレクトリに移動.
cd path/to/this/directory # 各自の環境に合わせてください

# 仮想環境を作成
python3 -m venv venv 

# 仮想環境を有効化
source venv/bin/activate 

# ライブラリをインストール
pip3 install -r requirements.txt
```

### 1.2. 設定ファイルの作成
`config/config.yaml.example` を `config/config.yaml` という名前でコピーしてください

### 1.3. 設定ファイルの編集
`config/config.yaml` を編集してください。
詳しくは, [config/README.md](config/README.md) を参照してください。


## 2. python スクリプトを実行
以下のコマンドを実行してください。

```bash
# python3 src/excel_to_form/main.py [法人名] の形式
python3 src/excel_to_form/main.py 山田出版
```

### サンプルスクリプト
サンプルスクリプトを実行することができます。

###### macOS の場合
```bash
bash sample_script/run_form_fill.sh
```
