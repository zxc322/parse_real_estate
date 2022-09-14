from parse_app.telegram_send import send_dump_to_telegram
from parse_app.settings import bot_token, chat_id


send_dump_to_telegram(bot_token, chat_id, 'docker_real_estate.gz')


