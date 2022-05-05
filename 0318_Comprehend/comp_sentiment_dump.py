# Boto3の機能を利用するためにBoto3をインポート
import boto3
# 結果を整形して表示するためにjsonをインポート
import json
# Comprehendサービスクライアントを作成
comprehend = boto3.client('comprehend')
# 処理対象の文字列
text = "I'm looking forward to visiting Japan next summer."
# 感情を分析
result = comprehend.detect_sentiment(Text=text, LanguageCode='en')
# 結果を整形して表示
print(json.dumps(result, indent=4))
