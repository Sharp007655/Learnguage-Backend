import os

# チャンネルアクセストークン
CHANNEL_ACCESS_TOKEN = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN")

# リクエストヘッダー
HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + CHANNEL_ACCESS_TOKEN
}

# リクエストメソッド
POST = 'POST'
GET = 'GET'

# リクエストタイプ
MESSAGE = 'message'
TEXT = 'text'
FOLLOW = 'follow'
UNFOLLOW = 'unfollow'

# 使用モード
MODE_CHAT = 'chat'

# メッセージ受信テキスト
MESSAGE_TRIGGER = '>'
MESSAGE_CHAT_START = '> チャットを開始する'
MESSAGE_CHAT_FINISH = '> チャットを終了する'
MESSAGE_QUIZ = '> クイズに挑戦！'
MESSAGE_ANALYZE = '> 文構造を分析する'

# メッセージ返信テキスト
RESPONSE_FOLLOW = 'お友達登録ありがとうございます！\n一緒に言語を学びましょう。'
RESPONSE_CHAT_NOT_STARTED = '現在、チャットモードがスタートされていません。\n下部メニューからチャットを開始してください。'
