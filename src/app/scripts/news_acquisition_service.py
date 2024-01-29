import requests


class acquisition_news:
    def __init__(self):
        pass

    def get_latest_hydrogen_news():

        url = "https://news.google.com/rss/headlines?hl=pt-br&gl=BR&ceid=BR:pt-BR&q=hidrogênio"

        response = requests.get(url)

        if response.status_code == 200:

            xml_response = response.content.decode("utf-8")

            items = xml_response.split("<item>")

            news = []
            for item in items:

                title = item.split("<title>")[1].split("</title>")[0]

                try:
                    date = item.split("<pubDate>")[1].split("</pubDate>")[0]
                except IndexError:
                    date = "Unknown"

                link = item.split("<link>")[1].split("</link>")[0]

                news_item = {
                    "title": title,
                    "date": date,
                    "link": link,
                }

                news.append(news_item)

            return news

        else:
            return None
