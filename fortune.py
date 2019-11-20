def fortune():
	import random
	messages = ['It is CERTAIN.',
    'It is likely.',
    'Yes, definitely.',
    'Reply hazy, try again.',
    'Ask again later.',
    'Concentrate, then ask again.',
    'My reply is NO.',
    'Outlook is not so good.',
    'Very doubtful.']

	r = random.randint(1, 9)
	ansExit = ''
	#while ansExit != 'n':
		#print('Welcome to Ben\'s Crystal Ball. Tell me what it is you want to know.')
		#request = input(">> ")
		#print('\n')
		#print('Your Fortune:  ' +
	return messages[random.randint(0, len(messages) - 1)]
		#print('\n')
		#print('Do you want to ask another?  (Y/n)')
		#ansExit = input(">> ")
	#print('Be wary, traveller.')

