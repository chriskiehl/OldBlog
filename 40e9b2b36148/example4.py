
import urllib2 
from multiprocessing.dummy import Pool as ThreadPool 

urls = [
	'http://www.python.org', 
	'http://www.python.org/about/',
	'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
	'http://www.python.org/doc/',
	'http://www.python.org/download/',
	'http://www.python.org/getit/',
	'http://www.python.org/community/',
	'https://wiki.python.org/moin/',
	'http://planet.python.org/',
	'https://wiki.python.org/moin/LocalUserGroups',
	'http://www.python.org/psf/',
	'http://docs.python.org/devguide/',
	'http://www.python.org/community/awards/'
	# etc.. 
	]

# Make the Pool of workers
pool = ThreadPool(4) 
# Open the urls in their own threads
# and return the results
results = pool.map(urllib2.urlopen, urls)
#close the pool and wait for the work to finish 
pool.close() 
pool.join() 

















# results = [] 
# for url in urls:
# 	result = urllib2.urlopen(url)
# 	results.append(result)

# # ------- VERSUS ------- # 


# # ------- 4 Pool ------- # 
# pool = ThreadPool(4) 
# results = pool.map(urllib2.urlopen, urls)

# # ------- 8 Pool ------- # 

# pool = ThreadPool(8) 
# results = pool.map(urllib2.urlopen, urls)

# # ------- 13 Pool ------- # 

# pool = ThreadPool(13) 
# results = pool.map(urllib2.urlopen, urls)




# 						Single thread:  14.4 Seconds 
# 						       4 Pool:   3.1 Seconds
# 						       8 Pool:   1.4 Seconds
# 						      13 Pool:   1.3 Seconds




