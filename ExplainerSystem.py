import asyncio
import os
import time
import threading
from flask import Flask
from datetime import datetime

import Explainer
import JsonWriter
import MakeQuery
from PowerpointReader import PowerpointReader

# app = Flask(__name__)
# TODO: Make it work from every working directory
UPLOADS_FOLDER = 'uploads'
OUTPUTS_FOLDER = 'outputs'


async def process_file(filename):
    reader = PowerpointReader(UPLOADS_FOLDER + "/" + filename)
    data_list = reader.read_slides()
    tasks = []
    for slide_data in data_list:
        query = MakeQuery.Query()
        query.from_slide(slide_data)
        task = asyncio.create_task(Explainer.get_explanation(query))
        tasks.append(task)
    explanations = await asyncio.gather(*tasks)
    json_filename = os.path.splitext(filename)[0]
    JsonWriter.to_json(OUTPUTS_FOLDER + "/" + json_filename, *explanations)


def is_file_processed(filename):
    files = os.listdir(OUTPUTS_FOLDER)
    for file in files:
        if filename in file:
            return True
    return False


def explainer():
    while True:
        # Scan the uploads folder for unprocessed files
        for filename in os.listdir(UPLOADS_FOLDER):
            if filename.endswith('.pptx') and not is_file_processed(filename):
                print(f"started processing file: {filename}" + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                asyncio.run(process_file(filename))
                print(f"finished processing file: {filename}" + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(10)


def start():
    explainer_thread = threading.Thread(target=explainer)
    explainer_thread.start()


if __name__ == '__main__':
    start()
