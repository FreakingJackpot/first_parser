import lxml.html as html
from lxml import etree


class Parser:
    def appid(self, html_text):
        """[summary]
        Парсит страницу запроса стима и находит имя игры и ключ
        Args:
            html_text ([string]): [html документ ввиде строки]

        Returns:
            [dict]: [словарь с играми, где ключ - название игры,
            а значение - appid в стиме]
        """
        search_result = {}
        tree = html.document_fromstring(html_text)
        text_original = tree.xpath('//*[@id="search_resultsRows"]/a')
        for item in text_original:
            name = item.get('href').split('/')
            search_result.update({name[5]: item.get('data-ds-appid')})
        return search_result

    def steam_online(self, html_text):
        """[summary
        Парсит страницу игры в steam charts и находит  колличество игроков
        сейчас, пик за 24, и пик за все время
        Args:
            html_text ([string]): [html документ ввиде строки]
        """
        tree = html.document_fromstring(html_text)
        current = tree.xpath('/html/body/div[3]/div[3]/div[1]/span/text()')
        day_peak = tree.xpath('/html/body/div[3]/div[3]/div[2]/span/text()')
        all_time_peak = tree.xpath(
            '/html/body/div[3]/div[3]/div[3]/span/text()')
        print('Playing now: ' + current[0] + '\n' + '24-hour peak: ' +
              day_peak[0] + '\n' + 'all-time peak: ' + all_time_peak[0])
