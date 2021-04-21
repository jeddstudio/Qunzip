import os
from os import listdir
from zipfile import ZipFile
import img2pdf

#Get Current Working Directory
zipfolder = os.getcwd()

# read all zip files in folder
for zip_files in os.listdir(zipfolder):
    if not zip_files.endswith(".zip"): # 這兩行可以用來避免'.DS_Store' problem in Mac
        continue
    # zip_name = zipfolder+zip_files #應該冇用⋯
    clean_name = os.path.splitext(zip_files)[0]
    dirname = zipfolder+'/'+clean_name

# create a folder by zip_files's name
    if zip_files.endswith('.zip'):
        os.makedirs(clean_name)
# 把zip files的圖片unzip到上面建立的folder內
    if zip_files.endswith('.zip'):
        with ZipFile(zip_files, 'r') as zipObj:
            zipObj.extractall(dirname)

# 把PDF放在當前folder內，二選一
    with open(f"{clean_name}.pdf", "wb") as f:
        imgs = []
        for pdf_files in os.listdir(dirname):
            if not pdf_files.endswith(".jpg"):
                continue
            path = os.path.join(dirname, pdf_files)
            if os.path.isdir(path):
                continue
            imgs.append(path)
            imgs.sort()
        f.write(img2pdf.convert(imgs))

# 把PDF放在圖片新開的folder內，二選一
    # pdf_path = zipfolder+'/'+'/'+clean_name+'/'+clean_name+'.pdf'
    # print(pdf_path)
    # with open(pdf_path, "wb") as f:
    #     imgs = []
    #     for pdf_files in os.listdir(dirname):
    #         if not pdf_files.endswith(".jpg"):
    #             continue
    #         path = os.path.join(dirname, pdf_files)
    #         if os.path.isdir(path):
    #             continue
    #         imgs.append(path)
    #         imgs.sort()
    #     f.write(img2pdf.convert(imgs))






# can using `rm .DS_Store` to detele this file first then run these code
