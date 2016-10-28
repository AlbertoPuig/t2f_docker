import httplib2 as http
#import httplib as http
import json
import feature_maker
from ConfigParser import SafeConfigParser
#from user_story import user_story
from user_story import UserStory


try:
    from urlparse import urlparse
except ImportError:																																																																																																																																																																																																																																																																																																																																																																																																																																																		

    from urllib.parse import urlparse
from ConfigParser import SafeConfigParser

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json; charset=UTF-8'
}

class TrelloConn(object):

	def __init__(self, log):
		parser = SafeConfigParser()
		parser.read('/usr/shared/conf.ini')
		self.__base_url = parser.get('trello_conf', 'url')
		self.__params_url = '?fields=username,fullName,url&boards=all&board_fields=name&organizations=all&organization_fields=displayName&key='
		self.__token_param = '&token='
		self.__key = parser.get('trello_conf', 'key')
		self.__user = parser.get('trello_conf', 'username')
		self.__token = parser.get('trello_conf', 'token')
		self.__board = ''
		self.__board_id = ''
		self.__board_id_list = []
		self.__card_id = ''
		self.__checklist_id = ''
		self.__checklistdetails = ''
		log.debug_msg("Connected Trello API")

	def set_user(self, user):
		self.__user = user
	def get_user(self):
		return self.__user

	def set_key(self,key):
		self.__key = key

	def get_key(self):
		return self.__key

	def set_token(self, token):
		self.__token = token

	def get_token(self):
		return self.__token

	def get_base_url(self):
		return self.__base_url

	def set_board(self, board):
		self.__board = board

	def get_board(self):
		return self.__board

	def set_board_id(self, board_id):
		self.__board_id = board_id

	def get_board_id(self):
		return self.__board_id

	def set_card_id(self, card_id):
		self.__card_id = card_id

	def get_card_id(self):
		return self.__card_id

	def set_checklist_id(self, checklist_id):
		self.__checklist_id = checklist_id

	def get_checklist_id(self):
		return self.__checklist_id

	def set_checklistdetails(self, checklistdetails):
		self.__checklistdetails = checklistdetails

	def get_checklistdetails(self):
		return self.__checklistdetails

	def connector(self, uri):
		if uri == "boards":
			uri = self.__base_url + self.__user + '?fields=username,fullName,url&boards=all&board_fields=name&organizations=all&organization_fields=displayName&key=' + self.__key + '&token=' + self.__token

		if uri == "cards":
			uri = "https://api.trello.com/1/boards/" + self.get_board_id() + "/cards?fields=field,name,idList,url&key=" + self.__key + "&token=" + self.__token

		if uri == "infocards":
			uri = "https://api.trello.com/1/cards/" + self.get_card_id() + "/?key=" + self.__key + "&token=" + self.__token
		
		if uri == "infochecklists":
			uri = "https://api.trello.com/1/cards/" + self.get_checklist_id() + "/checklists?fields=name,idList&member_fields=fullName&key=" + self.__key + "&token=" + self.__token

		if uri == "checklistsdetails":
			uri = "https://api.trello.com/1/checklists/" + self.get_checklistdetails() + "?fields=name&cards=all&card_fields=name&key=" + self.__key + "&token=" + self.__token


		path = ''
		target = urlparse(uri+path)
		method = 'GET'
		body = ''
		h = http.Http()

		response, content = h.request(
				target.geturl(),
				method,
				body,
				headers)
		data = json.loads(content)

		return data


	def get_trello_board(self):
		#print "1. All Boards"
		data = self.connector("boards")
		#get board_id of board_name pass by param
		for item in data['boards']:
			name = item.get("name")
			if self.__board == name:
				board_id = item.get("id")
				#print board_id
			#print name
		return board_id

	def create_features(self):
		cards = self.trello_cards()
		for item in cards:
			#print item.get("id")
			self.trello_desc_card(item.get("id"))

	def trello_cards(self):
		#get all cards of board
		data = self.connector("cards")
		return data


	def trello_desc_card(self, card_id):
		#get info of cards IN THIS TIME ONLY ONE WITH HARD SET ID
		#print "3. Info of Cards"
		self.set_card_id(card_id)
		data2 = self.connector("infocards")
		userstory = UserStory()
		#get checklist of card
		
		self.set_checklist_id(data2["id"])
		
		data3 = self.connector("infochecklists")

		for item in data3:
			#print item.get("name")
			dic_key = item.get("name")
			self.trello_get_checklist_details(item.get("id"),dic_key,userstory)

		userstory.set_name(data2["name"])
		userstory.set_desc(data2["desc"])
		
		feature_maker.prepare(userstory)

		#get checklist details
	def trello_get_checklist_details(self,checklistid, dic_key, userstory):

		self.set_checklistdetails(checklistid)
		data4 = self.connector("checklistsdetails")
		list_checkitems = []
		for item in data4["checkItems"]:
			list_checkitems.append(item.get("name"))
		userstory.add_check(dic_key, list_checkitems)