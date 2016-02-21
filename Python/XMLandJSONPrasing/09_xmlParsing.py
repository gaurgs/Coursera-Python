import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://python-data.dr-chuck.net/comments_207539.xml'

while True:
    url = serviceurl;
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'	
    commentinfo = ET.fromstring(data)

    lst = commentinfo.findall('comments/comment');

    sumCount=0
    countTag=0	 	
    for item in lst:
	  countTag=countTag+1;
	  sumCount=int(item.find('count').text)+sumCount;
    print "count:",countTag
    print "sum:",sumCount 		
    exit()		    

	 	

