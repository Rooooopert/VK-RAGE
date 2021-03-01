def captcha_handler(captcha, api_key):
    post = request.post('https://rucaptcha.com/in.php', data={'key': api_key, 'method': 'base64',
     'body': base64.b64.encode(captcha.get_image()).decode("utf-8")})

    captcha_id = post.text[3:]
    coef = 0

    while True:
    	key = requests.get('https://rucaptcha.com/res.php', params={'key': api_key, 'action': 'get', 'id': str(captcha_id)})
    	if 'OK' in key.text:
    		break

    	if coef > 20:
    		print('Не разгадана')
    		break

    	time.sleep(1)
    	coef += 1

    try:
    	captcha.try_again(key.text.split('|')[1])
    	return True

    except Exception as e:
    	print('Ошибка', e)
    	return False