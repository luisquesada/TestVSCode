#Download images from a page

import requests, os, bs4

url = "http://bustypics.com/?q=viola+bailey"

#os.makedirs("images",exist_ok=True)

#loads the page
res = requests.get(url)

try:
    res.raise_for_status()
except Exception as exc:
    print("There was a problem: {0}".format(exc))

fileSoup = bs4.BeautifulSoup(res.text,"html.parser")

#Create a list of images
elems = fileSoup.select('img')

#Checks for valid images and download them
for elem in elems:
    imgUrl = elem.get('data-src')
    if imgUrl != None:
        print('Downloading image %s...' % imgUrl)   
        res2 = requests.get(imgUrl)
        res2.raise_for_status()
        imageFile = open(os.path.join("C:\Soft", os.path.basename(imgUrl)),'wb')        
        for chunck in res2.iter_content(100000): #100000 bytes
            imageFile.write(chunck)
        imageFile.close()

print("Done!")


