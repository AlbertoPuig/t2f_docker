class UserStory(object):

	def __init__(self):
		self.__name = ''
		self.__id = ''
		self.__desc = ''
		self.__checks = {} 

	def set_name(self, name):
		self.__name = name

	def get_name(self):
		return self.__name

	def set_id(self, id):
		self.__id = id

	def get_id(self):
		return self.__id

	def set_desc(self, desc):
		self.__desc = desc

	def get_desc(self):
		return self.__desc

	def add_check(self, key, list_values):
		self.__checks[key] = list_values

	def get_check(self):
		return self.__checks

	def reset(self):
		self.__name = ''
		self.__desc = ''
		self.__checks.clear() 
