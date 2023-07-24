import SlideData
from dataclasses import dataclass

DEFAULT_CONTEXT = "Getting the content of a slide that is a part of a powerpoint including the " \
                  "titles and paragraphs in it. Please explain the slide. " \
                  "Answers should be short but clear. Explain unfamiliar terms if needed."


@dataclass
class Query:
    query: str = ""
    context: str = ""

    def from_slide(self, data: SlideData.SlideData) -> None:
        self.context = DEFAULT_CONTEXT
        if data.titles:
            self.query += "The titles in the slide are:\n"
            self.query += '\n'.join(data.titles)
        if data.paragraphs:
            self.query += "The paragraphs in the slide are:\n"
            self.query += '\n'.join(data.titles)
