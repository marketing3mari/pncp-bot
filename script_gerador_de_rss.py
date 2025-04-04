import feedparser
import xml.etree.ElementTree as ET

# Lista com os links dos feeds RSS que você quer combinar
feeds = [
    "https://pncp.gov.br/app/editais?q=moderniza%C3%A7%C3%A3o%20de%20ilumina%C3%A7%C3%A3o&status=recebendo_proposta&pagina=1",
    "https://www.gov.br/rss.xml"
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
def criar_rss(itens, nome_arquivo="feed_combinado2.xml"):
    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")

    ET.SubElement(channel, "title").text = "Feed Combinado2"
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
