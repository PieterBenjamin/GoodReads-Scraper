# GoodReads Scraper
The goal of this was project was simple: create a single python script which will scrape quotes from [goodreads.com](https://www.goodreads.com/).  

Python was chosen simply due to the availability of libraries. Initially, I tried using the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) libary,   
but found it too inflexible.  

Instead, upon the recommendation of a friend I used [Scrapy](https://scrapy.org/) and found it significantly faster and easier to use.  

Python 3.0, and Scrapy are the only necessary installations for this project to work. There are only 4 things you need to edit  
for a succesful scrape with a different author. 
1. Change the link from the [Tolkien one](https://github.com/PieterBenjamin/GoodReads-Scraper/blob/master/GoodReads_Scraper/spiders/GoodReads_Spider.py#L5) to whichever authors quotes you desire. 
2. Set the page to [start at](https://github.com/PieterBenjamin/GoodReads-Scraper/blob/master/GoodReads_Scraper/spiders/GoodReads_Spider.py#L8) (leave as 1 if desired)
3. Set the page to [end at](https://github.com/PieterBenjamin/GoodReads-Scraper/blob/master/GoodReads_Scraper/spiders/GoodReads_Spider.py#L9) (inclusive, make sure you do not ask for more pages than exist!)
4. Change the [authors name](https://github.com/PieterBenjamin/GoodReads-Scraper/blob/master/GoodReads_Scraper/spiders/GoodReads_Spider.py#L10) (used in output format)  

From here, `cd` into your directory and enter the command: `scrapy crawl GoodReadsSpider`  
After that, Scrapy will take care of the rest and you should have a diretory full of json files! The only element in these files  
is an array with all of the scraped quotes from the respective page numbers (which will be included in the file names).   

You are free, of course, to use the quotes however you like, but I might personally recommend the partner project to this, my [QuoteGenerator](https://github.com/PieterBenjamin/QuoteGenerator)
