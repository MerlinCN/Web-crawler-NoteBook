from bs4 import element
from bs4 import BeautifulSoup as Soup


class Tag(element.Tag):
    def get_img(self):
        return self.find('img')['src']


class BeautifulSoup(Soup, Tag):
    def insert_after(self, successor):
        super(BeautifulSoup, self).insert_after(successor)

    def insert_before(self, successor):
        super(BeautifulSoup, self).insert_before(successor)

    def handle_starttag(self, name, namespace, nsprefix, attrs, sourceline=None,
                        sourcepos=None):
        """Called by the tree builder when a new tag is encountered.

        :param name: Name of the tag.
        :param nsprefix: Namespace prefix for the tag.
        :param attrs: A dictionary of attribute values.
        :param sourceline: The line number where this tag was found in its
            source document.
        :param sourcepos: The character position within `sourceline` where this
            tag was found.

        If this method returns None, the tag was rejected by an active
        SoupStrainer. You should proceed as if the tag had not occurred
        in the document. For instance, if this was a self-closing tag,
        don't call handle_endtag.
        """
        # print("Start tag %s: %s" % (name, attrs))
        self.endData()

        if (self.parse_only and len(self.tagStack) <= 1
                and (self.parse_only.text
                     or not self.parse_only.search_tag(name, attrs))):
            return None

        tag = self.element_classes.get(Tag, Tag)(
            self, self.builder, name, namespace, nsprefix, attrs,
            self.currentTag, self._most_recent_element,
            sourceline=sourceline, sourcepos=sourcepos
        )
        if tag is None:
            return tag
        if self._most_recent_element is not None:
            self._most_recent_element.next_element = tag
        self._most_recent_element = tag
        self.pushTag(tag)
        return tag
