import bs4

exampleFile = open("example.html")

exampleSoup = bs4.BeautifulSoup(exampleFile.read(),"html.parser")

elems = exampleSoup.select('#author')

type(elems)

len(elems)

str(elems[0])

elems[0].getText()

elems[0].attrs

#elems[0].get('atribute name')