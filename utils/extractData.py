import zipfile

"""
A zip extract for the dataset. 
"""

DATASET_PATH = "./data/processed/dataset.zip"

DESTINATION_PATH = "./data/interim/"

unzipping  = zipfile.ZipFile(DATASET_PATH)

def extractData():
    unzipping.extractall(path=DESTINATION_PATH)
    unzipping.close()
