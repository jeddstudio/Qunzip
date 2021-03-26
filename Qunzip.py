
import os
from os import listdir
from zipfile import ZipFile

zipfolder = os.getcwd()

for zipname in os.listdir(zipfolder):
    zip_name = zipfolder+zipname
    clean_name = os.path.splitext(zipname)[0]

    if zipname.endswith('.zip'):
        os.makedirs(clean_name)

    if zipname.endswith('.zip'):
        with ZipFile(zipname, 'r') as zipObj:
            zipObj.extractall(zipfolder+'/'+clean_name)

    list = os.listdir(zipfolder+'/'+clean_name)
    new_list = [x for x in list if x.endswith(".jpg")]
    print("Total number of images to convert is: ", len(new_list))

# waiting to fix '.DS_Store' problem in Mac
# can using `rm .DS_Store` to detele this file first then run these code
