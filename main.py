import collections
import collections.abc
import os
import PowerpointReader
import JsonWriter


def main():
    path = r"C:\Users\tamar\Downloads\End of course exercise - kickof - upload.pptx"
    reader = PowerpointReader.PowerpointReader(path)
    data_list = reader.read_slides()
    data = [
        {
            "name": "John Doe",
            "age": 30,
            "city": "New York"
        },
        {
            "name": "John Dee",
            "age": 23,
            "city": "York"
        },
        {
            "name": "MJ Doe",
            "age": 34,
            "city": "Seattle"
        },
    ]
    JsonWriter.to_json(os.path.splitext(os.path.basename(path))[0], data)
    print("end")


if __name__ == '__main__':
    main()
