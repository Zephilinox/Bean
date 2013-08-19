from module_info import *

#! Based on: http://stackoverflow.com/a/5878324
#if swysdk['enable_caching']:
#    import pickle
#    import os
#    try:
#        l = pickle.load(open("Header/_swysdk.buildcache"))
#    except IOError:
#        l = []
#    db = dict(l)
#    path = __name__
#    checksum = os.path.getmtime(path)
#    if (db.get(path, None) != checksum):
#        print ("file changed: "+str(__name__))
#        db[path] = checksum
#    else:
#        You don't need to be recompiled
#        os.exit()
#    pickle.dump(db.items(), open("Header/_swysdk.buildcache", "w"))

#! Based on: http://stackoverflow.com/a/2440786
def swytrailzro(num):
	import decimal
	
	if swysdk['enable_optimizations']:
		return ('%f' % num).rstrip('0').rstrip('.')
	else:
		return ('%f' % num)