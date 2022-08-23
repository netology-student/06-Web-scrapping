
import requests
import bs4

# определяем список ключевых слов
KEYWORDS = ['автоматизации', 'новый', 'web', 'python', 'Сегодня']
HEADERS = {"User-Agent": "Google Chrome 53 (Win 10 x64): Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36"}

base_url = "https://habr.com"
url = base_url + "/ru/all"

def article_presentation(article):

    title_link_tag = article.find(class_="tm-article-snippet__title-link")
    href = base_url + title_link_tag.attrs['href']
    title = title_link_tag.find("span").text

    time_tag = article.find("time")
    time = time_tag.attrs['datetime']

    # Вывести в консоль список подходящих статей в формате: <дата> - <заголовок> - <ссылка>
    return f'{time} - {title} - {href}'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print(f"KEYWORDS = {KEYWORDS}")
    response = requests.get(url, headers=HEADERS)
    soup = bs4.BeautifulSoup(response.text, features='html.parser')

    result = []
    articles = soup.find_all("article")
    for article in articles:

        # Собираем текст превью без форматирования
        preview_text = ""
        p_tag_list = article.find_all("p")
        for p_tag in p_tag_list:
            preview_text = preview_text + p_tag.get_text()

        # Ищем ключевые слова
        for keyword in KEYWORDS:
            if preview_text.find(keyword) != -1:
                result.append(article)
                break

    if len(result) == 0:
        print("Статьи не найдены")
    else:
        for article in result:
            print(article_presentation(article))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
