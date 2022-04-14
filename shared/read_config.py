#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configparser import ConfigParser
import pathlib

class ConfigReader:
    def __init__(self, filename: str = "/config/config.ini"):
        path = str(pathlib.Path().resolve())
        self.config = ConfigParser()
        self.config.read(f"{path}{filename}")

    def get_eventhub(self) -> tuple:
        conn_str = self.config.get('eventhub', 'conn_str')
        event_name = self.config.get('eventhub', 'event_name')
        group = self.config.get('eventhub', 'group')
        return conn_str, event_name, group

    def get_kafka(self) -> tuple:
        bootstrap = self.config.get('kafka', 'bootstrap')
        topic = self.config.get('kafka', 'topic')
        return bootstrap, topic

    def get_kinesis(self) -> tuple:
        conn_str = self.config.get('kinesis', 'conn_str')
        return conn_str
