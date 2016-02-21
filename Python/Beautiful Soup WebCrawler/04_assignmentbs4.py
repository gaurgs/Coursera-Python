import urllib
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/comments_207542.html'
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
print html
sum=0

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
	 sum=sum+int(tag.contents[0])

print sum		




# tags = soup('a')
# for tag in tags:
   # Look at the parts of a tag
#   print 'TAG:',tag
 #  print 'URL:',tag.get('href', None)
 #  print 'Contents:',tag.contents[0]
 #  print 'Attrs:',tag.attrs  
