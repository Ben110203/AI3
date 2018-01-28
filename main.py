from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

# Replace by your channel secret and access token from Line Developers console -> Channel settings.
LINE_CHANNEL_SECRET = '75ce6e8ea5e559381fa9830575592c74'
LINE_CHANNEL_ACCESS_TOKEN = 'znDynalgVQMv77Ag4Hz0ULgU8GxgkNjXfEPHJIWCve7RkVakYMCbauBZAAoNiGZi5wXZ1t75fgmeUSLB5GiINb9a+/uB82bnB78GhHxHct382fsmYBXkr1bpQ8G/Jc47eq92MH+41/8seuveiIoMsgdB04t89/1O/w1cDnyilFU='
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)


@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # Replace the text by what you want to say
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="Hello world"))
     #   TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
