from zipfile import ZipFile

with ZipFile('archive.zip', 'a') as myzip:
    myzip.printdir()
    # info = myzip.infolist()
    # print(info[0].orig_filename)