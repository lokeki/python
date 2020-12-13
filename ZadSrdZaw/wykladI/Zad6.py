import urllib.request #pobieranie zawartosci ze strony
import os

pages = [

    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},

    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'},

    { 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' } ]

dirName = r'N:\temp'
for line in pages:
    try:
        path = os.path.join(dirName,line['name'] + '.html')
        urllib.request.urlretrieve(line['url'], path)
    except:
        print("Błąd")
        break
else:
    print("Bez problemow")