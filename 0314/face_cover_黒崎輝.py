# boto3、sysをインポート
import boto3
import sys

# PillowのImageモジュールをインポート
from PIL import Image

# コマンドライン引数の個数が不適切なら使い方を表示して終了
if len(sys.argv) != 3:
    print('python', sys.argv[0], 'image')
    exit()

# Rekognitionサービスクライアントを作成
rekognition = boto3.client('rekognition')

# 画像ファイルから顔を検出して結果を表示
with open(sys.argv[1], 'rb') as file:
    result = rekognition.detect_faces(
        Image={'Bytes': file.read()})

# 入力画像のファイルを読み込む
image1_in = Image.open(sys.argv[1])
image2_in = Image.open(sys.argv[2])
# 画像のサイズを取得
w, h = image1_in.size
# 検出された顔を順番に処理
for face in result['FaceDetails']:
    # バウンディングボックスを取得
    box = face['BoundingBox']
    # 顔の左、上、右、下の座標を計算
    left = int(box['Left']*w)
    top = int(box['Top']*h)
    right = left+int(box['Width']*w)
    bottom = top+int(box['Height']*h)

    # 画像を顔の位置に張り付ける
    image1_in.paste(image2_in, (left, top))

# 出力画像をファイルに保存
image1_in.save('show_'+sys.argv[1])
# 出力画像を表示
image1_in.show()
