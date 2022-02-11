import os
from zipfile import ZipFile

__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

path = os.getcwd() + '/cache/'

def clean_cache():
    if os.path.isdir(path):
        files = os.scandir(path)
        for f in files:
            os.remove(f)
    else:
        os.makedirs(path)

def cache_zip(zip_path, cache_dir):
    with ZipFile(zip_path, 'r') as zip: 
        zip.extractall(cache_dir)


def cached_files():
    list = []
    for item in os.listdir(path):
        list.append(os.path.abspath(path + item))
    return list

def find_password(list):
    for item in list:
        with open(item, 'r') as file:
            for line in file:
                if 'password' in line:
                    return line[line.find(" ") + 1:line.find('</br>')]
    

print(cached_files())
print(find_password(cached_files()))
