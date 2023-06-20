# task-automation
A collection of scripts for the automation of different tasks

## FileRename_HeritageQuay
A script to rewrite the contents of two folders on the Heritage Quay digital archive in one go. 

### Instructions for use 
1. Download the FileRename_HeritageQuay.py file to your computer

2. Open **cmd** application 

3. Locate the folder containing the audio you wish to convert. You want the folder that contains both the MP3 and WAV folders. This will be referred to as the 'Audio' folder. 

![Example file directory structure](/images/source_folder.png)

4. In **cmd** enter: 

```
cd 
```

Make sure there is a space after this command.

5. Drag the Audio folder into **cmd**. The file path should populate. Press enter. 

6. In cmd, type:

```
python3
```

add a space, and then drag the FileRename_HeritageQuay.py file into **cmd**. The file path should populate. Press enter. 

7. Check the MP3 and WAV folders – they should now contain audio files that have been renamed. 