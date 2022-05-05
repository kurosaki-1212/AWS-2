# boto3、sysをインポート
from email.mime import image
import boto3
import sys
# PillowのImage、ImageDraw、ImageFilterモジュールをインポート
from PIL import Image, ImageDraw

# コマンドライン引数の個数が不適切なら使い方を表示して終了
if len(sys.argv) != 2:
    print('python', sys.argv[0], 'image')
    exit()

# Rekognitionサービスクライアントを作成
rekognition = boto3.client('rekognition')

# 画像ファイルから顔を検出して結果を表示
with open(sys.argv[1], 'rb') as file:
    result = rekognition.detect_faces(
        Image={'Bytes': file.read()})

# 入力画像のファイルを読み込む
image_in = Image.open(sys.argv[1])
# 画像のサイズを取得
w, h = image_in.size
# 検出された顔を順番に処理
for face in result['FaceDetails']:
    # バウンディングボックスを取得
    box = face['BoundingBox']
    # 顔の左、上、右、下の座標を計算
    left = int(box['Left']*w)
    top = int(box['Top']*h)
    right = left+int(box['Width']*w)
    bottom = top+int(box['Height']*h)

    # 顔の位置を切り取る
    im_crop = image_in.crop((left, top, right, bottom))
    # 顔の位置を幅、高さを取得する
    w1, h1 = im_crop.size
    # 小さくしてから普通の大きさに戻す(モザイク)
    im_crop.resize((int(w1 / 10), int(h1 / 10))).resize((w1, h1))
    # モザイクにしたものを貼り付ける
    image_in.paste(im_crop, (w, h))

# 出力画像をファイルに保存
image_in.save('mozaiku_'+sys.argv[1])
# 出力画像を表示
image_in.show()

