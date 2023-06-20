import os

Source_Path_MP3 = './MP3'
Source_Path_WAV = './WAV'

Destination_MP3 = './MP3'
Destination_WAV = './WAV'


def main():
    for filename in os.listdir(Source_Path_MP3):
            dst =  filename[0:3]

            os.rename(os.path.join(Source_Path_MP3, filename),  os.path.join(Destination_MP3, dst + '.mp3'))
            print(filename + ' renamed to ' + dst  + '.mp3')

    for filename in os.listdir(Source_Path_WAV):
        dst =  filename[0:3]

        if dst == '047': 
            rename47 = '047' + '-' + filename[39:40]
            os.rename(os.path.join(Source_Path_WAV, filename),  os.path.join(Destination_WAV, rename47 + '.wav'))
            print(filename + ' renamed to ' + str(rename47) + '.wav')
        
        elif dst == '148':
            rename148 = '148' + '-' + filename[19:20]
            os.rename(os.path.join(Source_Path_WAV, filename),  os.path.join(Destination_WAV, rename148 + '.wav')) 
            print(filename + ' renamed to ' + str(rename148) + '.wav')

        else:
            os.rename(os.path.join(Source_Path_WAV, filename),  os.path.join(Destination_WAV, dst + '.wav'))
            print(filename + ' renamed to ' + dst + '.wav')

if __name__ == '__main__':
    main()