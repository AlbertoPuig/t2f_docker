#logger
import logging

class Logger(object):
	def __init__(self):
		logger = logging.getLogger(__name__)

	def set_debuglevel(self):
		logging.basicConfig(level=logging.DEBUG)

	def set_infolevel(self):
		logging.basicConfig(level=logging.INFO)

	def info_msg(self, msg):
		logging.info(msg)

	def debug_msg(self, msg):
		logging.debug(msg)