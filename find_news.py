from Model.NeteaseNews import MainPage
from Model.NeteaseNews import News
from database import MySQL
from tqdm import tqdm

if __name__ == "__main__":
    oMain = MainPage('https://news.163.com/')
    crawDB = MySQL()
    for title, url in tqdm(oMain.news_dict.items()):
        print(title, url)
        oNews = News(url)
        crawDB.insert(title, url, oNews.get_content())
    crawDB.close()
