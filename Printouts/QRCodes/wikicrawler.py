import mwapi
import json
import requests
import re
from bs4 import BeautifulSoup
session = mwapi.Session(host='https://wiki.comakingspace.de', api_path='/api.php')
def crawlCategory(categoryname, infoboxname):
    global session
    print("-----------------------------------------------------")
    print("Crawling Category " + categoryname)
    
    query_result = session.get(action='query', list='categorymembers',cmtitle='Category:' + categoryname)
    machine_pages = query_result['query']['categorymembers']
    for page in machine_pages:
        # get the content of the page
        crawlpage(page['title'],infoboxname,categoryname)

def crawlBacklinks(backlinkpage, infoboxname):
    global session
    print("-----------------------------------------------------")
    print("Crawling Backlinks to: %s" % backlinkpage)
    
    query_result = session.get(action='query', list='backlinks',bltitle=backlinkpage,bllimit='max')
    machine_pages = query_result['query']['backlinks']
    machine_pages = sorted(machine_pages,key= lambda page: page['title'],reverse=False)
    for page in machine_pages:
        # get the content of the page
        crawlpage(page['title'],infoboxname,infoboxname)

def crawlpage(title,infoboxname, categoryname = ''):
    print(title)
    rawurl = "https://wiki.comakingspace.de/index.php?title=" + title + '&action=raw'
    responseraw = requests.get(rawurl)
    infoboxes = extractinfoboxes(responseraw.text,infoboxname)
    number = 1
    for infobox in infoboxes:
        html = parseToolbox(infobox, title)
        basefilename = title.strip().replace(' ', '_')
        basefilename = re.sub(r'(?u)[^-\w.]', '', basefilename)
        with open('%s_%s_%i.html' % (categoryname,basefilename,number),'w',encoding='utf8') as f:
            f.write(html.prettify())
            number += 1



def parseToolbox(infoboxtext, title):
    global session
    url= "https://wiki.comakingspace.de/" + title
    parsingresponse = session.get(action='parse', text = infoboxtext, contentmodel = 'wikitext', disablelimitreport = 1)
    parsedwikitext = parsingresponse['parse']['text']['*']
    parsedwikitext = ('<html><body>' + parsedwikitext + '</body></html>')

    html = BeautifulSoup(parsedwikitext,'html.parser')
    image_link = html.find('a','image')
    image_tag = image_link.find('img')
    new_figure = html.new_tag('figure')
    Image_tag_copy = image_tag.replaceWith(new_figure)
    new_figure.append(Image_tag_copy)
    figurecaption = html.new_tag('figcaption')
    figurecaption.string = 'Wiki: %s' % title
    new_figure.append(figurecaption)
    image_tag['src'] = 'http://chart.apis.google.com/chart?chs=200x200&cht=qr&chl=' + url
    del image_tag['srcset']
    image_tag['height'] = 200
    image_tag['width'] = 200
    table = html.find('table')
    table['style'] = table['style'].replace('float:right;','')
    for a in html.findAll('a'):
        a.replaceWithChildren()
    return html

def extractinfoboxes(wikitext,infoboxname):
    infoboxes = []
    searchstart = 0
    number_of_infoboxes = wikitext.count("{{" + infoboxname)
    infoboxstart = wikitext.find("{{" + infoboxname)
    infoboxtext = None
    while infoboxstart != -1:
        infoboxend = wikitext.find("}}",infoboxstart)
        checkstart = infoboxstart
        infoboxtext = wikitext[infoboxstart:infoboxend+2]
        while infoboxtext.count("{{") != infoboxtext.count('}}'):
            infoboxend = wikitext.find("}}",infoboxend+2)
            infoboxtext = wikitext[infoboxstart:infoboxend+2]
        if infoboxtext is not None:
            infoboxes.append(infoboxtext)
        infoboxstart = wikitext.find("{{" + infoboxname,infoboxend)
    return infoboxes

if __name__ == "__main__":
    crawlBacklinks('Template:ToolInfoBox','ToolInfoBox')
    crawlBacklinks('Template:MachineInfoBox','MachineInfoBox')
    crawlBacklinks('Template:MaterialInfoBox','MaterialInfoBox')
    crawlBacklinks('Template:ProjectInfoBox','ProjectInfoBox')
    #crawlpage('Eccentric_Sanders','ToolInfoBox','Test')
    #crawlCategory("Audio", "ProjectInfoBox")
    #crawlCategory("Hardware", "ToolInfoBox")
    #crawlCategory("Power Tools", "ToolInfoBox")
    #crawlCategory("Machines", "MachineInfoBox")
