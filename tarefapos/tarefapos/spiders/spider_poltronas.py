import scrapy

class SpiderPoltronas(scrapy.Spider):
    name = 'spider_poltronas'
    
    start_urls = [f'https://www.madeiramadeira.com.br/moveis/moveis-para-sala-de-estar/poltronas-para-sala-de-estar/{i}?f=eyJxdWVyeVN0cmluZyI6W119' for i in range (1,30)]

       

    def parse(self, response, **kwargs):
        for i in response.xpath('//div[@class="cav--c-eNhzRw cav--c-eNhzRw-fyOwyl-sm-6 cav--c-eNhzRw-fLxfDQ-md-4 cav--c-eNhzRw-lhTIxp-lg-4"]'):
            name = i.xpath('.//h2[@class="cav--c-gNPphv cav--c-gNPphv-epiGtV-textStyle-bodySmallRegular cav--c-gNPphv-iAsWAM-css"]//text()').getall()
            price = i.xpath('.//span[@class="cav--c-gNPphv cav--c-gNPphv-kQaGxl-size-h4 cav--c-gNPphv-hyvuql-weight-bold cav--c-gNPphv-ihtexkH-css"]//text()').getall()
            yield {
                'name': name,
                'preco': price
            }
 
        
        