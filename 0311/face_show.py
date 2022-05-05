# boto3、json、sysをインポート
import boto3
import json
import sys
# Pillowのimageモジュールをインポート
from PIL import Image

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
# 出力画像を作成
image_out = Image.new('RGB', (w, h), (200, 200, 200))
# 検出された顔を順番に処理
for face in result['FaceDetails']:
    # バウンディングボックスを取得
    box = face['BoundingBox']
    # 顔の左、上、右、下の座標を計算
    left = int(box['Left']*w)
    top = int(box['Top']*h)
    right = left+int(box['Width']*w)
    bottom = top+int(box['Height']*h)
    # 入力画像から出力画像に顔部分を貼り付け
    image_out.paste(
        image_in.crop((left, top, right, bottom)),
        (left, top))
# 出力画像をファイルに保存
image_out.save('show_'+sys.argv[1])
# 出力画像を表示
image_out.show()
