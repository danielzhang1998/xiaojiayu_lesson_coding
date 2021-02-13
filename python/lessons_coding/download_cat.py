import urllib.request as uuu

response = uuu.urlopen('http://placekitten.com/600/800')
cat_image = response.read()

with open('cat_600_800.jpg','wb') as f:
    f.write(cat_image)