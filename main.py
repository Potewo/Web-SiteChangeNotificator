import sys
import csv
import urllib.request, urllib.error
from bs4 import BeautifulSoup
from notify import LINENotifyBot
import logging

# ログの記録するフォーマットを決める
log_format = '%(levelname)s : %(asctime)s : %(message)s'
logging.basicConfig(filename='パス/log.log', level=logging.INFO, format=log_format)
logging.info('START')
url = "変更を検知したいサイトのURL"
bot = LINENotifyBot('アクセストークン')
try:
    # HTMLを取得する
    html = urllib.request.urlopen(url)
    # HTMLのステータスコード（正常に取得できたかどうか）を記録する
    logging.info('HTTP STATUS CODE: ' + str(html.getcode()))
except:
    # 取得に失敗した場合もLINEに通知してログを取る
    bot.send('URLの取得に失敗しました')
    # 念の為強制終了
    sys.exit(1)
soup = BeautifulSoup(html, "html.parser")
# HTMLの中からaタグのみを抽出
tags = soup.find_all("a")
links = list()
# 前回取ったリンク
oldlinks = set()
# 今回とったリンク
newlinks = set()
for tag in tags:
    # aタグからリンクのURLのみを取り出す。
    links.append(tag.get('href'))
try:
    # 前回取得したリンクをファイルから読み込む
    with open('パス/links.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            oldlinks = set(row)
        logging.info('Opened csv file"')
except:
    # 何かしら失敗した場合はLINEに通知、ログ
    bot.send('ファイルの取得に失敗しました')
    logging.error('Failed to get csv file')

try:
    # 今回取得したリンクを記録する（上書き）
    with open('パス/links.csv', 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(links)
    logging.info('Writed csv file')
except:
    # 失敗したら通知、ログ
    bot.send('ファイルの書き込みに失敗しました')
    logging.error('Failed to write csv file')
    sys.exit(1)

try:
    newlinks = set(links)
    # setで引き算をすると差分がわかる
    # 今回新しく発見したリンク
    added = newlinks - oldlinks
    # 前回あったけど今回はなくなったリンク
    removed = oldlinks - newlinks
    for link in added:
        # 追加されたら通知
        # 追加されたURL自体もお知らせしようとしたらリンクをむやみに貼るなと書いてあったので一応やめておいた
        bot.send('リンクが追加されました')

    for link in removed:
        # 追加と同様に
        bot.send('リンクが消去されました')

    logging.info('Compared links')

except:
    # 失敗したら…（以下略）
    bot.send('比較に失敗しました')
    logging.error('Failed to compare')
    sys.exit(1)

logging.info('DONE')
