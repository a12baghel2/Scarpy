import scrapy

class bookSpider(scrapy.Spider):
    name = "book_crawl"
    def start_requests(self):

        urls = ['http://books.toscrape.com/catalogue/page-1.html']

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        
        for r in response.css("article.product_pod"):
            img = r.css('div.image_container a img::attr(src)').get()
            title = r.css('h3 a::attr(title)').get()
            price = r.css('div.product_price p.price_color::text').get()
            
            #title = title.replace(',','')               

            yield {
                'image_url':img,
                'book_title': title,
                'product_price': price
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse)
    
