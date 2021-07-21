i=2
while i >= 0:
	password = input('請輸入密碼:')
	if password == 'a123456':
		print('登入成功!')
		break
	else:
		if i == 0:
			break
	print('密碼錯誤，還有', i, '次機會，加油!')
	i = i - 1
