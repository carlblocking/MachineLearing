from os import scandir

path="C:/Users/Administrator/Desktop/hunan"

def test_scandir(path):
    for file in scandir(path):
        if file.name.endswith('jpg') and file.is_file():
            print(file.path)
        
test_scandir(path)

 


























