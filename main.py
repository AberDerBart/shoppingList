from shoppinglist import actions
from shoppinglist.sList import List
from shoppinglist.config import config, args

sl=List(config.get('server'),config.get('list'))

if(args.command):
	actions.actionDict[args.command](sl,args)
else:
	sl.sync()

sl.show()
