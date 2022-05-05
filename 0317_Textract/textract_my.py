# Boto3の機能を利用するためにboto3をインポート
import boto3
# オブジェクトを整形して表示するためにjsonをインポート
import json
# コマンドライン引数を整理するためにsysをインポート
import sys
# 画像を読み書きするためにPillowのImageモジュールをインポート
from PIL import Image

# コマンドライン引数の個数hが不適切ならば使い方を表示して終了
if len(sys.argv) != 2:
    print('python', sys.argv[0], 'image')
    exit()

# Textractサービスクライアントを作成
textract = boto3.client('textract')
# 画像ファイルを開く
with open(sys.argv[1], 'rb') as file:
    # 文字列を検出
    result = textract.detect_document_text(
        Document={'Bytes': file.read()})

# 入力画像のファイルを読み込む
image_in = Image.open(sys.argv[1])
# 画像のサイズを取得
w, h = image_in.size
# 出力画像を作成
image_out = Image.new('RGB', (w, h), (200, 200, 200))

# 行数、列数の初期値を０にする
gyou = 0
count = 0
# 空のリストを作成する
list = []
# 検出されたブロックを順番に処理
for block in result['Blocks']:
    # ブロックタイプが行かどうかを調べる
    if block['BlockType'] == 'LINE': # 1行分得
        # 行をカウントする
        gyou += 1
        # 文字を分割してリストに入れる
        sp = block['Text'].split()
        list.append(sp)
# 二次元配列の中の個数を計算する
for item in list:
    count += len(item)

# 行数と単語数を表示する
print('切り出したテキスト')
print('行数 = ', gyou, '、',  '単語数 = ', count)

# 検出されたブロックを順番に処理
for block in result['Blocks']:
    # ブロックタイプが行かどうかを調べる
    if block['BlockType'] == 'LINE': # 1行分
        # バウンディボックスを取得
        box = block['Geometry']['BoundingBox'] # Geometry の中の BoundingBox をデータを取得
        # 文字列の左、上、右、下の座標を計算
        left = int(box['Left']*w)
        top = int(box['Top']*h)
        right = left+int(box['Width']*w)
        bottom = top+int(box['Height']*h)
        # 入力画像から出力画像に文字列の部分を貼り付け
        image_out.paste(
            image_in.crop((left, top, right, bottom)), (left, top))
        # 文字列の内容を表示
        print(block['Text']) # 読み取った１行分の文字を表示
