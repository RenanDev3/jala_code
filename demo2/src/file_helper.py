import glob, os
from pathlib import Path
import json


def search_files(path, extension):
    lista = []
    os.chdir(path)
    extension = f'*.{extension}'
    for file in glob.glob(extension):
        lista.append(f'{path}{file}')
    return lista


def read_data(files):
    content_dict = {}
    for path in files:
        try:
            with open(path, 'r') as file:
                content_dict = json.load(file)
        except Exception as e:
            print(e)
    return list(content_dict)
