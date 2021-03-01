import vk_api
import sys
import time
import requests
from rich.console import Console
from captchasolving import captcha_handler
from banner import banner
from functions import message_count, time_set, get_users


api_key = 'RuCaptcha Api Token'
TOKEN = "Kate Mobile Token"


vk = vk_api.VkApi(token=TOKEN, captcha_handler=captcha_handler).get_api()
console = Console()
console.print(banner, style='cyan')


timer = time_set()
message_num = message_count()
user_list = get_users(vk)


message = input('Введите сообщение для отправки: ')
tasks = [f'''Сообщения отправляются"{i[0]}"'''  for i in user_list]


with console.status("[bold green]Отсылаю сообщения...") as status:      
	for user in user_list:

		task = tasks.pop(0)
		time.sleep(timer)
		console.log(f"{task}")

		for _ in range(message_num):
			try:
			    vk.messages.send(user_id=user[1], random_id=0, message=message)
			    time.sleep(timer)
			except:
				time.sleep(timer)

console.print('Работа завершена.', style='bold green')
