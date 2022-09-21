from requests import request
import os
import time

class Bot:

    def __init__(self, token: str = None):
        self.token = os.getenv('TELEGRAM_BOT_TOKEN') if token is None else token
        
        # Prepare all urls that would be used so we don't have to do it in each method
        self.base_url = 'https://api.telegram.org/bot{0}/{1}'
        self.get_updates_url = self.base_url.format(self.token, 'getUpdates')
        self.send_message_url = self.base_url.format(self.token, 'sendMessage')
        self.timeout = 10

    def __make_request(self, request_method, url, data=None, params=None, timeout=None):
        
        if timeout is None:
            timeout = self.timeout
        return request(request_method, url, data=data, params=params, timeout=timeout)
    
    def __acknowledge_update(self, update_id):
        payload = {'offset' : update_id + 1}
        r = self.__make_request('get', self.get_updates_url, data=payload)

        if r.status_code != 200:
            raise Exception(f'An error occured with message acknowledgement')
        return True
    
    def send_msg(self, to:str, msg:str) -> None:
        
        payload = {'chat_id' : to, 'text' : msg}  

        r = self.__make_request('post', self.send_message_url, data=payload)

        if r.status_code != 200:
            raise Exception(f'An error occured with message notification - {r.status_code}')
        return True

    def __execute_command(self):
        # TO DO
        # Implement method that executes a command on the host machine
        pass

    def listen(self):

        while True:
            time.sleep(1)
            r = self.__make_request('get', self.get_updates_url)

            if r.json()['result']:
                update_id = r.json()['result'][0]['update_id']
                self.__acknowledge_update(update_id)
                self.execute_command()

                


bot = Bot('')
bot.listen()