print('Hello, Django girls!')
if 5 > 2:
	print('5 is indeed greater than 2')
else:
	print('5 is not greater than 2')
name = 'Gabi'
if name == 'Ola' :
	print('Hey Ola')
elif name == 'Gabi' :
	print('Hey Gabi')
else:
	print('Hey anonymus')
def hi():
	print('Hi there!')
	print('How are you?')
hi()
def hi(name):
	if name == 'Ola':
		print('Hi Ola')
	elif name == 'Gabi' :
		print('Hi Gabi')
	else:
		print('Hi anonymus!')
hi("Gabi")
def hi(name):
	print('Hi ' + name + '!')
hi("Rachel")
girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
	hi (name)
	print('Next girl')
for i in range(1, 6):
	print(i)