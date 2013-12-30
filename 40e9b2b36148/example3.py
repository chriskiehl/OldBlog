import urllib2

urls = ['http://www.yahoo.com', 'http://www.reddit.com']
results = map(urllib2.urlopen, urls)

results = []
for url in urls: 
	results.append(urllib2.urlopen(url))

from multiprocessing import Pool
from multiprocessing.dummy import Pool as tPool 

