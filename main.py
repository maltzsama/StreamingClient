#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
from shared import read_json, read_config
from manager import sender


def event_hub(table_name, conn, name, group, data):
    s = sender.MessageSender(conn_str=conn, name=name, group=group)
    data_to_send = data[table_name.upper()][:100]
    s.send_batch(data_to_send)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Send some dummy data from JSON file')
    parser.add_argument('--kind', metavar='kind', type=str, help='kind of streaming', required=True)
    parser.add_argument('--table', metavar='table', type=str, help='name of table to be send to topic', required=True)
    args = parser.parse_args()

    config = read_config.ConfigReader()
    conn_str, event_name, event_group = config.get_eventhub()

    json_data = read_json.JSONReader(args.table).get_json_data()

    from time import sleep
    while True:
        if args.kind == 'eventhub':
            event_hub(args.table, conn_str, event_name, event_group, json_data)
            sleep(30)
        else:
            print("Error!")
            break
