import scrapy
from scrapy import Request
from ..items import mangaItem

class MangaSpider(scrapy.Spider):
    name = 'manga'
    start_urls = ['https://myanimelist.net/manga.php']

    def parse(self, response):
        #Les mangas sont triés par ordre alphabétique, On cherche à aller sur les liens des différentes lettres, de A à Z
        urls = response.xpath("//div[@id='horiznav_nav']//li/a/@href").extract()
        for url in urls:
            yield Request(url, callback=self.manga_parse)

    def manga_parse(self, response):
        #On cherche à accéder aux manga un par un
        #En HTML, le tr délimite une ligne d'un tableau, la commande response.css('div.js-categories-seasonal tr ~ tr') permet de ne selectionner que les données d'une ligne, soit les données d'un manga
        i = 0
        for manga in response.css('div.js-categories-seasonal tr ~ tr'):
            #On créer notre dictionnaire avec les informations du manga de la ligne
            yield mangaItem(
                titre = manga.xpath('//a[@class="hoverinfo_trigger fw-b"]/strong/text()').extract()[i],
                synopsis = manga.xpath('//div[@class="pt4"]/text()').extract()[i],
                #les informations type, episodes et note sont contenues dans les trois derniers <td> de la ligne <tr>, on les recupère comme ça.
                genre = manga.css('td:nth-child(3)::text').extract_first(),
                episodes = manga.css('td:nth-child(4)::text').extract_first(), 
                note = manga.css('td:nth-child(5)::text').extract_first()
            )
            i+=1

        #On se dirige maintenant vers le lien des autres pages de la lettre
        urls = 'https://myanimelist.net' + response.xpath("//div[@class='spaceit']//a/@href").extract()
        for url in urls:
            yield Request(url, callback=self.manga_parse)