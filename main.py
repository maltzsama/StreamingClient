#!/usr/bin/env python
# -*- coding: utf-8 -*-
from shared import read_json, read_config
from manager import sender


def event_hub(conn, name, group, data):
    s = sender.MessageSender(conn_str=conn, name=name, group=group)
    data_to_send = data[table_name.upper()][:100]
    s.send_batch(data_to_send)


if __name__ == '__main__':
    config = read_config.ConfigReader()
    conn_str, event_name, event_group = config.get_eventhub()

    table_name = 'fotografia'
    json_data = read_json.JSONReader(table_name).get_json_data()

    event_hub(conn_str, event_name, event_group, json_data)
