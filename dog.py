class Dog(object):
	# 初始化方法 创建对象的时候调用
	def __init__(self,name):
		self.name = name

	def game(self):
		print(self.name+"在玩耍")

class XiaoTianDog(Dog):
	def game(self):
		print(self.name+"在天上玩耍")

class Person(object):
	def __init__(self,name):
		self.name = name

	def game_with_dog(self,dog):
		print("%s和%s在玩耍"%(self.name,dog.name))


#wancai = Dog("旺财")
feitianwancai = XiaoTianDog("飞天旺财")

xiaoming = Person("小明")

xiaoming.game_with_dog(feitianwancai)




