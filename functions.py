def message_count():
	try:
	    message_num = int(input('Укажите кол-во сообщений одному пользователю: '))
	    return message_num
	except:
		print('Данные введены неверно. Попробуйте еще раз.')
		message_count()


def time_set():
	try:
	    btw_time = int(input('Укажите время между сообщениями(в сек): '))
	    return btw_time
	except:
		print('Данные введены неверно. Попробуйте еще раз.')
		time_set()


def get_users(vk):
    with open('users.txt', 'rt') as f:
        user_list = f.read().strip().split(';')
        del user_list[-1]

        ids = vk.users.get(user_ids=','.join(user_list))
        ids = [(info['first_name'] + ' ' + info['last_name'], info['id']) for info in ids]

        return ids