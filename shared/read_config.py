#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configparser import ConfigParser
import subprocess


class ConfigReader:
    def __init__(self, filename: str = "/config/config.ini"):
        p = subprocess.Popen(["pwd"], stdout=subprocess.PIPE)
        path = p.communicate()[0].decode("utf-8").replace('\n', '')
        self.config = ConfigParser()
        self.config.read(f"{path}{filename}")

    def get_eventhub(self) -> (str, str, str):
        conn_str = self.config.get('eventhub', 'conn_str')
        event_name = self.config.get('eventhub', 'event_name')
        group = self.config.get('eventhub', 'group')
        return conn_str, event_name, group

    def get_kafka(self):
        broadcast = self.config.get('kafka', 'broadcast')
        return broadcast

    def get_kinesis(self):
        conn_str = self.config.get('kinesis', 'conn_str')
        return conn_str
