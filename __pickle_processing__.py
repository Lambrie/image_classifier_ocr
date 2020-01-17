import pickle

def writeFile(img, fileName,dir):
    # fileName = fileName.replace("\\","_")
    file = open(dir+fileName, "wb")
    pickle.dump(img, file)
    file.close()

def readFile(fileName, dir) -> bytearray:
    # fileName = fileName.replace("\\", "_")
    with open(dir + fileName, "rb") as f:
        img = pickle.load(f)
    return img

def checkFile(fileName, dir):
    from pathlib import Path
    my_file = Path(dir + fileName)
    if my_file.exists():
        return True
    else:
        return False