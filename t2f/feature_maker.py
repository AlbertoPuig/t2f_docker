#feature maker
import os, sys
import errno
from ConfigParser import SafeConfigParser
#from os.path import expanduser
from user_story import UserStory
from logger import  Logger

#class FeatureMaker(object):


def prepare(userstory):
	parser = SafeConfigParser()
	parser.read('/usr/shared/conf.ini')
	feature = parser.get('gherkin_conf', 'feature')
	scenario = parser.get('gherkin_conf','scenario')
	language = parser.get('gherkin_conf','language')
	size = parser.get('gherkin_conf','size')

	freq = parser.get('gherkin_conf','freq')
	scale = parser.get('gherkin_conf','scale')
	ambit = parser.get('gherkin_conf','ambit')



	given = parser.get('gherkin_conf', 'given')
	other = parser.get('gherkin_conf', 'other')
	path = parser.get('gherkin_conf', 'path')
	when = parser.get('gherkin_conf', 'when')
	then = parser.get('gherkin_conf', 'then')

	log = Logger()
	log.debug_msg("Getting config")

	if len(userstory.get_name()) > 25:
		filename = userstory.get_name()[:25]
	else:
		filename = userstory.get_name()
	log.debug_msg("Writing file: " + filename)	
	filename = filename.replace(" " ,"_")
	dicc = userstory.get_check()
	#list_items = list(userstory.get_check().keys())
	list_items = list(dicc.keys())
	#k = list(b.keys())
	check_values = userstory.get_check()
	file = open(path + filename + '.feature', "w")

	file.write(language + "\n")
	file.write(size + "\n")
	file.write(freq + "\n")
	file.write(scale + "\n")
	file.write(ambit + "\n \n")

	file.write(feature + ' ' + userstory.get_desc().replace('\n'," ") + " \n");
	file.write(scenario + ' ' + userstory.get_name() + " \n")
	
	for key in list_items:
   		file.write(given + ' ' + key + " \n")
   		list_checks = get_checks_detail(dicc,key)
   		for check in list_checks:
   			file.write(when + ' ' + check + " \n")
			file.write(then +  ' ' + " \n")

	file.close()
	log.debug_msg("File created successfully")

	'''print".................................................."
	print userstory.get_name()
	print userstory.get_desc()
	print userstory.get_check()
	print "Filename: " + filename
	print".................................................."'''


if __name__ == '__main__':
	prepare(sys.argv[1])


def get_checks_detail(dicc, key):
	return dicc.get(key)