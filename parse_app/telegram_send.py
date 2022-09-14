import requests
from datetime import datetime


def send_dump_to_telegram(bot_token, chat_id, file_name):
    with open(file_name, "rb") as file:
        files = {"document":file}
        now = datetime.now()
        title = f"dumped data from parse_app\n{now}"
        chat_id = chat_id
        r = requests.post('https://api.telegram.org/bot' + bot_token + '/sendDocument' , data={"chat_id":chat_id, "caption": title}, files=files)
        if r.status_code != 200:
            raise Exception("send error")
