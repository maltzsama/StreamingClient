#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import pathlib


class JSONReader:
    def __init__(self, table_name: str = '', file_path: str = '/data'):
        path = str(pathlib.Path().resolve())
        self.table_name = table_name
        self.file_path = f"{path}{file_path}/{table_name}.json"

    def get_file_data(self):
        file = open(f'{self.file_path}')
        return file

    def get_json_data(self):
        return json.load(self.get_file_data())
