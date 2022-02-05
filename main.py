import os
import pathlib
import glob
from zipfile import ZipFile

__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

path = str(pathlib.Path(__file__).parent.absolute()) + '/cache'

def clean_cache():
    files = glob.glob(path + '/*')
    if os.path.exists(path):
        for f in files:
            os.remove(f)
    else:
        os.makedirs(path)

def cache_zip(zip_path, cache_dir):
    with ZipFile(zip_path, 'r') as zip: 
        zip.extractall(cache_dir)


def cached_files():
    list = []
    for item in glob.glob(f'{path}/*'):
        list.append(item)
    return list

def find_password(list):
    for item in list:
        with open(item, 'r') as file:
            for line in file:
                if 'password' in line:
                    secret_code = line[:line.find('</br>')]
    return secret_code
