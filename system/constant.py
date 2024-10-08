import os

# チャンネルアクセストークン
CHANNEL_ACCESS_TOKEN = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN")

# ログインチャンネルID
LOGIN_CHANNEL_ID = os.environ.get("LINE_LOGIN_CHANNEL_ID")

#LLMキー
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# リクエストヘッダー
HEADERS_JSON = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + CHANNEL_ACCESS_TOKEN
}
HEADERS_X_WWW_FORM_URLENCODED = {
    'Content-Type': 'application/json',
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
MODE_QUIZ = 'quiz'
MODE_ANALYZE = 'analyze'

# メッセージ受信テキスト
MESSAGE_TRIGGER = '>'
MESSAGE_CHAT_START = '> チャットを開始する'
MESSAGE_CHAT_FINISH = '> チャットを終了する'
MESSAGE_QUIZ = '> クイズに挑戦！'
MESSAGE_ANALYZE = '> 文構造を分析する'
MESSAGE_TRANSLATION = '> 和訳する'

# メッセージ返信テキスト
RESPONSE_FOLLOW = 'お友だち登録ありがとうございます！\n一緒に言語を学びましょう。'
RESPONSE_CHOOSE_LANG = '下記メニューから学習したい言語を選択してください。'
RESPONSE_MENU_NOT_SELECTED = '現在、モードが選択されていません。\n下部メニューからメニューを選択してください。'
RESPONSE_ANALYZE_START = '文の分析を開始しました。テキストを送信してください。\n(メッセージ送信後、自動的にオフになります。)'
RESPONSE_REANALYZE = '続けて分析する場合は下部のボタンを押してください。'
RESPONSE_QUIZ = '次の言葉の読みを選ぼう。'
RESPONSE_GOOD = '正解！'
RESPONSE_BAT = '残念！'
RESPONSE_ONE_MORE_QUIZ = '続けてもう一問する場合は下部のボタンを押してください。'
RESPONSE_DAIRY_QUIZ = '今日の一問！'
RESPONSE_CHAT_START = 'チャットを始めましょう！\n(あまり長い返答は返ってきません。)'
RESPONSE_CHAT_FINISH = 'チャットを終了します。'
RESPONSE_NO_USER_WORD = '辞書にデータがありません。\n分析を使用して単語を増やしてください。'

def RESPONSE_CHOOSED_LANG(language):
    return language + "を選択しました！\nこれから頑張りましょう！！"

# DeepL言語略称
JAPANESE = 'JA'
ENGLISH = 'EN'
ENGLISH_TO = 'EN-US'
KOREAN = 'KO'
CHINESE = 'ZH'

# 言語名
JA_LANG = {
    JAPANESE: '日本語',
    ENGLISH: '英語',
    KOREAN: '韓国語',
    CHINESE: '中国語'
}

# 記号
SYMBOL_COMMA = ','
SYMBOL_PERIOD = '.'
SYMBOL_QUESTION = '?'
SYMBOL_EXCLAMATION = '!'
SYMBOL_EM_SPACE = '　'
SYMBOL_EN_SPACE = ' '

# フロントエンド
FRONT_ID_TOKEN = 'idToken'

# その他
LANGUAGE_TRIGGER = '語'
ANARYZE_RESULT = '分析結果'
ARPABET_TO_IPA = {
    'AA': 'ɑ', 'AE': 'æ', 'AH': 'ʌ', 'AO': 'ɔ', 'AW': 'aʊ',
    'AY': 'aɪ', 'B': 'b', 'CH': 'tʃ', 'D': 'd', 'DH': 'ð',
    'EH': 'ɛ', 'ER': 'ɝ', 'EY': 'eɪ', 'F': 'f', 'G': 'ɡ',
    'HH': 'h', 'IH': 'ɪ', 'IY': 'i', 'JH': 'dʒ', 'K': 'k',
    'L': 'l', 'M': 'm', 'N': 'n', 'NG': 'ŋ', 'OW': 'oʊ',
    'OY': 'ɔɪ', 'P': 'p', 'R': 'ɹ', 'S': 's', 'SH': 'ʃ',
    'T': 't', 'TH': 'θ', 'UH': 'ʊ', 'UW': 'u', 'V': 'v',
    'W': 'w', 'Y': 'j', 'Z': 'z', 'ZH': 'ʒ',
    # ストレスは無視するため、数字を除去
    '0': '', '1': '', '2': ''
}
