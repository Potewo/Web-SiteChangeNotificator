# Web-SiteChangeNotificator
Webサイトが変更されたことを検知してLINEに通知します。
It detects changes on your website and notifies to your LINE.

## 解説記事 explanation article
[【自動化】WEBサイトの変更を検知してLINEに通知する](https://qiita.com/Potewo/items/431cea6b954652adb0b3)

## Required
- python3
  - urllib
  - beautifulsoup4

## 使い方 Usage
1. このリポジトリをクローンする clone this repository
1. `パス`をクローンしたリポジトリのパスに置き換える replace `パス` with your path to cloned repository
1. `変更を検知したいURL`を自分が変更を検知したいURLに置き換える replace `変更を検知したいURL` with your URL to detect the change
1. [LINE Notify](https://notify-bot.line.me/ja/)でサインアップし、アクセストークンを入手する Sign up [LINE Notify](https://notify-bot.line.me/en/) and get API token
1. `アクセストークン`を入手したアクセストークンに置き換える replace `アクセストークン` with API token you got
1. cronのようなもので定期実行する run this program regularly with something like cron

