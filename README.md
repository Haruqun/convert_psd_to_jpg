```markdown
# PSD to JPG Converter

このプログラムは、PSDファイルをJPG形式に一括変換するPythonスクリプトです。変換の際、アスペクト比を維持しながら余白を埋めるように画像サイズを変更します。

## 機能

- PSDファイルをJPG形式に一括変換
- アスペクト比を維持しながら余白を埋めるように画像サイズを変更
- 画像の引き伸ばしを防止し、画質を維持

## 必要条件

- Python 3.6以上
- Pillow
- psd-tools

## インストール

1. このリポジトリをクローンまたはダウンロードします。
2. 以下のコマンドを実行して、必要なライブラリをインストールします。

```
pip install -r requirements.txt
```

## 使用方法

1. `convert_psd_to_jpg.py`の`PSD_FOLDER`と`JPG_FOLDER`の値を、実際のPSDファイルとJPGファイルを保存するフォルダのパスに置き換えます。
2. 必要に応じて、`ASPECT_RATIO`と`BACKGROUND_COLOR`の値を調整します。
3. 以下のコマンドを実行して、PSDファイルをJPG形式に変換します。

```
python convert_psd_to_jpg.py
```

変換が完了すると、指定された出力ディレクトリにJPG形式の画像が保存されます。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細については、[LICENSE](LICENSE)ファイルを参照してください。
```

requirements.txt:

```
Pillow>=9.0.0
psd-tools>=1.9.22
```
