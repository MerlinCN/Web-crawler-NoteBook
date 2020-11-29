class Element:
    def __init__(self, value):
        self.value = value


class Text(Element):
    def __init__(self, value):
        super(Text, self).__init__(value)


class Image(Element):
    def __init__(self, value):
        super(Image, self).__init__(value)
