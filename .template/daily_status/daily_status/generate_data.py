#!/usr/local/bin/python3

from datetime import date, timedelta

import json
import os
import re

unfinished = re.compile('\*\s\[\s\].+')

@staticmethod
def copy_unfinished(yesterday):
    if os.path.exists("./markdown/daily-status/"+yesterday+".md"):
        with open("./markdown/daily-status/"+yesterday+".md", "r") as yesterday_file:
            read_content = yesterday_file.read()
            unfinished_items = re.findall(unfinished, read_content)
            return unfinished_items
    return []


if __name__ == '__main__':
    data = dict()

    today = date.today()
    yesterday = today - timedelta(days=1)
    data["today"] = today.strftime("%Y-%m-%d")
    data["yesterday"] = yesterday.strftime("%Y-%m-%d")
    # If today is Monday, we need to look at Friday's file not Saturday's
    if today.weekday() == 0:
        yesterday = today - timedelta(days=3)
        data["yesterday_items"] = copy_unfinished(yesterday.strftime("%Y_%m_%d"))
    else:
        data["yesterday_items"] = copy_unfinished(yesterday.strftime("%Y_%m_%d"))

    print(json.dumps(data, sort_keys=True, indent=4))
