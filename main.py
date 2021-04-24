import configparser
import random

class UserClass:
	"""docstring for UserClass"""
	username = 'no name'
	remain = 0
	items = []

	def __init__(self, username, remain, items):
		self.username = username
		self.remain = remain
		self.items = items

	def getRemain(self):
		return self.remain

	def getItem(self):
		return self.items

	def addItem(self, itemname):
		self.items.append(itemname)
		return self.items

	def deleteItem(self, itemname):
		if itemname in self.items:
			self.items.remove(itemname)
			return self.items
		else:
			return False

	def checkItem(self, itemname):
		if itemname in self.items:
			return True
		else:
			return False

	def getRemain(self):
		return self.remain

	def deRemain(self, num):
		self.remain -= num
		return self.remain

config = configparser.ConfigParser()
config.read('config.ini')

if(not config.has_section('設定')):
	section1 = '設定'
	config.add_section(section1)
	config.set(section1, 'ゴールまでのマス', '3')
	config.set(section1, '初期所持アイテム', 'double')
	section2 = 'double'
	config.add_section(section2)
	config.set(section2, 'dice', '2')
	path_w = 'config.ini'
	with open(path_w, 'w') as file:
		config.write(file)

def Command(name):
	cmd = input('コマンドを入力 : ')
	if cmd == 'item':
		print('使用するアイテムを選択し、その名前を入力してください。')
		for itemname in name.getItem():
			print(itemname)
		item = input('アイテムを入力 : ')
		if item in name.getItem():
			print('アイテム' + item + 'を使用します。')
			config.read('config.ini')
			dice_effect = int(config[item]['dice'])
			roll_num = random.randrange(1, 7)
			advance = roll_num * dice_effect
			print(str(advance) + 'マス進みます！')
			name.deleteItem(item)
			name.deRemain(advance)
		else:
			print(item + 'は存在しないアイテムです！')
			Command(name)
	elif cmd == 'd':
		roll_num = random.randint(1, 6)
		print('サイコロの目は' + str(roll_num) + 'でした。')
		name.deRemain(roll_num)
	elif cmd == 'itemcheck':
		for itemname in name.getItem():
			print(itemname)
	else:
		print('そのコマンドは存在しません！')
		Command(name)

num = int(input('プレイ人数を教えてください(半角数字) : '))

username = []
player = []
rank = []
goal = 0

config.read('config.ini')
remain = int(config.get('設定', 'ゴールまでのマス'))
item_initial = config.get('設定', '初期所持アイテム')

for n in range(0, num):
	number = n + 1
	x = input('プレイヤー' + str(number) + 'の名前を入力してください : ')
	username.append(x)
	player.append(UserClass(username[n], remain, [item_initial]))

print('ゲームを開始します...')
print('アイテムを使う : item')
print('所持アイテム確認 : itemcheck')
print('さいころをふる : d')

numl = num - 1
while goal <= numl:
	for n in range(0, numl + 1):
		name = player[n]
		print(str(username[n]) + 'のターンです。')
		m = name.getRemain()
		print('残り' + str(m) + 'マスです。')
		Command(name)
		if(name.getRemain() <= 0):
			print(str(username[n]) + 'がゴールしました！')
			goal += 1
			print(str(goal) + '位' + ' ' + str(username[n]))
			rank.append(username[n])
			numl -= 1
			if(goal == num - 1):
				break

for pname in username:
	if(pname not in rank):
		rank.append(pname)

print('ゲームが終了しました。')
print('Result : ')
for n in range(0, num):
	nl = n + 1
	print(str(nl) + '位  :  ' + str(rank[n]))











