from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import random
app = Flask(__name__)

line_bot_api = LineBotApi('CYDAvPiHlJ0MQjpT0eBs/Gd/ZOXG+DgBFp9qdVHtyoM1xhiE/kkzP4PgCnylwq4hsfn+gTjUml7FU1ZORXFz/pMH9sF5Xw+MzLjAP+OWQs/wLaNTJyayh5Pqac+spxvP/uyByAxZfFWADW0yc1O5yAdB04t89/1O/w1cDnyilFU=')
line_handler = WebhookHandler('893d665afbd8eb35b7308e7a8950b9f8')

@app.route('/')
def home():
    return 'Hello World'

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        line_handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


def myG():
    myW=['你好','吃飽了嗎','天氣如何']
    return random.choice(myW)

@line_handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    getA=event.message.text        

    if getA =='0' :        
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=str(myG())))      
    elif event.message.text == "2":        
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='333'))
        
    elif event.message.text=='3':            
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='344'))
        
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="輸入0"))
 
if __name__ == "__main__":
    app.run()