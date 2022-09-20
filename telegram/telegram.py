import requests
import os


class Bot:

    BASE_URL = 'https://api.telegram.org/bot{token}/{method}'

    def __init__(
        self,
        token: str = None
    ):
        self.token = os.getenv('TELEGRAM_BOT_TOKEN') if token is None else token

    def send_msg(self, to:str, msg:str) -> None:
        
        url = self.BASE_URL.format(token=self.token, method='sendMessage')

        payload = {
            'chat_id' : to,
            'text' : msg
        }

        r = requests.post(url, data=payload)

        if r.status_code != 200:
            raise Exception(f'An error occured with message notification - {r.status_code}')
        return True