#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

root_dir = "/home/sylvain/Wikimedia/Projets/Refonte des sites web/Blog/"

with open(root_dir + 'correspondance.csv', 'r') as correspondance:
        reader = csv.DictReader(correspondance)
        for row in reader:
            new_url = row['new_url']
            old_url = row['old_url']
            old_url_bit = old_url[25:]
            print("""
    if ( $request_filename ~ {} ) {{
        rewrite ^ {} permanent;
    }}""".format(
        old_url_bit,
        new_url
        ))
correspondance.closed