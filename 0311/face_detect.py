import boto3 # AWSのサービスを呼び出すためのライブラリ
import json
import sys # コマンドライン引数

if len(sys.argv) != 2:
    print('python', sys.argv[0], 'image') # エラーメッセージ
    exit() # プログラムを終了

rekognition = boto3.client('rekognition')

with open(sys.argv[1], 'rb') as file: # Read Binary の略
    result = rekognition.detect_faces(Image={'Bytes': file.read()}) # AWSに画像を送る
    print(json.dumps(result, indent=4))
