import os
from zipfile import ZipFile
from pathlib import Path

__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

path = Path(os.path.realpath(__file__)).parent.absolute()
cache_path = path / 'cache' 

def clean_cache():
    if os.path.isdir(cache_path):
        files = os.scandir(cache_path)
        for f in files:
            os.remove(f)
    else:
        os.makedirs(path)

def cache_zip(zip_path = path / 'data.zip', cache_dir = path / 'cache'):
    with ZipFile(zip_path, 'r') as zip: 
        zip.extractall(cache_dir)

def cached_files():
    list = []
    for item in os.listdir(cache_path):
        list.append(os.path.realpath(cache_path / item))
    return list

def find_password(list):
    for item in list:
        with open(item, 'r') as file:
            for line in file:
                if 'password' in line:
                    return line[line.find("password: ") + len("password: "):line.find('</br>')]
    
