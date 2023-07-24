class SlideData:
    def __init__(self, _ppt_title: str, _titles: list[str], _paragraphs: list[str]):
        self.ppt_title = _ppt_title
        self.titles = _titles
        self.paragraphs = _paragraphs

    def slide_is_empty(self) -> bool:
        return not (self.ppt_title and (self.titles or self.paragraphs))
