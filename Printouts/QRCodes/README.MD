Installation: 
```shell
pip install -r requirements.txt
```
Usage: 
```shell
wikicrawler.py [-h]
                      [--Machine | --Tool | --Material | --Project | --All]
                      [--Page PAGE] [--InfoBoxName INFOBOXNAME]

Generate Tool printouts from the CoMakingSpace Wiki
(https://wiki.comakingspace.de)

optional arguments:
  -h, --help            show this help message and exit
  --Machine             Crawl for Machine Info Boxes
  --Tool                Crawl for Tool Info Boxes
  --Material            Crawl for Machine Info Boxes
  --Project             Crawl for Project Info Boxes
  --All                 Crawl for All Info Boxes
  --Page PAGE           Parse a specific page (use only with --InfoBoxName)
                        example: 'python .\wikicrawler.py --Page "Chop Saw"
                        --InfoBoxName "ToolInfoBox"'
  --InfoBoxName INFOBOXNAME
                        Indicate the InfoBoxName when parsing a specific page
                        (use only with --Page)
```

What to print:

We have a ["MissingQR" category in the wiki](https://wiki.comakingspace.de/Category:MissingQR) that should help you see which QR codes are "flagged" for printing. Please remove the pages from this category once you print the code! 
