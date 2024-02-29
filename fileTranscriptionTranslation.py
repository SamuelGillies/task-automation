import os
from PIL import Image
from natsort import natsorted
import pytesseract
import keys
import deepl

source_directory = './source'
destination_directory = './output'

translator = deepl.Translator(keys.deepLKey)

def main():
    for filename in natsorted(os.listdir(source_directory)):
        if not filename.startswith('.'):    # filter out .ds-store files
            file = source_directory + '/' + filename
            fileOutputSingle = destination_directory + '/' + filename[:-5] + '.txt'
            fileOutputMultiple = destination_directory + '/' + filename[:-7] + '.txt' # formatted for pages 1-9
            fileOutputMultiple2 = destination_directory + '/' + filename[:-8] + '.txt' # formatted for pages 10-99

            transcription = pytesseract.image_to_string(Image.open(file), lang='deu')
            translation = translator.translate_text(transcription, target_lang="EN-GB")

            if file[-5].isdigit():
                if file[-6].isdigit():
                    # print(filename, 'page 10+')
                    with open(fileOutputMultiple2, 'a') as f: 
                        f.write(str(translation))
                        f.close
                elif os.path.exists(fileOutputMultiple):
                    # print(filename, 'file found')
                    with open(fileOutputMultiple, 'a') as f: 
                        f.write(str(translation))
                        f.close
                else: 
                    # print(filename, 'new file created')
                    with open(fileOutputMultiple, 'w') as f: 
                        f.write(str(translation))
                        f.close
            else: 
                # print('new file created')
                with open(fileOutputSingle, 'w') as f: 
                    f.write(str(translation))
                    f.close


if __name__ == '__main__':
    main()