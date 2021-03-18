import os

dirs = [
    os.path.join('data','raw'),
    os.path.join('data','preprocessed'),
    'notebooks',
    'saved_models',
    'src'
]

for dir_ in dirs:
    os.makedirs(dir_,exist_ok=True)
    with open(os.path.join(dir_,'.gitkeep'),'w') as p:
        pass

file_ =[
    'dvc.yaml',
    'params.yaml',
    '.gitignore',
    os.path.join('src','__init__.py')
]

for files in file_:
    with open(files,'w') as n:
        pass 