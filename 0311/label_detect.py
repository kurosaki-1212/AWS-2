# boto3、json、sysとpillowのimageモジュールをインポート
import boto3
import json
import sys
from PIL import Image

# コマンドライン引数の個数が不適切なら使い方を表示して終了
if len(sys.argv) != 2:
    print('python', sys.argv[0], 'image')
    exit()

# Rekogniionサービスクライアントを作成
rekognition = boto3.client('rekognition')

# 画像ファイルを開く
with open(sys.argv[1], 'rb') as file:
    # 画像内の物を検出　detect_faceにすると顔を検出
    result = rekognition.detect_labels(Image={'Bytes': file.read()})
    # 結果を整形して取得
    print(json.dumps(result, indent=4))

# 入力画像のファイルを読み込む
image_in = Image.open(sys.argv[1])

# 画像のサイズを取得
w, h = image_in.size
# 検出されたラベルを順番に取得
for label in result['Labels']:
    # ラベルに対応する物が検出されたかどうかを調べる
    if label['Instances']:
        # 出力画像を作成
        image_out = Image.new('RGB', (w, h), (200, 200, 200))
        # 検出された物を順番に取得
        for instance in label['Instances']:
            # バウンディングボックスを取得
            box = instance['BoundingBox']
            # 物の左、上。右、下の座標を計算
            left = int(box['Left']*w)
            top = int(box['Top']*h)
            right = left+int(box['Width']*w)
            bottom = top+int(box['Height']*h)
            # 入力画像から出力画像に物の部分を貼り付け
            image_out.paste(
                image_in.crop((left, top, right, bottom)),
                (left, top))

        # 出力画像のファイル名
        name = 'label_'+label['Name']+'_'+sys.argv[1]
        # ファイル名を表示
        print(name)
        # 出力画像をファイルに保存
        image_out.save(name)
