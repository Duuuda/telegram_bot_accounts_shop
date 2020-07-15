from os import listdir
from json import load
from json.decoder import JSONDecodeError


class IncorrectJson(Exception):
    pass


class JSON:
    def __call__(self, **kwargs):
        file_names = [file for file in listdir('.') if file[-5:].lower() == '.json']
        if len(file_names):
            with open(file_names[0], 'r', encoding='UTF-8') as file:
                try:
                    json = load(file)
                    return tuple(json.values())
                except JSONDecodeError:
                    if kwargs.get('without_exceptions'):
                        return False
                    raise IncorrectJson('failed to read json file')
        if kwargs.get('without_exceptions'):
            return False
        raise FileNotFoundError('no json files were found')
