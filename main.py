import Parser
import requests

parser = Parser.Parser()


def main():
    """Основная функция
    """
    url = 'https://store.steampowered.com/search/?term=' + input()
    html_text = requests.get(url).text
    # Передача html парсеру
    appids = parser.appid(html_text)
    # Проверка на пустой список
    if len(appids) == 0:
        print('game doesn\'t exist. Closing')
        raise SystemExit(0)
    # Вывод списка
    print('Results:\n' + '\n'.join(appids.keys()))
    print('\ntype game name from list')
    name = input()
    appid = appids.get(name)
    # Проверка на корректность имени
    if appid is None:
        print('wrong name. Closing')
    else:
        url = 'https://steamcharts.com/app/' + appid
        html_text = requests.get(url).text
        # передача парсеру html документа
        parser.steam_online(html_text)


if __name__ == "__main__":
    main()
