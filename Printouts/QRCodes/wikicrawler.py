import mwapi
import json
import requests
import re
from bs4 import BeautifulSoup

def crawlCategory(categoryname, infoboxname):
    print("-----------------------------------------------------")
    print("Crawling Category " + categoryname)
    session = mwapi.Session(host='https://wiki.comakingspace.de', api_path='/api.php')
    query_result = session.get(action='query', list='categorymembers',cmtitle='Category:' + categoryname)
    machine_pages = query_result['query']['categorymembers']
    for page in machine_pages:
        print(page['title'])
        url= "https://wiki.comakingspace.de/" + page['title']
        rawurl = "https://wiki.comakingspace.de/index.php?title=" + page['title'] + '&action=raw'
        responsehtml = requests.get(url)
        responseraw = requests.get(rawurl)
        infoboxstart = responseraw.text.find("{{" + infoboxname)
        infoboxtext = ""
        if infoboxstart != -1:
            #This gets the wikicode of the infobox.
            #Missing logic: If another template was used in between, this will not work. 
            infoboxend = responseraw.text.find("}}",infoboxstart)
            checkstart = infoboxstart
            infoboxtext = responseraw.text[infoboxstart:infoboxend+2]
            while infoboxtext.count("{{") != infoboxtext.count('}}'):
                infoboxend = responseraw.text.find("}}",infoboxend+2)
                infoboxtext = responseraw.text[infoboxstart:infoboxend+2]
            parsingresponse = session.get(action='parse', text = infoboxtext, contentmodel = 'wikitext')
            parsedwikitext = parsingresponse['parse']['text']['*']
            parsedwikitext = ('<html><body>' + parsedwikitext + '</body></html>')
            basefilename = page['title'].strip().replace(' ', '_')
            basefilename = re.sub(r'(?u)[^-\w.]', '', basefilename)
            html = BeautifulSoup(parsedwikitext,'html.parser')
            image_link = html.find('a','image')
            image_tag = image_link.find('img')
            image_tag['src'] = 'http://chart.apis.google.com/chart?chs=200x200&cht=qr&chl=' + url
            del image_tag['srcset']
            image_tag['height'] = 200
            image_tag['width'] = 200
            for a in html.findAll('a'):
                a.replaceWithChildren()
            #print(basefilename)
            with open(categoryname + '_' + basefilename + '.html','w',encoding='utf8') as f:
                f.write(html.prettify())
            #with open(categoryname + '_' + basefilename + '_wikitext.txt','w',encoding='utf8') as f:
            #    f.write(infoboxtext)
        print(url)
        #print(rawurl)
        #print(parsedwikitext)
        #print(infoboxtext)

if __name__ == "__main__":
    crawlCategory("Hardware", "ToolInfoBox")
    crawlCategory("Machines", "MachineInfoBox")
