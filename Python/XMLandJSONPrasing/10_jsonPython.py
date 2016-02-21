import json
import urllib

serviceurl = 'http://python-data.dr-chuck.net/comments_207543.json'
while True:
    url = serviceurl
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()

    info = json.loads(data)
    print 'Retrieved',len(data),'characters'
    countSum=0;
    countObj=0;
    for item in info["comments"]:
	countObj=countObj+1;
	countSum=countSum+item['count'];    	
    print "Count:",countObj
    print "Sum:",countSum
    exit()	




