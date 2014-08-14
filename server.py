#!/usr/bin/python

import uwsgi
from time import sleep

print(
    '\n* server #{} is up on port 200{}\n'.format(
        uwsgi.mule_id(),
        uwsgi.mule_id()
    )
)

while True:
    sleep(1)
