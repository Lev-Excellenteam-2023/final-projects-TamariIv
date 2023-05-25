from pptx import Presentation
from pptx.slide import Slide

import SlideData


class PowerpointReader:
    def __init__(self, _path):
        self.powerpoint = Presentation(_path)
        self.slides_iterator = iter(self.powerpoint.slides)

    def read_slides(self):
        for i, slide in enumerate(self.powerpoint.slides):
            print("slide: ", i)
            self.extract_data(slide)
        print("end")

    def extract_data(self, slide: Slide) -> SlideData.SlideData:
        if not slide:
            return {}
        titles, body = [], []
        for shape in slide.placeholders:
            if shape.placeholder_format.type in [1, 3]:
                print("Title Placeholder:", shape.text)
            elif shape.placeholder_format.type == 2:
                print("Body Placeholder:", shape.text)
            elif shape.placeholder_format.type == 7 and shape.has_text_frame and shape.text:
                print("Body Placeholder:", shape.text)

        # for shape in slide.shapes:
        #     for ph in slide.placeholders:
        #         if ph.placeholder_format.type in [MSO_SHAPE_TYPE.]
        #     # Check if the shape is a title placeholder
        #     if shape.placeholder is not None and shape.placeholder.name == 'Title Placeholder':
        #         title = shape.text
        #         titles.append(title)
        #     # Check if the shape is a text box
        #     if shape.has_text_frame:
        #         text = ''
        #         for paragraph in shape.text_frame.paragraphs:
        #             text += paragraph.text.strip()
        #         body.append(text)
        return SlideData.SlideData(self.powerpoint.core_properties.title, titles, body)
