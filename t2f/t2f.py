import os, sys 
from trello_conn import TrelloConn
from logger import  Logger

def prepare(boardname, verbose):
	log = Logger()
	if verbose == 'y':
		log.set_debuglevel()
	else:
		log.set_infolevel()
	
	log.info_msg("RUNNING PROCESS")
	log.debug_msg("DEBUG_INFO")
	trello = TrelloConn(log)
	log.debug_msg("Connecting to Trello")
	trello.set_board(boardname)
	id_board = trello.get_trello_board()
	log.debug_msg("Getting board data")
	trello.set_board_id(id_board)
	log.debug_msg("Creating feature files")
	trello.create_features()
	log.debug_msg("_______________________________")	
	log.debug_msg("Process completed successfully")	
	log.info_msg("Process completed successfully")	
	log.debug_msg("_______________________________")

def usage():
	print"====================================================================="
	print "Make features files (BDD - Gherkin) from Trello User_Stories\n"
	print "SYNOPSIS"
	print "t2f board_name [-v]"
	print "t2f -h\n"
	print "DESCRIPTION"
	print "board_name Set the name of board in Trello"
	print "-ve Set Verbose mode"
	print "-h Show program help\n"
	print"====================================================================="

if __name__ == '__main__': 
	if len(sys.argv) > 3 or len(sys.argv) < 2: 
		usage()
	if len(sys.argv) == 2:
		if sys.argv[1] == '-h':
			usage()
		else:
			verbose = 'n'
			prepare(sys.argv[1],verbose)

	if len(sys.argv) == 3:
		if sys.argv[2] == '-ve':
			verbose = 'y'
			prepare(sys.argv[1],verbose)
		else:
			usage()
