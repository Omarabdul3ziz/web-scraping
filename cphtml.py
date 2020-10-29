# copy the html code for any webpage and place it in folder

import requests, sys

fi = sys.argv[1]
ad = sys.argv[2]

page = requests.get(ad)

f = open(fi, 'w')
f.write(page.text)
f.close
