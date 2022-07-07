import os

"""
A helper to rename our model to the required after versioning
"""

indexFileVersionedName = "./models/mobileNet/indxfile.00020.index"
indexFileRequiredName =  "./models/mobileNet/interim/.00020.index"

weightFileVersionedName = "./models/mobileNet/weights.00020.data-00000-of-00001"
weightFileRequiredName = "./models/mobileNet/interim/.00020.data-00000-of-00001"

# renaming
def rename():
    os.rename(indexFileVersionedName, indexFileRequiredName)
    os.rename(weightFileVersionedName, weightFileRequiredName)

def reset_rename():
    os.rename(indexFileRequiredName,indexFileVersionedName)
    os.rename(weightFileRequiredName, weightFileVersionedName)

rename()