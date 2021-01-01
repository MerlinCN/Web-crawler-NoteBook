from Model.NeteaseNews import MainPage
from database import MySQL
if __name__ == "__main__":
    oMain = MainPage('https://news.163.com/')
    for title, url in oMain.news_dict.items():
        print(title, url)
