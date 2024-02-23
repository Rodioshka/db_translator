import logging
import os
from typing import Any


class Writer:
    @staticmethod
    def save_data(file_name: str, file_format: str, data: Any, file_folder: str = None, ) -> None:
        if not file_folder:
            file_folder = file_name
        path = fr'{file_folder}'

        if not os.path.isdir(path):
            os.makedirs(path)

        with open(fr'{path}/{file_name}.{file_format}', 'w', encoding='utf-8') as file:
            file.write(''.join(data))
            logging.info(fr'Файл сохранен по пути: {file_folder}\{file_name}')


writer = Writer()
