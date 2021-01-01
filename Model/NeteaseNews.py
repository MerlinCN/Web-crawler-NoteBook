import sys
from typing import List
from Component.Element import Text, Image
from Component.MySoup import Tag
from Model import WebModel


class News(WebModel.Website):
    except_str: List[str] = ['StartFragment', 'EndFragment']

    def __init__(self, url):
        super(News, self).__init__(url)
        try:
            self.title = self.bs.find(
                'meta', {'property': 'og:title'})['content']
            self.oBody = self.bs.find('div', {'class': 'post_body'})
        except TypeError:
            print('网页无法识别')
            sys.exit(-1)
        self.init_content()

    def tag_except(self, tag: Tag) -> bool:
        """
        标签中元素是否除外
        :rtype: bool
        """
        if tag.find('div', {'class': "video-wrapper"}):
            return True
        if tag.find('comment'):
            return True
        if tag.text in self.except_str:
            return True
        return False

    def init_content(self):
        for con in self.oBody.contents:
            if isinstance(con, Tag):
                if con.find('img'):
                    self.content.append(Image(con.get_img()))
                elif self.tag_except(con):
                    continue
                else:
                    self.content.append(Text(con.text))
            else:
                if con in self.except_str:
                    continue
                self.content.append(Text(con))

    def get_content(self) -> str:
        return '\n'.join(element.value for element in self.content)


class MainPage(WebModel.Website):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
        self.news = self.bs.find(
            'div', {'class', 'news_bj_news'}).find_all('a')
        self.news_dict = {}
        for item in self.news:
            self.news_dict[item.text] = item['href']
        