import sys
try:
    sys.argv[1]
    print('OKです')
except:
    print('コマンドライン引数を入力してください')