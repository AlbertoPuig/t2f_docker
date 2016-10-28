from ConfigParser import SafeConfigParser


parser = SafeConfigParser()
parser.read('conf.ini')

print parser.get('trello_conf', 'url')
print parser.get('trello_conf', 'username')
print parser.get('trello_conf', 'key')
print parser.get('trello_conf', 'token')