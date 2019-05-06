import scrapy
import json
# Set these two variables as the (inclusive, inclusive) number of pages to crawl.
# By default, this spider will only crawl the first page.
start_page = 1
end_page = 1
# Initial url to crawl. CRUCIALLY, DOES NOT CONTAIN THE PAGE NUMBER.
init_url = 'https://www.goodreads.com/author/quotes/656983.J_R_R_Tolkien?page=%s'
author_name = 'Tolkien'
special_case = '  ―\n  '  # This sequence *appears* to IMMEDIATELY follow every quote on GoodReads


class QuotesSpider(scrapy.Spider):
    name = "GoodReadsSpider"

    def start_requests(self):

        for i in range(start_page, (end_page + 1)):
            url = init_url % i
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        quotes = response.css('div[class=quoteText]::text').getall()
        constructed_quotes = []
        QuotesSpider.extract_quote(loaded_quotes=quotes, constructed_quotes=constructed_quotes, curr_string="", index=0)

        page_num = response.url.split("=")[1]
        filename = author_name + 'Quotes-%s.json' % page_num

        with open(filename, 'w') as outfile:
            json.dump(constructed_quotes, outfile)

        self.log('Saved file %s' % filename)

    # Turns the gobble-de-gook text extracted from the GoodReads site into a coherent array
    # where each element (should) be one of the discrete quotes listed on the web page.
    @staticmethod
    def extract_quote(loaded_quotes, constructed_quotes, curr_string, index):
        if index < len(loaded_quotes):
            # The pattern always immediately follows a quote, and we don't want to include any newline chars
            if loaded_quotes[index] == special_case:
                constructed_quotes.append(curr_string)
                QuotesSpider.extract_quote(loaded_quotes=loaded_quotes,
                                           constructed_quotes=constructed_quotes,
                                           curr_string="",
                                           index=(index + 1))
            # The newline only case
            elif QuotesSpider.only_newlines(string=loaded_quotes[index]):
                QuotesSpider.extract_quote(loaded_quotes=loaded_quotes,
                                           constructed_quotes=constructed_quotes,
                                           curr_string=curr_string,
                                           index=(index + 1))
            # If we aren't at the end of the quote, keep appending the string
            else:
                QuotesSpider.extract_quote(loaded_quotes=loaded_quotes,
                                           constructed_quotes=constructed_quotes,
                                           curr_string=(curr_string + ' ' + QuotesSpider.treat_string(loaded_quotes[index]) + "\n"),
                                           index=(index+1))

    # GoodReads consistently adds a bunch of noise to the text which we do not want.
    # The following was an appropriate fix for me, but feel free to change it if
    # there is additional nonsense appearing in your Strings.
    @staticmethod
    def treat_string(string):
        return string.strip()

    # Returns true if the passed string is only made of newline chars or spaces.
    @staticmethod
    def only_newlines(string):
        for i in range(0, len(string)):
            if string[i] != '\n' and string[i] != ' ':
                return False

        return True
