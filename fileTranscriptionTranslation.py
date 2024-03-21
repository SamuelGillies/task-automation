import os
from PIL import Image, ImageEnhance
from langdetect import detect
from natsort import natsorted
import pytesseract
import keys
import deepl

source_directory = './source'
destination_directory = './output'

colour_enhancement_factor = 0.0    # black and white
sharpness_enhancement_factor = 2.0      # sharpen image to max

translator = deepl.Translator(keys.deepLKey)

def main():
    for filename in natsorted(os.listdir(source_directory)):
        if not filename.startswith('.'):    # filter out .ds-store files
            file = source_directory + '/' + filename
            fileOutputSingle = destination_directory + '/' + filename[:-4] + '.txt'
            fileOutputMultiple = destination_directory + '/' + filename[:-7] + '.txt' # formatted for pages 1-9
            fileOutputMultiple2 = destination_directory + '/' + filename[:-8] + '.txt' # formatted for pages 10-99

            original_image = Image.open(file)
            colour_enhance = ImageEnhance.Color(original_image)         # conversion to black and white and sharpen image to increase image clarity for OCR
            black_white_image = colour_enhance.enhance(colour_enhancement_factor)
            sharpness_enhance = ImageEnhance.Sharpness(black_white_image)
            sharpest_image = sharpness_enhance.enhance(sharpness_enhancement_factor)

            sharpest_image.save(destination_directory + '/test.jpg')

            transcription = pytesseract.image_to_string(sharpest_image)
            language = detect(transcription)

            if language == 'en':        # logic to only use translation when the text is no english
                # print('english')
                translation = transcription
            else:
                # print('not english')
                translation = translator.translate_text(transcription, target_lang="EN-GB")

            if file[-5].isdigit():                          # formatted for Koln archive data, if last character is a digit true else false
                if file[-6].isdigit():                      # if final number > 1 character then append text to existing document
                    # print(filename, 'page 10+')
                    with open(fileOutputMultiple2, 'a') as f: 
                        f.write(str(translation))
                        f.close
                elif os.path.exists(fileOutputMultiple):    # if earlier page has been written, append text to existing document
                    # print(filename, 'file found')
                    with open(fileOutputMultiple, 'a') as f: 
                        f.write(str(translation))
                        f.close
                else:                                       # create new document
                    # print(filename, 'new file created')
                    with open(fileOutputMultiple, 'w') as f: 
                        f.write(str(translation))
                        f.close
            else:                                           # create new document as file is a single page
                # print('new file created')
                with open(fileOutputSingle, 'w') as f: 
                    f.write(str(translation))
                    f.close

    print ('task complete')

if __name__ == '__main__':
    main()