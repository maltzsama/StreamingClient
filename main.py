#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
from shared import read_json, read_config
from controller import eventhub_sender
from controller import kafka_sender
from time import sleep


def event_hub(table_name, conn, name, group, data):
    s = eventhub_sender.EventHubSender(conn_str=conn, name=name, group=group)
    data_to_send = data[table_name.upper()][:100]
    s.send_batch(data_to_send)


def kafka(table_name, bootstrap, topic, data):
    s = kafka_sender.KafkaSender(bootstrap=bootstrap)
    data_to_send = data[table_name.upper()][:100]
    s.send_batch(topic, data_to_send)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Send some dummy data from JSON file')
    parser.add_argument('--kind', metavar='kind', type=str, help='kind of streaming', required=True)
    parser.add_argument('--table', metavar='table', type=str, help='name of table to be send to topic', required=True)
    args = parser.parse_args()

    json_data = read_json.JSONReader(args.table).get_json_data()
    config = read_config.ConfigReader()

    if args.kind == 'eventhub':
        conn_str, event_name, event_group = config.get_eventhub()
        while True:
            event_hub(table_name=args.table, conn=conn_str, name=event_name, group=event_group, data=json_data)
            sleep(30)

    elif args.kind == 'kafka':
        bootstrap, topic = config.get_kafka()
        while True:
            kafka(table_name=args.table, bootstrap=[bootstrap], topic=topic, data=json_data)
            sleep(30)

    else:
        print("Error!")
