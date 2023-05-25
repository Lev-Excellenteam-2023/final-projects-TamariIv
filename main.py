import PowerpointReader


def main():
    path = r"C:\Users\tamar\Downloads\End of course exercise - kickof - upload.pptx"
    reader = PowerpointReader.PowerpointReader(path)
    reader.read_slides()
    print("end")


if __name__ == '__main__':
    main()
