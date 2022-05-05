# Boto3の機能を利用するためにboto3をインポート
import boto3
# Comprehendサービスクライアントを作成
comprehend = boto3.client('comprehend')
# 処理対象の文字列
text = input('言語を検出します。文字列を入力してください： ')
# 言語を検出
result = comprehend.detect_dominant_language(Text=text)

# Languageキーを変数に入れる
l = result['Languages']
# getメソッドでLanguageCodeの値を取得する
language = [d.get('LanguageCode') for d in l]

# 辞書の中に言語を追加する
lang = {'de':'ドイツ語', 
        'en':'英語', 
        'es':'スペイン語', 
        'it':'イタリア語', 
        'pt':'ポルトガル語', 
        'fr':'フランス語',
        'ja':'日本語', 
        'ko':'韓国語',
        'hi':'ヒンディー語',
        'ar':'アラビア語',
        'zh':'簡体字中国語',
        'zh-TW':'繫体字中国語'}

# 帰ってきた言語を表示する
print('入力された言語は', lang[language[0]], 'です')
    
