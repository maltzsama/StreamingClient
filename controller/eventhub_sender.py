#!/usr/bin/env python
# -*- coding: utf-8 -*-

from azure.eventhub import EventHubProducerClient
from azure.eventhub import EventData


class EventHubSender:
    def __init__(self, conn_str: str = '', name: str = '', group: str = '$Default'):
        self.conn_str = conn_str
        self.name = name
        self.group = group

    def send_batch(self, data: list):
        producer = EventHubProducerClient.from_connection_string(
            conn_str=self.conn_str,
            consumer_group=self.group,
            eventhub_name=self.name
        )
        with producer:
            event_data_batch = producer.create_batch()
            for n in data:
                event_data_batch.add(EventData(str(n)))
            producer.send_batch(event_data_batch)

