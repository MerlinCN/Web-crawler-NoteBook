from typing import List
import sys
from Model import WebModel
from Component.MySoup import Tag, BeautifulSoup
from Component.Element import Text, Image


class News(WebModel.Website):
    except_str: List[str] = ['StartFragment', 'EndFragment']

    def __init__(self, url):
        super(News, self).__init__(url)
        try:
            self.title = self.bs.find('meta', {'property': 'og:title'})['content']
            self.oBody = self.bs.find('div', {'class': 'post_text'})
        except TypeError:
            print('网页无法识别')
            sys.exit(-1)
        self.initContent()

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

    def initContent(self):
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

    def getContent(self) -> str:
        return '\n'.join(element.value for element in self.content)
