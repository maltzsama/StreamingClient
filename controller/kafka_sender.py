#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kafka import KafkaProducer


class KafkaSender:
    def __init__(self, bootstrap=None, name: str = '', group: str = '$Default'):
        if bootstrap is None:
            bootstrap = ['localhost:9092']
        self.bootstrap_server = bootstrap
        self.name = name
        self.group = group

    def send_batch(self, data: list):
        producer = KafkaProducer(bootstrap_servers=self.bootstrap_server)
        with producer:
            for n in data:
                producer.send(self.name, value=str(n))
