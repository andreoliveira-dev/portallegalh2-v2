import requests


class acquisition_news:
    def __init__(self):
        pass

    def get_latest_hydrogen_news():
        # Obtém a URL das últimas notícias do Google
        url = "https://news.google.com/rss/headlines?hl=pt-br&gl=BR&ceid=BR:pt-BR&q=hidrogênio"

        # Faz uma solicitação GET para a URL
        response = requests.get(url)

        # Verifica se a solicitação foi bem-sucedida
        if response.status_code == 200:
            # Converte a resposta em um objeto XML
            xml_response = response.content.decode("utf-8")

            # Obtém os elementos `item` do XML
            items = xml_response.split("<item>")

            # Cria uma lista de notícias
            news = []
            for item in items:
                # Obtém o título da notícia
                title = item.split("<title>")[1].split("</title>")[0]

                # Obtém a data da notícia
                try:
                    date = item.split("<pubDate>")[1].split("</pubDate>")[0]
                except IndexError:
                    date = "Unknown"

                # Obtém o link da notícia
                link = item.split("<link>")[1].split("</link>")[0]

                # Cria um objeto de notícia
                news_item = {
                    "title": title,
                    "date": date,
                    "link": link,
                }

                # Adiciona o objeto de notícia à lista
                news.append(news_item)

            return news

        else:
            return None
