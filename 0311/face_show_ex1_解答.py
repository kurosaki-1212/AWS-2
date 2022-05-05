# boto3 をインポート
import boto3
# json をインポート
import json
# sys をインポート
import sys
# pillow の Image モジュールと ImageDraw モジュールをインポート
from PIL import Image, ImageDraw

# コマンドラインの引数チェック
if len(sys.argv) != 2:
    # プログラム名を含む引数の個数が２でないとき
    # 実行形式を表示
    print('python', sys.argv[0], 'image')
     # プログラムを強制終了
    exit()

# rekognition サービスクライアントを作成
rekognition = boto3.client('rekognition')
# 画像ファイルをオープン
with open(sys.argv[1], 'rb') as file:
    # 画像ファイルから顔を検出する
    result = rekognition.detect_faces(
        Image={'Bytes': file.read()})
    # 検出結果を整形して表示
    print(json.dumps(result, indent=4))

# 画像ファイルをオープン
image_in = Image.open(sys.argv[1])
# 画像のサイズを取得
w, h = image_in.size
# ImageDrawオブジェクトを生成
image_draw = ImageDraw.Draw(image_in)

# 検出された顔を順番に処理
for face in result['FaceDetails']:
    # バウンディングボックスを取得
    box = face['BoundingBox']
    # 顔の左の座標を取得
    left = int(box['Left']*w)
    # 顔の上の座標を取得
    top = int(box['Top']*h)
    # 顔の右の座標を取得
    right = left+int(box['Width']*w)
    # 顔の下の座標を取得
    bottom = top+int(box['Height']*h)
    # 顔の部分を四角で囲む
    image_draw.rectangle([(left, top), (right, bottom)],
        outline='red', width=2)
# 出力画像をファイルに保存
image_in.save('show_'+sys.argv[1])
# 出力画像を表示
image_in.show()
