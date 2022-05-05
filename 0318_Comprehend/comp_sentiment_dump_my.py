# Boto3の機能を利用するためにBoto3をインポート
import boto3
# Comprehendサービスクライアントを作成
comprehend = boto3.client('comprehend')
# 空のリスト作成
sentensu = []
# #が入力されるまでループ処理をする
while True:
    text = input('文字列を入力 = ')
    if text == '#':
        break
    sentensu.append(text)

# リストの中身を順番にループさせる
for i in sentensu:
    # 感情を分析
    result = comprehend.detect_sentiment(Text=i, LanguageCode='en')
    # 結果を表示する
    print('入力された文字列 = ', i)
    print('推測した感情 = ', result['Sentiment'])
    print('肯定的な感情なスコア = ', result['SentimentScore']['Positive'])
    print('否定的な感情なスコア = ', result['SentimentScore']['Negative'])
    print('中立的な感情なスコア = ', result['SentimentScore']['Neutral'])
    print('混じった感情のスコア = ', result['SentimentScore']['Mixed'])