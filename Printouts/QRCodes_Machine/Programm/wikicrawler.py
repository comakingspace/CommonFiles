import argparse
import mwapi
import json
import requests
import re
import argparse
import io
import qrcode
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont

session = mwapi.Session(host='https://wiki.comakingspace.de', api_path='/api.php')

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
parser.add_argument('--Projects', dest='Projects', action='store_true', help='crawl the project pages')
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
    machine_pages = sorted(machine_pages,key= lambda page: page['title'],reverse=False)
    total_pages = len(machine_pages)
    count = 0
    print('%i pages in total' % len(machine_pages))
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

    #Generating a BeatifulSoup object, which allows us to modify the DOM
    html = BeautifulSoup(parsedwikitext, 'html.parser')

    #Adding the mediawiki CSS file into the head
    head = html.new_tag('head')
    meta = html.new_tag('meta')
    meta['charset'] = 'utf-8'
    head.append(meta)
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
    image_tag = image_link.find('img')
    #replacing the imagetag with a figure tag - so that we can add a caption
    new_figure = html.new_tag('figure')
    Image_tag_copy = image_tag.replaceWith(new_figure)
    new_figure.append(Image_tag_copy)
    figurecaption = html.new_tag('figcaption')
    figuredescription = html.new_tag('small')
    figuredescription.string = "For further information please scan the QR-Code or check our"
    figurecaption.append(figuredescription)
    figurecaption.append(html.new_tag('br'))
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
def crawlProjectNameSpace():
    global session
    print("-----------------------------------------------------")
    print("Crawling Project Namespace")    
    query_result = session.get(action='query', list='allpages', apnamespace='4', aplimit='500')
    project_pages = query_result['query']['allpages']
    for page in project_pages:
        # get the content of the page
        crawlPageForPic(page['title'])
def crawlPageForPic(title, infoboxname='ProjectInfoBox'):
    global session
    rawurl = "https://wiki.comakingspace.de/index.php?title=" + title + '&action=raw'
    responseraw = requests.get(rawurl)
    infoboxes = extractinfoboxes(responseraw.text, infoboxname)
    for infobox in infoboxes:
        #get the image and the corresponding link
        file_start = infobox.find("image=")+6
        file_end = infobox.find("\n", file_start)
        file_name = "File:" + infobox[file_start:file_end]
        if infobox[file_start:file_end].find('.') == -1:
            break
        #get url
        query_result = session.get(action='query', prop='imageinfo', iiprop='url', titles=file_name)
        image_specifics = query_result['query']['pages'][list(query_result['query']['pages'])[0]]
        if 'missing' in image_specifics:
            break
        image_link = image_specifics['imageinfo'][0]['url']
        project_title = title[title.find(':')+1:]
        url = "https://wiki.comakingspace.de/" + title.replace(" ","_")
        buildPrintout (url, project_title, image_link)

def getProjectsWithPictures ():
    global session
    print("-----------------------------------------------------")
    print("Downloading Project Information")    
    
    query_result = session.get(action='ask', query='[[Project:+]]|[[Has image::!File:Project-default.png]]|?has caption|?has image|limit=500')
    project_pages = query_result['query']['results']
    for page in project_pages:
        project_title = page.replace('Project:','')
        image_link = project_pages[page]['printouts']['Has image'][0]['fullurl'].replace('File:', 'Special:Redirect/file/')
        url = project_pages[page]['fullurl']
        buildPrintout(url, project_title, image_link)

def buildPrintout(url, project_title, image_link):
    #some general parameters
    border_percent = 4
    
    print(f'Building the Image for {project_title}')

    #Download the Image 
    headers = {"User-Agent": "CoMakingSpace Wikicrawler (https://www.comakingspace.org; info@comaking.space)"}
    file = requests.get(image_link, headers = headers).content

    image = Image.open(io.BytesIO(file))
    size = image.size[1]//10
    text_font = ImageFont.truetype('Roboto-Regular.ttf', size=size)

    # create the QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="white", back_color="#383e42")
    qr_image = qr_image.get_image()
    qr_image = qr_image.resize((size*2,size*2))
 
    #Add the Project Name to the image
    text_image = Image.new('RGB', text_font.getsize(project_title) , '#383e42')
    draw = ImageDraw.Draw(text_image)
    draw.text((0,0),project_title, fill='white', font=text_font)
    if text_image.size[0] > image.size[0]:
        target_size_x = image.size[0]-qr_image.size[0]
        factor = target_size_x / text_image.size[0]
        text_image = text_image.resize( (int(text_image.size[0]*factor), int (text_image.size[1]*factor) ) )
    
    #Join the downloaded image, the text and the QR Code
    image_total = Image.new('RGB', (max(image.size[0],text_image.size[0]+qr_image.size[0]), image.size[1]+text_image.size[1]), (56,62,66) )
    image_total.paste(image, (int(image_total.size[0] /2 - image.size[0]/2) ,0))
    image_total.paste(text_image, (int(text_image.size[0] /2 - text_image.size[0]/2) ,image.size[1]))
    image_total.paste(qr_image, (image_total.size[0] - qr_image.size[0] ,image_total.size[1] - qr_image.size[1]))

    # Add some border
    image_total_2 = Image.new('RGB', ( int(image_total.size[0] * (border_percent/100+1)), int(image_total.size[1] * (border_percent/100+1) )), (56,62,66) )
    image_total_2.paste(image_total, ( int((border_percent/100)*image_total.size[0]/2) ,int((border_percent/100)*image_total.size[1]/2)))
    
    #save the whole thing
    image_total_2.save(project_title + "_total.jpg")
    print(f'Image for {project_title} saved')

if __name__ == "__main__":
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
    if (args.Projects):
        #crawlProjectNameSpace()
        getProjectsWithPictures()
    # crawlpage('Eccentric_Sanders','ToolInfoBox','Test')
    # crawlCategory("Audio", "ProjectInfoBox")
    # crawlCategory("Hardware", "ToolInfoBox")
    # crawlCategory("Power Tools", "ToolInfoBox")
    # crawlCategory("Machines", "MachineInfoBox")
