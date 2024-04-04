import os
from PIL import Image
from psd_tools import PSDImage

# 定数でディレクトリを指定
PSD_FOLDER = "/Users/xxxxx/Desktop/psd"
JPG_FOLDER = "/Users/xxxxxx/Desktop/jpg"
ASPECT_RATIO = (6, 4)
BACKGROUND_COLOR = (255, 255, 255)  # 背景色（白）

def convert_psd_to_jpg(psd_folder, jpg_folder, aspect_ratio=ASPECT_RATIO):
    # PSDファイルが格納されているフォルダを走査
    for filename in os.listdir(psd_folder):
        if filename.endswith(".psd"):
            psd_path = os.path.join(psd_folder, filename)
            jpg_path = os.path.join(jpg_folder, f"{os.path.splitext(filename)[0]}.jpg")

            # PSDファイルを開く
            psd = PSDImage.open(psd_path)
            img = psd.compose()

            # 画像のアスペクト比を計算
            width, height = img.size
            current_ratio = width / height

            # 目標のアスペクト比と比較し、必要に応じて余白を追加
            if current_ratio != aspect_ratio[0] / aspect_ratio[1]:
                target_width = int(height * aspect_ratio[0] / aspect_ratio[1])
                target_height = int(width * aspect_ratio[1] / aspect_ratio[0])

                if target_width > width:
                    new_width = target_width
                    new_height = height
                else:
                    new_width = width
                    new_height = target_height

                # 新しい画像を作成し、中央に元の画像を配置
                new_img = Image.new("RGB", (new_width, new_height), BACKGROUND_COLOR)
                left = (new_width - width) // 2
                top = (new_height - height) // 2
                new_img.paste(img, (left, top))
                img = new_img

            # JPG形式で保存
            img.convert("RGB").save(jpg_path, "JPEG", quality=90)

    print("変換が完了しました。")

# 使用例
convert_psd_to_jpg(PSD_FOLDER, JPG_FOLDER)