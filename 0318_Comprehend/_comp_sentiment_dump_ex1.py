# 各種ライブラリのインポート
import boto3
import json

# Comprehendサービスクライアントを作成
comprehend = boto3.client('comprehend', 'us-east-2')

# 処理対象の文字列を設定
# 複数文字列を保存するリストの初期化
texts = []
# '#'が入力するまで繰り返す
while True:
  # 文字列を入力
  text = input('文字列を入力 = ')
  # 入力された文字列が '#' ならブレーク
  if text == '#':
    break
  # 入力された文字列を追加
  texts.append(text)

# 複数行文字列の感情を分析
for text in texts:
  # 感情を分析
  result = comprehend.detect_sentiment(Text=text, LanguageCode='en')
  # 結果を表示
  print('入力された文字列 = {}'.format(text))
  # 検出された感情を表示
  print('推測した感情 = {}'.format(result['Sentiment']))
  # 感情ごとのスコアを表示
  score = result['SentimentScore']
  print('肯定的な感情のスコア = {}'.format(score['Positive']))
  print('否定的な感情のスコア = {}'.format(score['Negative']))
  print('中立的な感情のスコア = {}'.format(score['Neutral']))
  print('混じった感情のスコア = {}'.format(score['Mixed']))