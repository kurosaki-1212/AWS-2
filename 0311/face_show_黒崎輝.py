# boto3、json、sysをインポート
import boto3
import json
import sys
# PillowのImageモジュールをインポート
from PIL import Image
# PillowのImageDrawモジュールをインポート
from PIL import ImageDraw

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
    print(json.dumps(result, indent=4))

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
    # ImageDrawモデルを生成
    draw = ImageDraw.Draw(image_in)
    # 赤い四角で囲う位置を決める
    draw.rectangle((left, top, right, bottom), outline='red', width=4)

# 出力画像をファイルに保存
image_in.save('show_'+sys.argv[1])
# 出力画像を表示
image_in.show()
