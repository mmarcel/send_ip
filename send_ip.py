from dotenv import load_dotenv
import requests
import os

load_dotenv()

class TelegramBot:
    def __init__(self):
        telegram_token = os.getenv('TELEGRAM_TOKEN')
        self.url_base = f'https://api.telegram.org/bot{telegram_token}/'

    def responder(self, resposta, chat_id):
        link_de_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_de_envio)

def main():
    ip_file_path = os.getenv('IP_FILE_PATH')
    with open(ip_file_path, "r") as arquivo:
        current_ip = str(arquivo.readline())
        arquivo.close()
        try:
            r = requests.get('https://api.ipify.org')
            new_ip = r.text
            if new_ip != current_ip:
                with open(ip_file_path, "w") as arquivo:
                    arquivo.write(new_ip)
                    arquivo.close()

                chat_id = os.getenv('CHAT_ID')
                bot = TelegramBot()
                bot.responder(new_ip, chat_id)
        except Exception as ex:
            exit()

if __name__ == "__main__":
    main()