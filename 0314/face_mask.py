# boto3、sysをインポート
import boto3
import sys

# PillowのImageモジュールをインポート
from PIL import Image

# コマンドライン引数の個数が不適切なら使い方を表示して終了
if len(sys.argv) != 4:
    print('python', sys.argv[0], 'image')
    exit()

# Rekognitionサービスクライアントを作成
rekognition = boto3.client('rekognition')

# 画像ファイルから顔を検出して結果を表示
with open(sys.argv[1], 'rb') as file:
    result = rekognition.detect_faces(
        Image={'Bytes': file.read()})

# 入力画像のファイルを読み込む
im1 = Image.open(sys.argv[1])
im2 = Image.open(sys.argv[2])
mask_im = Image.open(sys.argv[3]).resize(im2.size).convert('L')
# 画像のサイズを取得
w, h = im1.size
# 検出された顔を順番に処理
for face in result['FaceDetails']:
    # バウンディングボックスを取得
    box = face['BoundingBox']
    # 顔の左、上、右、下の座標を計算
    left = int(box['Left']*w)
    top = int(box['Top']*h)
    right = left+int(box['Width']*w)
    bottom = top+int(box['Height']*h)

    im1.paste(im2, (left, top), mask_im)
    im1.save('pien_mask.jpg', quality=95)

# 出力画像をファイルに保存
im1.save('show_'+sys.argv[1])
# 出力画像を表示
im1.show()
