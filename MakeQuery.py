import SlideData


class Query:
    def __init__(self):
        self.query = ''
        self.context = ''

    def from_slide(self, data: SlideData.SlideData) -> None:
        self.context = "Getting the content of a slide that is a part of a powerpoint including the " \
                       "titles and paragraphs in it. Please explain the slide. " \
                       "Answers should be short but clear. Explain unfamiliar terms if needed."
        q = ""
        if data.titles:
            q += "The titles in the slide are:\n"
        for t in data.titles:
            q += t + '\n'
        if data.paragraphs:
            q += "The paragraphs in the slide are:\n"
        for p in data.paragraphs:
            q += p + '\n'
