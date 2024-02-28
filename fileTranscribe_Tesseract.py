import os
import csv
from PIL import Image
import pytesseract

source_directory = './source'
destination_directory = './output'


def main():

    print(pytesseract.image_to_string(Image.open('./source/test.JPG')))

    print('File conversion complete')

if __name__ == '__main__':
    main()