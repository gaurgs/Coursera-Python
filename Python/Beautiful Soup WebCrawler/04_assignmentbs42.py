import urllib
from BeautifulSoup import *

url = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Arlo.html'
position=1

# Retrieve all of the anchor tags
i=0

for i in range(0,7):
	#print i
	position=1	
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	tags = soup('a')
	for tag in tags:   
			if(position==18):
				#print tag.get('href', None),'Contents:',tag.contents[0]
				url=tag.get('href', None)
				break;
			else:
				position=position+1
	if(i==6):
		print tag.contents[0]
		break


	




