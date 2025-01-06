import feedparser
import xml.etree.ElementTree as ET

# Lista com os links dos feeds RSS que você quer combinar
feeds = [
    "https://www.canalrural.com.br/feed/",
    "https://newspulpaper.com/feed/",
    "https://revistaoe.info/feed/",
    "https://www.brasilmineral.com.br/rss.xml",
    "https://g1.globo.com/rss/g1/",
    "https://amanha.com.br/noticias?format=feed&type=rss",
    "https://globorural.globo.com/rss/globorural",
    "https://www.infomoney.com.br/feed/",
    "https://www.nsctotal.com.br/feed",
    "https://www.terra.com.br/rss.xml",
    "https://www.cimm.com.br/portal/noticia/rss",
    "https://petrosolgas.com.br/feed/",
    "https://exame.com/feed",
    "https://agenciabrasil.ebc.com.br/rss.xml",
    "https://petronoticias.com.br/feed/",
    "https://diariodocomercio.com.br/api/feeds/rss.xml",
]

# Função para coletar e combinar os feeds
def combinar_feeds(feed_urls):
    itens_combinados = []
    for url in feed_urls:
        print(f"Processando o feed: {url}")
        feed = feedparser.parse(url)
        for entry in feed.entries:
            item = {
                "title": entry.title,
                "link": entry.link,
                "description": getattr(entry, "description", ""),
                "pubDate": getattr(entry, "published", "Sem data")
            }
            itens_combinados.append(item)
    return itens_combinados

# Função para criar um novo feed RSS
def criar_rss(itens, nome_arquivo="feed_combinado.xml"):
    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")

    ET.SubElement(channel, "title").text = "Feed Combinado"
    ET.SubElement(channel, "link").text = "https://marketing3mari.github.io/meu-feed-rss/"
    ET.SubElement(channel, "description").text = "Feed RSS combinado de várias fontes"

    for item in itens:
        item_element = ET.SubElement(channel, "item")
        ET.SubElement(item_element, "title").text = item["title"]
        ET.SubElement(item_element, "link").text = item["link"]
        ET.SubElement(item_element, "description").text = item["description"]
        ET.SubElement(item_element, "pubDate").text = item["pubDate"]

    # Salva o arquivo
    tree = ET.ElementTree(rss)
    tree.write(nome_arquivo, encoding="utf-8", xml_declaration=True)
    print(f"Feed combinado salvo em {nome_arquivo}")

# Executa o script
if __name__ == "__main__":
    itens = combinar_feeds(feeds)
    criar_rss(itens)
