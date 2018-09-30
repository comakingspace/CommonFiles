import argparse
import mwapi
import json
import requests
import re
import argparse
from bs4 import BeautifulSoup
session = mwapi.Session(host='https://wiki.comakingspace.de', api_path='/api.php')
<<<<<<< HEAD
parser = argparse.ArgumentParser(description='Wikicrawler in order to generate tool printouts')
parser.add_argument('--MachineBox', dest='MachineBox', action='store_const',
                    const=True, default=False,
                    help='Backcrawl the Machine Info Boxes')
parser.add_argument('--MaterialBox', dest='MaterialBox', action='store_const',
                    const=True, default=False,
                    help='Backcrawl the Material Info Boxes')
parser.add_argument('--ProjectBox', dest='ProjectBox', action='store_const',
                    const=True, default=False,
                    help='Backcrawl the Project Info Boxes')
parser.add_argument('--ToolBox', dest='ToolBox', action='store_const',
                    const=True, default=False,
                    help='Backcrawl the Tool Info Boxes')
=======

parser = argparse.ArgumentParser(description='Generate Tool printouts from the CoMakingSpace Wiki (https://wiki.comakingspace.de)')
categoryGroup = parser.add_mutually_exclusive_group()
categoryGroup.add_argument('--Machine', dest='MachineBox', action='store_true', 
                    help='Crawl for Machine Info Boxes')
categoryGroup.add_argument('--Tool', dest='ToolBox', action='store_true',
                    help='Crawl for Tool Info Boxes')
categoryGroup.add_argument('--Material', dest='MaterialBox', action='store_true',
                    help='Crawl for Machine Info Boxes')
categoryGroup.add_argument('--Project', dest='ProjectBox', action='store_true',
                    help='Crawl for Project Info Boxes')
categoryGroup.add_argument('--All', dest='All', action='store_true',
                    help='Crawl for All Info Boxes')
parser.add_argument('--Page', dest='Page', default='', help='Parse a specific page (use only with --InfoBoxName) example: \'python .\\wikicrawler.py --Page \"Chop Saw\" --InfoBoxName \"ToolInfoBox\"\'')
parser.add_argument('--InfoBoxName', dest='InfoBoxName', default='', help='Indicate the InfoBoxName when parsing a specific page (use only with --Page)')
>>>>>>> b8b6cb0f2690bd0fb9d26f20afac900d7f0db6c2
args = parser.parse_args()

def crawlCategory(categoryname, infoboxname):
    global session
    print("-----------------------------------------------------")
    print("Crawling Category " + categoryname)    
    query_result = session.get(action='query', list='categorymembers', cmtitle='Category:' + categoryname)
    machine_pages = query_result['query']['categorymembers']
    for page in machine_pages:
        # get the content of the page
        crawlpage(page['title'], infoboxname, categoryname)
def crawlBacklinks(backlinkpage, infoboxname):
    global session
    print("-----------------------------------------------------")
    print("Crawling Backlinks to: %s" % backlinkpage)
    query_result = session.get(action='query', list='backlinks', bltitle=backlinkpage, bllimit='max')
    machine_pages = query_result['query']['backlinks']
<<<<<<< HEAD
    machine_pages = sorted(machine_pages,key= lambda page: page['title'],reverse=False)
    total_pages = len(machine_pages)
    count = 0
    print('%i pages in total' % len(machine_pages))
=======
    machine_pages = sorted(machine_pages, key=lambda page: page['title'], reverse=False)
>>>>>>> b8b6cb0f2690bd0fb9d26f20afac900d7f0db6c2
    for page in machine_pages:
        count += 1
        print ('Page %i of %i' % (count, total_pages))
        # get the content of the page
        crawlpage(page['title'], infoboxname, infoboxname)
def crawlpage(title, infoboxname, categoryname=''):
    print(title)
    rawurl = "https://wiki.comakingspace.de/index.php?title=" + title + '&action=raw'
    responseraw = requests.get(rawurl)
    infoboxes = extractinfoboxes(responseraw.text, infoboxname)
    number = 1
    for infobox in infoboxes:
        html = parseToolbox(infobox, title)
        basefilename = title.strip().replace(' ', '_')
        basefilename = re.sub(r'(?u)[^-\w.]', '', basefilename)
        with open('%s_%s_%i.html' % (categoryname, basefilename, number), 'w', encoding='utf8') as f:
            #prettify messes up the formatted html in chrome, so we just output the plain html string.
            #f.write(html.prettify())
            f.write(str(html))
            number += 1
def parseToolbox(infoboxtext, title):
    #Getting the parsed html of the infobox
    global session
    url = "https://wiki.comakingspace.de/" + title
    url = url.replace(' ', '_')
    parsingresponse = session.get(action='parse', text=infoboxtext, contentmodel='wikitext', disablelimitreport=1)
    parsedwikitext = parsingresponse['parse']['text']['*']
    parsedwikitext = ('<html><body>' + parsedwikitext + '</body></html>')

<<<<<<< HEAD
    html = BeautifulSoup(parsedwikitext,'html.parser')
    table_tag = html.find('table')
    table_tag['style'] = table_tag['style'] + "; max-width:200px"
    image_link = html.find('a','image')
=======
    #Generating a BeatifulSoup object, which allows us to modify the DOM
    html = BeautifulSoup(parsedwikitext, 'html.parser')

    #Adding the mediawiki CSS file into the head
    head = html.new_tag('head')
    style = html.new_tag('link')
    style['href'] = 'https://wiki.comakingspace.de/load.php?debug=false&lang=en&modules=ext.slideshow.css%7Cmediawiki.legacy.commonPrint%2Cshared%7Cmediawiki.sectionAnchor%7Cmediawiki.skinning.interface%7Cskins.vector.styles&only=styles&skin=vector'
    style['rel'] = 'stylesheet'
    head.append(style)
    html.html.body.insert_before(head)
    
    try:
        Tutor = html.find('a',text='(?)', title='Tutors')
        Tutor.decompose()
    except:
        pass
    #Tutor.string = 'Tutor'
    #Modifying the Image:
    #finfind the image tag
    image_link = html.find('a', 'image')
>>>>>>> b8b6cb0f2690bd0fb9d26f20afac900d7f0db6c2
    image_tag = image_link.find('img')
    #replacing the imagetag with a figure tag - so that we can add a caption
    new_figure = html.new_tag('figure')
    Image_tag_copy = image_tag.replaceWith(new_figure)
    new_figure.append(Image_tag_copy)
    figurecaption = html.new_tag('figcaption')
<<<<<<< HEAD
    figurecaptionsmall = html.new_tag('small')
    figurecaptionsmall.string = 'For further information please scan the QR-Code or check our'
    figurecaptionsmall.append(html.new_tag('br'))
    figurecaption.append(figurecaptionsmall)
=======
    figuredescription = html.new_tag('small')
    figuredescription.string = "For further information please scan the QR-Code or check our"
    figurecaption.append(figuredescription)
    figurecaption.append(html.new_tag('br'))
>>>>>>> b8b6cb0f2690bd0fb9d26f20afac900d7f0db6c2
    figurecaption.append('Wiki: %s' % title)
    new_figure.append(figurecaption)
    # Replacing the image with the QR-code
    image_tag['src'] = 'http://chart.apis.google.com/chart?chs=200x200&cht=qr&chl=' + url
    del image_tag['srcset']
    image_tag['height'] = 200
    image_tag['width'] = 200
    table = html.find('table')
    table['style'] = table['style'].replace('float:right;', '')

    #Replacing all link tags with their respective content
    for a in html.findAll('a'):
        a.replaceWithChildren()
    return html
def extractinfoboxes(wikitext, infoboxname):
    infoboxes = []
    infoboxstart = wikitext.find("{{" + infoboxname)
    infoboxtext = None
    while infoboxstart != -1:
        infoboxend = wikitext.find("}}", infoboxstart)
        infoboxtext = wikitext[infoboxstart:infoboxend+2]
        while infoboxtext.count("{{") != infoboxtext.count('}}'):
            infoboxend = wikitext.find("}}", infoboxend+2)
            infoboxtext = wikitext[infoboxstart:infoboxend+2]
        if infoboxtext is not None:
            infoboxes.append(infoboxtext)
        infoboxstart = wikitext.find("{{" + infoboxname, infoboxend)
    return infoboxes

if __name__ == "__main__":
<<<<<<< HEAD
    if args.ToolBox:
        crawlBacklinks('Template:ToolInfoBox','ToolInfoBox')
    if args.MachineBox:
        crawlBacklinks('Template:MachineInfoBox','MachineInfoBox')
    if args.MaterialBox:
        crawlBacklinks('Template:MaterialInfoBox','MaterialInfoBox')
    if args.ProjectBox:
        crawlBacklinks('Template:ProjectInfoBox','ProjectInfoBox')
    #crawlpage('Eccentric_Sanders','ToolInfoBox','Test')
    #crawlCategory("Audio", "ProjectInfoBox")
    #crawlCategory("Hardware", "ToolInfoBox")
    #crawlCategory("Power Tools", "ToolInfoBox")
    #crawlCategory("Machines", "MachineInfoBox")
=======
    if (args.MachineBox or args.All):
        crawlBacklinks('Template:MachineInfoBox', 'MachineInfoBox')
    if (args.MaterialBox or args.All):
        crawlBacklinks('Template:MaterialInfoBox', 'MaterialInfoBox')
    if (args.ProjectBox or args.All):
        crawlBacklinks('Template:ProjectInfoBox', 'ProjectInfoBox')
    if (args.ToolBox or args.All):
        crawlBacklinks('Template:ToolInfoBox', 'ToolInfoBox')
    if (args.Page!= ''):
        if (args.InfoBoxName!=''):
            crawlpage(args.Page, args.InfoBoxName)
        else:
            print('Please indicate the Info Box Name when crawling a specific page.')
    # crawlpage('Eccentric_Sanders','ToolInfoBox','Test')
    # crawlCategory("Audio", "ProjectInfoBox")
    # crawlCategory("Hardware", "ToolInfoBox")
    # crawlCategory("Power Tools", "ToolInfoBox")
    # crawlCategory("Machines", "MachineInfoBox")
>>>>>>> b8b6cb0f2690bd0fb9d26f20afac900d7f0db6c2
