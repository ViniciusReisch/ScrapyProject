import scrapy

class BuscapeSpider(scrapy.Spider):
    name = 'buscape'
    start_urls = ["https://www.buscape.com.br/console-de-video-game/console-playstation-5-edicao-digital-sony-4k?_lc=88&searchterm=ps"]

    def parse(self, response):
        for produtos in response.css(".OfferCard_OfferCardWrapper__3SbhD"):
            yield{
                'Loja': produtos.css('.OfferMerchant_Name__f_ADg::text').get(),
                'Preco': produtos.css('.Text_MobileHeadingM__FRgbv::text').get(),
                'Prestacao': produtos.css('.OfferPrice_Installments__006GM::text').get()
            }