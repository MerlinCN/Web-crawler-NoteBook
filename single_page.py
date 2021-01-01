from Model.NeteaseNews import News

if __name__ == '__main__':
    url = input('请输入网址')
    oNews: News
    oNews = News(url)
    '''
    code start
    '''
    print(f"\033[31m{oNews.title}\033[0m")
    print(oNews.get_content())
